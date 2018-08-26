import os
import subprocess
import argparse

from utils.exec import exec_cmd

WORKERS_DIR = "/var/buildbot/workers"


parser = argparse.ArgumentParser(
    description='Create/Update the virtualenv of the worker')
parser.add_argument('worker', type=str, help='worker name')
parser.add_argument('builder', type=str, help='builder name')
parser.add_argument('-r', '--requirements', type=str,
                    help='pip requirements to install')
args = parser.parse_args()

venv_dir = f"{WORKERS_DIR}/{args.worker}/venv/"
build_dir = f"{WORKERS_DIR}/{args.worker}/{args.builder}/build/"

if not os.path.isdir(venv_dir):
    print(f"Creating the virtualenv in {venv_dir}")
    ret = exec_cmd(["python3", "-m", "venv", venv_dir])
    if ret["code"] != 0:
        print(ret["out"])
        exit(1)
ret = exec_cmd([venv_dir + 'bin/pip', 'install', '-r', build_dir + args.requirements])
if ret["code"] != 0:
    print(ret["out"])
    exit(2)
