#!/usr/bin/python3
from fabric.api import env, local, run


env.hosts = ['54.157.145.62', '54.157.138.182']
env.user = "ubuntu"


def do_clean(number=0):
    """CLEANS"""

    number = int(number)

    if number == 0:
        number = 2
    else:
        number += 1

    local('cd versions ; ls -t | tail -n +{} | xargs rm -rf'.format(number))
    path = '/data/web_static/releases'
    run('cd {} ; ls -t | tail -n +{} | xargs rm -rf'.format(path, number))
