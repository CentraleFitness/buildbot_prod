from buildbot.plugins import util, steps

from .helpers.steps import venv_step, service_step

PYTHON_EX = "/var/buildbot/workers/email_api/venv/bin/python3"


email_api_builder = util.BuilderConfig(
    name='EmailApi',
    workername='email_api',
    factory=util.BuildFactory([
        steps.Git(
            repourl='git@github.com:CentraleFitness/email_api.git',
            mode='incremental'),
        venv_step('email_api', 'EmailApi', 'requirements.txt'),
        steps.ShellCommand(
            command=[
                "mv", "config/buildbot.py",
                "config/config.py"]),
        steps.ShellCommand(
            command=[PYTHON_EX, "manage.py", "migrate"]),
        steps.ShellCommand(
            command=[PYTHON_EX, "manage.py", "collectstatic"]),
        service_step('email_api', pidfile="/var/run/email_api.pid")
    ])
)
