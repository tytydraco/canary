import glob
import pathlib
import subprocess

from src.logging.log import Log


class Init:
    init_path = pathlib.Path(__file__).parent.resolve()

    @staticmethod
    def run_init_scripts():
        scripts = glob.glob(f'{Init.init_path}/**/*.sh', recursive=True)
        Log.dbg(f'Found scripts: {scripts}')
        for script in scripts:
            Log.dbg(f'Executing script: {script}')
            subprocess.call(script, shell=True)
