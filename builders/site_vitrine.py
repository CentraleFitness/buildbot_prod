from buildbot.plugins import util, steps


site_vitrine_builder = util.BuilderConfig(
    name='SiteVitrine',
    workername='site_vitrine',
    factory=util.BuildFactory([
        steps.Git(repourl='git@github.com:CentraleFitness/site_vitrine.git',
                mode='incremental'),
        steps.ShellCommand(command=["yarn"]),
        steps.ShellCommand(command=["yarn", "build"]),
        steps.ShellCommand(command=["forever", "stop", "bin/www"]),
        steps.ShellCommand(command=["forever", "start", "bin/www"]),
    ])
)

site_vitrine_builder_alt = util.BuilderConfig(
    name='SiteVitrine_npm',
    workername='site_vitrine',
    factory=util.BuildFactory([
        steps.Git(repourl='git@github.com:CentraleFitness/site_vitrine.git',
                mode='incremental'),
        steps.ShellCommand(command=["npm", "install"]),
        steps.ShellCommand(command=["npm", "run", "build"]),
        steps.ShellCommand(command=["forever", "stop", "bin/www"]),
        steps.ShellCommand(command=["forever", "start", "bin/www"]),
    ])
)
