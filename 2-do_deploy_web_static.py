#!/usr/bin/python3
""" distributes an archive to your web servers, using the function do_deploy"""

from fabric.api import env, run, put
from pathlib import Path

# env.hosts = ["localhost"]
env.hosts = ["34.75.120.130", "35.185.98.157"]


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

        run("mkdir -p {:s}".format(host_path))
        run("tar -xzf {} -C {:s}".format(tar_path, host_path))
        run("rm {}".format(tar_path))
        run("mv /data/web_static/releases/{:s}/web_static/* {:s}"
            .format(name, host_path))

        run("rm -rf {:s}web_static".format(host_path))
        run("rm -rf /data/web_static/current")

        run("ln -s {:s} /data/web_static/current".format(host_path))

        print("New version deployed!")
        return True

    except:

        return False
