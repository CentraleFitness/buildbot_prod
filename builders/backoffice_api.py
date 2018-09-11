from buildbot.plugins import util, steps

from .helpers.steps import venv_step, uwsgi_step, service_step

PYTHON_EX = "/var/buildbot/workers/backoffice_api/venv/bin/python3"


backoffice_api_builder = util.BuilderConfig(
    name='BackofficeApi',
    workername='backoffice_api',
    factory=util.BuildFactory([
        steps.Git(repourl='git@github.com:CentraleFitness/backoffice-server.git',
                mode='incremental'),
        venv_step('backoffice_api', 'BackofficeApi'),
        steps.ShellCommand(
            command=[PYTHON_EX, "manage.py", "migrate"]),
        service_step('backoffice_api')
    ])
)
