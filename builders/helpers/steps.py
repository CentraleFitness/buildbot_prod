from buildbot.plugins import steps

def venv_step(worker: str, builder: str, requirements: str='requirements.txt'):
    return steps.ShellCommand(
        command=[
            "python3", "/var/buildbot/scripts/load_venv.py", worker, builder,
            "-r", requirements
        ],
        haltOnFailure=True,
        timeout=600)

def uwsgi_step(api: str, uwsgi_dir: str):
    return steps.ShellCommand(
        command=[
            "python3", "/var/buildbot/scripts/uwsgi_loader.py", api, uwsgi_dir])
