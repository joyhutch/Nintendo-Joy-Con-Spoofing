
from collections import defaultdict

from asyncio import sleep
from joycontrol.controller_state import ControllerState, button_push, button_press, button_release

from .cli import QueueCLI

DIRS = defaultdict(str, {
    'u': 'up',
    'd': 'down',
    'l': 'left',
    'r': 'right',
    'c': 'center',
})


def register_combos(controller_state: ControllerState, cli: QueueCLI):
    """
    Commands registered here can use the given controller state.
    The doc string of commands will be printed by the CLI when calling "help"
    :param cli:
    :param controller_state:
    """

    async def n():
        """
        Neutral Air Attack (Jump + A) 
        """
        await controller_state.connect()

        await button_push(controller_state, "x")
        await button_push(controller_state, "a")
        pass

    cli.add_command(n.__name__, n)

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
        Throw [Direction] (Grab + Direction)
        """
        dir = DIRS[d]
        await controller_state.connect()
        await button_push(controller_state, 'l')


        await cli.cmd_stick("l", dir)
        await cli.cmd_stick("l", "center")

    cli.add_command(throw.__name__, throw)

    async def f(d):
        """
        Face the given direction
        """
        dir = DIRS[d]
        await controller_state.connect()
        await cli.cmd_stick("l", dir)
        await sleep(.1)
        await cli.cmd_stick("l", "center")

    cli.add_command(f.__name__, f)

    async def m(d):
        """
        Move in the given direction
        """
        dir = DIRS[d]
        await controller_state.connect()
        await cli.cmd_stick("l", dir)

    cli.add_command(m.__name__, m)
    