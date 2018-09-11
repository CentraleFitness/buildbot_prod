import os
import argparse

from utils.exec import exec_cmd


def is_pid_running(pid_file: str) -> bool:
    try:
        with open(pid_file, 'r') as fhandler:
            pid = int(fhandler.read())
        os.kill(pid, 0)
    except Exception:
        return False
    return True

parser = argparse.ArgumentParser(description="Start or reload a service")
parser.add_argument("service", type=str)
parser.add_argument("-p", "--pidfile", type=str)
args = parser.parse_args()

if args.pidfile and not is_pid_running(args.pidfile):
    print(f"Starting {args.service}...")
    ret = exec_cmd(f"/etc/init.d/{args.service} start")
    if ret['code'] != 0:
        print(ret['out'])
        exit(1)
else:
    print(f"Reloading {args.service}...")
    ret = exec_cmd(f"/etc/init.d/{args.service} reload")
    if ret['code'] != 0:
        print(ret['out'])
        exit(1)
