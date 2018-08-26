from buildbot.plugins import util, steps

WORKDIR = "emailproj/"
PYTHON_EX = "../../venv/bin/python3"
SCRIPT_EX = "/bin/bash"

backoffice_api_factory = util.BuildFactory([
    steps.Git(repourl='git@github.com:CentraleFitness/backoffice-server.git',
              mode='incremental'),
    steps.ShellCommand(command=[PYTHON_EX, "emailproj/manage.py", "migrate"]),
    steps.ShellCommand(command=[SCRIPT_EX, "emailproj/uwsgi/bb_uwsgi.sh", "start"])
])

backoffice_api_builder = util.BuilderConfig(
    name='BackofficeApi',
    workername='backoffice_api',
    factory=backoffice_api_factory
)
