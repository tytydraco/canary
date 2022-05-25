from src.logging.log import Log


class Parser:
    @staticmethod
    def handle_command(command):
        Log.dbg(f'Parser handling: {command}')
