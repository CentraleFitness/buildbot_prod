from buildbot.plugins import util, steps

from .helpers.steps import venv_step, uwsgi_step

UWSGI_DIR = "/var/buildbot/workers/backoffice_api/BackofficeApi/build/emailproj/uwsgi"
PYTHON_EX = "/var/buildbot/workers/backoffice_api/venv/bin/python3"


backoffice_api_factory = util.BuildFactory([
    steps.Git(repourl='git@github.com:CentraleFitness/backoffice-server.git',
              mode='incremental'),
    venv_step('backoffice_api', 'BackofficeApi'),
    steps.ShellCommand(
        command=[PYTHON_EX, "manage.py", "migrate"]),
    uwsgi_step('backoffice_api', UWSGI_DIR)
])

backoffice_api_builder = util.BuilderConfig(
    name='BackofficeApi',
    workername='backoffice_api',
    factory=backoffice_api_factory
)
