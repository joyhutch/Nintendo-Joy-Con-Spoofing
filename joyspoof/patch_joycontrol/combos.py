


from joycontrol.command_line_interface import CLI
from joycontrol.controller_state import ControllerState


def register_combos(controller_state: ControllerState, cli: CLI):
    """
    Commands registered here can use the given controller state.
    The doc string of commands will be printed by the CLI when calling "help"
    :param cli:
    :param controller_state:
    """

    async def n(*args):
        """
        n - performs a neutral arial attack 
        """
        pass

    cli.add_command(n.__name__, n)
    