#!/usr/bin/env python3

import os
import time
import argparse
import asyncio
import logging

from multiprocessing import Process
from multiprocessing import Queue

from joycontrol.controller import Controller
from joycontrol.memory import FlashMemory
from joycontrol.protocol import controller_protocol_factory
from patch_joycontrol.cli import QueueCLI
from patch_joycontrol.server import create_hid_server

log = logging.getLogger(__name__)
log.setLevel(logging.INFO)


async def run(iteration, queue, reconnect_bt_addr=None):

    factory = controller_protocol_factory(Controller.PRO_CONTROLLER,
                                          reconnect=reconnect_bt_addr,
                                          spi_flash=FlashMemory(default_stick_cal=True))

    ctl_psm, itr_psm = 17, 19

    if iteration == 0:
        log.info('Welcome to Nintendo Joy-Con Spoofing')
    else:
        log.info('Reconnecting...')
    if iteration == 0:
        log.info(
            'Waiting for Switch to connect, Please open the "Change Grip/Order" menu')

    _, protocol, ns_addr = await create_hid_server(factory,
                                                   reconnect_bt_addr=reconnect_bt_addr,
                                                   ctl_psm=ctl_psm,
                                                   itr_psm=itr_psm,
                                                   unpair=not reconnect_bt_addr)
    controller_state = protocol.get_controller_state()
    await controller_state.connect()

    if not reconnect_bt_addr:
        reconnect_bt_addr = ns_addr
        queue.put(ns_addr)

    if iteration == 0:  # first iteration we need to pair and connect
        log.info('Nintendo Switch Address: %s', reconnect_bt_addr)
        controller_state.button_state.set_button('a', pushed=True)
        await controller_state.send()
        while True:
            await asyncio.sleep(0.2)

    queue.put('unlock')  # unlock console

    # create and run the cli
    await QueueCLI(controller_state, queue).run()


def runner(loop, iteration_count, queue, switch_addr):
    try:
        loop.run_until_complete(
            run(iteration_count, queue, switch_addr)
        )
    except:
        pass


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-r', '--reconnect_bt_addr', type=str, default=None,
                        help='The Switch console Bluetooth address (or "auto" for automatic detection), for reconnecting as an already paired controller.')
    args = parser.parse_args()

    loop = asyncio.get_event_loop()

    def handle_exception(*_a, **_kw):
        tasks = [t for t in asyncio.all_tasks() if t is not
                 asyncio.current_task()]
        for task in tasks:
            task.cancel()
    loop.set_exception_handler(handle_exception)

    queue = Queue()

    switch_addr = args.reconnect_bt_addr
    begin = 1 if switch_addr else 0

    for iteration in range(begin, 2):
        p = Process(target=runner, args=(
            loop, iteration, queue, switch_addr))
        p.start()

        if iteration == 0:
            switch_addr = queue.get()  # wait nintendo switch address
            p.join()
        else:
            queue.get()  # lock console
        prev_cmd = None
        while p.is_alive():
            try:
                cmd = input('cmd >> ')
            except EOFError:
                cmd = 'q'  # ctrl+d == quit
            if cmd in ['exit', 'quit', 'q', 'bye', 'shutdown']:
                p.kill()
                break
            if not cmd and prev_cmd:
                cmd = prev_cmd
            else:
                prev_cmd = cmd

            queue.put(cmd)

        # wait reconnection
        time.sleep(2)  # important 2 or more

    log.info("Exiting.")


if __name__ == '__main__':
    # check if root
    if os.geteuid() != 0:
        raise PermissionError('Script must be run as root!')
    main()
