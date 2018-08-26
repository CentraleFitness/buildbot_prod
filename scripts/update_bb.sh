#!/bin/bash

cd /var/buildbot/src/buildbot_prod/ && git pull && cd -
/var/buildbot/venv/bin/buildbot restart /var/buildbot/master/
