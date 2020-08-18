#!/usr/bin/python3
""" generates a .tgz archive from the contents of the web_static folder
"""

from fabric.api import local

from datetime import datetime
from pathlib import Path


def do_pack():
    """creates an archive .tgz"""

    time = datetime.now()

    filename = "web_static_{}{}{}{}{}{}".format(
        time.strftime("%Y"),
        time.month,
        time.day,
        time.hour,
        time.minute,
        time.second
    )

    local("mkdir -p versions")
    local("tar -cvzf versions/{}.tgz web_static".format(filename))

    file_path = Path("versions/{}.tgz".format(filename))

    if file_path.is_file():
        return "versions/{}.tgz".format(filename)

    else:
        return None
