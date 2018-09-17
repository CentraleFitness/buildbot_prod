import os
import sys
import argparse

from utils.exec import exec_cmd

PID_BASEDIR = "/var/run"

def is_pid_running(pid_file: str) -> bool:
    try:
        with open(pid_file, 'r') as fhandler:
            pid = int(fhandler.read())
        os.kill(pid, 0)
    except Exception:
        return False
    return True

parser = argparse.ArgumentParser(description="Start or reload a UWSGI process")
parser.add_argument("api", type=str)
parser.add_argument("uwsgidir", type=str)
args = parser.parse_args()

if is_pid_running(f"{PID_BASEDIR}/{args.api}.pid"):
    print("Reloading uwsgi...")
    ret = exec_cmd(f"{args.uwsgidir}/reload.sh")
else:
    print("Starting uwsgi...")
    ret = exec_cmd(f"{args.uwsgidir}/start.sh")
sys.exit(ret["code"])
