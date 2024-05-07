#!/usr/bin/python3
"""creates and distributes an archive to your web servers"""
from fabric.api import *
from time import strftime
from datetime import datetime
from os import path


env.hosts = ['100.25.137.186', '54.196.50.77']
env.user = 'ubuntu'
env.key_filename = '~/.ssh/id_rsa'


def do_pack():
    """ script to fully deploy file to webserver"""
    fd = datetime.utcnow()
    file = "versions/web_static_{}{}{}{}{}{}.tgz".format(fd.year,
                                                         fd.month,
                                                         fd.day,
                                                         fd.hour,
                                                         fd.minute,
                                                         fd.second)

    if path.isdir("versions") is False:
        if local("mkdir -p versions").failed is True:
            return None
    print("Packing web_static to {}".format(file))
    if local("tar -cvzf {} web_static".format(file)).failed is True:
        return None
    print("web_static packed: {} -> {}Bytes".format(file, path.getsize(file)))
    return file


def do_deploy(archive_path):
    """distrubetes archive to web server"""
    if path.isfile(archive_path) is False:
        return False
    file = archive_path.split("/")[-1]
    name = file.split(".")[0]

    if put(archive_path, "/tmp/{}".format(file)).failed is True:
        return False
    if run("rm -rf /data/web_static/releases/{}/".
           format(name)).failed is True:
        return False
    if run("mkdir -p /data/web_static/releases/{}/".
           format(name)).failed is True:
        return False
    if run("tar -xzf /tmp/{} -C /data/web_static/releases/{}/".
           format(file, name)).failed is True:
        return False
    if run("rm /tmp/{}".format(file)).failed is True:
        return False
    if run("mv /data/web_static/releases/{}/web_static/* "
           "/data/web_static/releases/{}/".format(name, name)).failed is True:
        return False
    if run("rm -rf /data/web_static/releases/{}/web_static".
           format(name)).failed is True:
        return False
    if run("rm -rf /data/web_static/current").failed is True:
        return False
    if run("ln -s /data/web_static/releases/{}/ /data/web_static/current".
           format(name)).failed is True:
        return False
    return True


def deploy():
    """create & distrubute an arch to webserver."""
    file = do_pack()
    if file is None:
        return False
    return do_deploy(file)
