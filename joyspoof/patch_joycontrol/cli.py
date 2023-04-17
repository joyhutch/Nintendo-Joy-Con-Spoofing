

from multiprocessing import Queue
import shlex
from joycontrol.command_line_interface import ControllerCLI
from joycontrol.controller_state import button_push, ControllerState
from joycontrol.transport import NotConnectedError


class QueueCLI(ControllerCLI):
    def __init__(self, controller_state: ControllerState, queue: Queue):
        super().__init__(controller_state)
        self.queue = queue

    async def run(self):
        while True:
            user_input = self.queue.get()
            if not user_input.strip():
                continue

            buttons_to_push = []

            for command in user_input.split('&&'):
                cmd, *args = shlex.split(command)

                if cmd == 'exit':
                    return

                available_buttons = self.controller_state.button_state.get_available_buttons()

                if hasattr(self, f'cmd_{cmd}'):
                    try:
                        result = await getattr(self, f'cmd_{cmd}')(*args)
                        if result:
                            print(result)
                    except Exception as e:
                        print(e)
                elif cmd in self.commands:
                    try:
                        result = await self.commands[cmd](*args)
                        if result:
                            print(result)
                    except Exception as e:
                        print(e)
                elif cmd in available_buttons:
                    buttons_to_push.append(cmd)
                else:
                    print('command', cmd, 'not found, call help for help.')

            if buttons_to_push:
                await button_push(self.controller_state, *buttons_to_push)
            else:
                try:
                    await self.controller_state.send()
                except NotConnectedError:
                    print('Warning: Connection was lost.')
                    return
