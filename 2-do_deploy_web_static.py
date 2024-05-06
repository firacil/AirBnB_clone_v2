#!/usr/bin/python3
"""
    module to send archive file & uncompress it
    in my remote server
"""
from fabric.api import *
from datetime import datetime
from os import path


env.hosts = ['100.25.137.186', '54.196.50.77']
env.user = 'ubuntu'
env.key_filename = '~/.ssh/id_rsa'


def do_deploy(archive_path):
    """deploy archive file to web server"""

    try:
            if not (path.exists(archive_path)):
                return False

            # upload arc
            put(archive_path, '/tmp/')

            # target directory
            ts = archive_path[-18:-4]
            run('sudo mkdir -p /data/web_static/releases/\
web_static_{}/'.format(ts))

            # uncompress the file
            run('sudo tar -xzf /tmp/web_static_{}.tgz -C \
/data/web_static/releases/web_static_{}/'.format(ts, ts))

            # remove arch file
            run('sudo rm /tmp/web_static_{}.tgz'.format(ts))

            # move content into host webstatic
            run('sudo mv /data/web_static/releases/web_static_{}/web_static/* \
/data/web_static/releases/web_static_{}/'.format(ts, ts))

            # remove unusable dir
            run('sudo rm -rf /data/web_static/releases/\
web_static_{}/web_static'.format(ts))

            # delete existing link(-s)
            run('sudo rm -rf /data/web_static/current')

            # re-establish symbolic link
            run('sudo ln -s /data/web_static/releases/\
web_static_{}/ /data/web_static/current'.format(ts))
    except:
            return False

    # return True if success
    return True
