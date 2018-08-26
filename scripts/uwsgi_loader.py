import os
import subprocess
import argparse

UWSGI_SCRIPT_DIR = "/home/buildbot/uwsgi"
PID_BASEDIR = "/var/run/buildbot"

def is_pid_running(pid_file: str) -> bool:
    try:
        with open(pid_file, 'r') as fhandler:
            pid = int(fhandler.read())
        os.kill(pid, 0)
    except Exception:
        return False
    return True


def exec_cmd(cmd: list, timeout: int=60) -> dict:
    """Execute a given command in the shell"""
    ret = {"code": 0}
    try:
        ret["out"] = subprocess.check_output(
            cmd,
            shell=True,
            universal_newlines=True,
            stderr=subprocess.STDOUT,
            timeout=timeout)
    except subprocess.CalledProcessError as exc:
        ret["code"] = exc.returncode
        ret["out"] = str(exc.output)
    except Exception as exc:
        ret["code"] = 1
        ret["out"] = str(exc)
    return ret

parser = argparse.ArgumentParser(description="Start or reload a UWSGI process")
parser.add_argument("api", type=str)
args = parser.parse_args()

if is_pid_running(f"{PID_BASEDIR}/{args.api}.pid"):
    print("Reloading uwsgi...")
    exec_cmd(f"{UWSGI_SCRIPT_DIR}/{args.api}/reload.sh")
else:
    print("Starting uwsgi...")
    exec_cmd(f"{UWSGI_SCRIPT_DIR}/{args.api}/startup.sh")