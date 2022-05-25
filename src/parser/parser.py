from src.commands.command import Command
from src.commands.reboot import Reboot
from src.logging.log import Log


class Parser:
    command_map = dict[str, Command]({
        'reboot': Reboot,
    })

    @staticmethod
    def handle_command(command):
        Log.dbg(f'Parser handling: {command}')

        # Create instance of Command and execute it
        if command in Parser.command_map:
            p = Parser.command_map[command]()
            p.execute()
