#!/usr/bin/python3
import os
from fabric.api import *

env.hosts = ['100.25.137.186', '54.196.50.77']


def do_clean(number=0):
    """
        deletes out-of-date archives
        Args:
            number: the number of archives to keep
    """
    number = 1 if int(number) == 0 else int(number)

    arc = sorted(os.listdir("versions"))
    [arc.pop() for i in range(number)]
    with lcd("versions"):
        [local("rm ./{}".format(a)) for a in arc]

    with cd("/data/web_static/releases"):
        arc = run("ls -tr").split()
        arc = [a for a in arc if "web_static_" in a]
        [arc.pop() for i in range(number)]
        [run("rm -rf ./{}".format(a)) for a in arc]
