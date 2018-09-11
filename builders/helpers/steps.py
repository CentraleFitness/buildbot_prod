from buildbot.plugins import steps

PYTHON_EX = "/var/buildbot/venv/bin/python3"


def venv_step(worker: str, builder: str, requirements: str='requirements.txt'):
    return steps.ShellCommand(
        command=[
            PYTHON_EX, "/var/buildbot/scripts/load_venv.py", worker, builder,
            "-r", requirements
        ],
        haltOnFailure=True,
        timeout=600)

def uwsgi_step(api: str, uwsgi_dir: str):
    return steps.ShellCommand(
        command=[
            PYTHON_EX, "/var/buildbot/scripts/uwsgi_loader.py", api, uwsgi_dir])

def service_step(service: str, **kwargs):
    cmd = [PYTHON_EX, "/var/buildbot/service.py", service]
    if 'pidfile' in kwargs:
        cmd.extend(['--pidfile', kwargs['pidfile']])
    return steps.ShellCommand(command=cmd)
