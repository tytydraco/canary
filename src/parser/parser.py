from src.commands.reboot import Reboot
from src.commands.upgrade import Upgrade
from src.logging.log import Log


class Parser:
    command_map = dict({
        'reboot': Reboot,
        'upgrade': Upgrade,
    })

    @staticmethod
    def handle_command(command):
        Log.dbg(f'Parser handling: {command}')

        # Create instance of Command and execute it
        if command in Parser.command_map:
            command_inst = Parser.command_map[command]()
            command_inst.execute()
