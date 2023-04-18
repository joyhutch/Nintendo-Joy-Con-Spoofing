from asyncio import sleep
from joycontrol.controller_state import (
    ControllerState,
    button_push,
)
import logging
from joycontrol.command_line_interface import DIRS, ControllerCLI

log = logging.getLogger(__name__)
log.setLevel(logging.DEBUG)


def register_combos(controller_state: ControllerState, cli: ControllerCLI):
    """
    Commands registered here can use the given controller state.
    The doc string of commands will be printed by the CLI when calling "help"
    :param cli:
    :param controller_state:
    """

    async def r():
        """
        Recovery Move (Up B)
        """
        await controller_state.connect()
        await cli.cmd_stick("l", "up")
        await button_push(controller_state, "b")
        await cli.cmd_stick("l", "center")

    cli.add_command(r.__name__, r)

    async def throw(d):
        """
        Throw in the given direction (Grab + Direction)
        """
        dir = DIRS[d]
        await controller_state.connect()
        await button_push(controller_state, "l")

        await cli.cmd_stick("l", dir)
        await cli.cmd_stick("l", "center")

    cli.add_command(throw.__name__, throw)

    async def f(d):
        """
        Face the given direction (Tap Left Stick + Direction)
        """
        dir = DIRS[d]
        await controller_state.connect()
        await cli.cmd_stick("l", dir)
        await sleep(0.1)
        await cli.cmd_stick("l", "center")

    cli.add_command(f.__name__, f)

    async def m(d):
        """
        Move in the given direction (Hold Left Stick + Direction)
        """
        dir = DIRS[d]
        await controller_state.connect()
        await cli.cmd_stick("l", dir)

    cli.add_command(m.__name__, m)

    async def s(d):
        """
        Smash attack in the given direction (Tap Right Stick + Direction)
        """
        dir = DIRS[d]
        await controller_state.connect()
        await cli.cmd_stick("r", dir)
        await sleep(0.05)
        await cli.cmd_stick("r", "center")

    cli.add_command(s.__name__, s)

    async def t(d):
        """
        Tilt attack in the given direction (Tap Left Stick + Direction + A)
        """
        dir = DIRS[d]
        await controller_state.connect()
        await cli.cmd_stick("l", dir)
        await button_push(controller_state, "a")
        await cli.cmd_stick("l", "center")

    cli.add_command(t.__name__, t)

    async def c1():
        """
        Arial combo - Jump > A > Up Smash
        """
        await controller_state.connect()
        await button_push(controller_state, "x")
        await sleep(0.5)
        await button_push(controller_state, "a")
        await s("up")

    cli.add_command(c1.__name__, c1)

    async def c2():
        """
        Ground combo - Up Smash > Up Tilt > X > Up Air > Up Air > Up Special
        """
        await controller_state.connect()
        await s("up")
        log.debug("up smash")
        await sleep(0.1)
        await t("up")
        log.debug("tilt up")
        await sleep(0.1)
        await button_push("x")
        log.debug("jump")
        await sleep(0.05)
        await t("up")
        log.debug("tilp up")
        await sleep(0.05)
        await t("up")
        log.debug("tilp up")
        await sleep(0.1)
        await r()
        log.debug("recovery")

    cli.add_command(c2.__name__, c2)
