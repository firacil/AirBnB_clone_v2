#!/usr/bin/python3
"""
    script that generates a .tgz archive
    from the contents of the web_static
"""
from fabric.api import local
from time import strftime
from datetime import date

def do_pack():
    """function that generate arvhive from web_static"""

    fn = strftime("%Y%m%d%H%M%S")
    try:
        local("mkdir -p versions")
        local("tar -czvf versions/web_static_{}.tgz web_static/"
              .format(fn))

        return "Versions/web_static_{}.tgz".format(fn)

    except Exception:
        return None
