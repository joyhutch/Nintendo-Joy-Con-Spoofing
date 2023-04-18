
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
        await button_push(controller_state, 'l')

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
        await sleep(.1)
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
        sleep(0.1)
        await cli.cmd_stick("r", "center")

    cli.add_command(m.__name__, m)

    async def t(d):
        """
        Tilt attack in the given direction (Tap Left Stick + Direction + A)
        """
        await controller_state.connect()
        await cli.cmd_stick("l", dir)
        await button_press(controller_state, "a")
        await cli.cmd_stick("l", "center")

    cli.add_command(t.__name__, t)

    async def c1():
        """
        Arial combo - Jump > A > Up Smash 
        """
        await controller_state.connect()
        await button_press(controller_state, "x")
        sleep(1)
        await button_press(controller_state, "a")
        await s("up")

    cli.add_command(c1.__name__, c1)

    async def c2():
        """
        Ground combo - Up Smash > Up Tilt > X > Up Air > Up Air > Up Special
        """
        await controller_state.connect()
        await s("up")
        sleep(0.5)
        await t("up")
        sleep(0.5)
        await button_press("x")
        sleep(0.1)
        await t("up")
        sleep(0.1)
        await t("up")
        sleep(0.3)
        await r()

    cli.add_command(c2.__name__, c2)
