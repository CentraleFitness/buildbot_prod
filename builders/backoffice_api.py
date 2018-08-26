from buildbot.plugins import util, steps

from helpers.steps import venv_step, uwsgi_step

WORKDIR = "emailproj/"
BUILDDIR = "/var/buildbot/workers/backoffice_api/BackofficeApi/build/"
PYTHON_EX = "../../venv/bin/python3"


backoffice_api_factory = util.BuildFactory([
    steps.Git(repourl='git@github.com:CentraleFitness/backoffice-server.git',
              mode='incremental'),
    venv_step('backoffice_api', 'BackofficeApi'),
    steps.ShellCommand(
        command=[PYTHON_EX, "manage.py", "migrate"], workdir=WORKDIR),
    uwsgi_step('backoffice_api', BUILDDIR)
])

backoffice_api_builder = util.BuilderConfig(
    name='BackofficeApi',
    workername='backoffice_api',
    factory=backoffice_api_factory
)
