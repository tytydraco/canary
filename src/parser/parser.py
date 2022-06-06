from src.commands.gitpull import GitPull
from src.commands.ping import Ping
from src.commands.reboot import Reboot
from src.commands.selfupdate import SelfUpdate
from src.commands.upgrade import Upgrade
from src.logging.log import Log


class Parser:
    command_map = dict({
        'reboot': Reboot,
        'upgrade': Upgrade,
        'ping': Ping,
        'gitpull': GitPull,
        'selfupdate': SelfUpdate,
    })

    @staticmethod
    def handle_command(command):
        Log.dbg(f'Parser handling: {command}')

        # Create instance of Command and execute it
        if command in Parser.command_map:
            command_inst = Parser.command_map[command]()
            command_inst.execute()
            return True
        else:
            return False
