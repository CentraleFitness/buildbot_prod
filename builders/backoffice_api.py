from buildbot.plugins import util, steps

from .helpers.steps import venv_step, uwsgi_step

WORKDIR = "emailproj/"
UWSGI_DIR = "/var/buildbot/workers/backoffice_api/BackofficeApi/build/emailproj/uwsgi"
PYTHON_EX = "../../venv/bin/python3"


backoffice_api_factory = util.BuildFactory([
    steps.Git(repourl='https://github.com/CentraleFitness/backoffice-server.git',
              mode='incremental', origin='origin/master'),
    venv_step('backoffice_api', 'BackofficeApi'),
    steps.ShellCommand(
        command=[PYTHON_EX, "manage.py", "migrate"], workdir=WORKDIR),
    uwsgi_step('backoffice_api', UWSGI_DIR)
])

backoffice_api_builder = util.BuilderConfig(
    name='BackofficeApi',
    workername='backoffice_api',
    factory=backoffice_api_factory
)
