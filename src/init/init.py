import glob
import pathlib
import subprocess

from other.config import INIT
from src.logging.log import Log


class Init:
    init_path = pathlib.Path(__file__).parent.resolve()

    @staticmethod
    def run_init_scripts():
        if not INIT:
            return

        scripts = glob.glob(f'{Init.init_path}/**/*.sh', recursive=True)
        Log.dbg(f'Found scripts: {scripts}')
        for script in scripts:
            Log.dbg(f'Executing script: {script}')
            subprocess.call(script, shell=True)
