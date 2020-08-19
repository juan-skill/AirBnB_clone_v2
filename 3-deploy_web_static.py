#!/usr/bin/python3
""" generates a .tgz archive from the contents of the web_static folder
"""

from datetime import datetime
from pathlib import Path

from fabric.api import local, env, run, put, sudo


# env.hosts = ["localhost"]
# env.user = "root"
env.hosts = ["34.75.120.130", "35.185.98.157"]
env.user = "ubuntu"


def do_pack():
    """creates an archive .tgz"""

    time = datetime.now()

    """name of .tgz archive tar  and date folder web_static
       form: name archive_date.tgz """
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
    print("first command local  -->   mkdir -p versions")
    print("second command local -->  tar -cvzf versions/{}.tgz web_static"
          .format(filename))

    "Exist archive with success"
    file_path = Path("versions/{}.tgz".format(filename))

    if file_path.is_file():
        print("return: path a .tgz archive  --> versions/{}.tgz"
              .format(filename))
        return "versions/{}.tgz".format(filename)

    else:
        return None


def do_deploy(archive_path):
    """deploy: distributes an archive to your web servers"""

    arc_path = Path(archive_path)

    if not arc_path.is_file():
        return False

    try:
        name = archive_path[9:-4]
        tar_path = "/tmp/{:s}.tgz".format(name)
        host_path = "/data/web_static/releases/{:s}/".format(name)

        put(archive_path, tar_path)

        sudo("mkdir -p {:s}".format(host_path))
        sudo("tar -xzf {} -C {:s}".format(tar_path, host_path))
        sudo("rm {}".format(tar_path))
        sudo("mv /data/web_static/releases/{:s}/web_static/* {:s}"
             .format(name, host_path))

        sudo("rm -rf {:s}web_static".format(host_path))
        sudo("rm -rf /data/web_static/current")

        sudo("ln -s {:s} /data/web_static/current".format(host_path))

        print("New version deployed!")
        return True

    except:

        return False


def deploy():
    """deployment"""
    try:
        return do_deploy(do_pack())
    except Exception as e:
        print(str(e))

    finally:
        return False
