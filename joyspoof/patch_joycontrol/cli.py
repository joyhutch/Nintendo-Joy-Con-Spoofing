from multiprocessing import Queue
from joycontrol.command_line_interface import ControllerCLI
from joycontrol.controller_state import ControllerState
from joycontrol.run_controller_cli import _register_commands_with_controller_state
from .combos import register_combos


class QueueCLI(ControllerCLI):
    def __init__(self, controller_state: ControllerState, queue: Queue):
        super().__init__(controller_state)
        self.queue = queue
        _register_commands_with_controller_state(controller_state, self)
        register_combos(controller_state, self)

    async def get_input(self):
        return self.queue.get()
