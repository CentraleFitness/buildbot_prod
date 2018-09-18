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
        venv_step('email_api', 'EmailApi'),
        steps.ShellCommand(
            command=[
                "mv", "emailproj/config/buildbot.py",
                "emailproj/config/config.py"]),
        steps.ShellCommand(
            command=[PYTHON_EX, "emailproj/manage.py", "migrate"]),
        service_step('email_api', pidfile="/var/run/email_api.pid")
    ])
)
