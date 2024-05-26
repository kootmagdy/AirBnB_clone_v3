#!/usr/bin/python3
# Fabfile to delete out-of-date archives.

import os
from fabric.api import env, lcd, local, cd, run

env.hosts = ["54.157.145.62", "54.157.138.182"]


def do_clean(archives_to_keep=1):
    """Delete out-of-date archives.
    
    Args:
        archives_to_keep (int): The number of archives to keep.
            If 0 or 1, keeps only the most recent archive. If
            2, keeps the most and second-most recent archives, etc.
    """
    archives_to_keep = max(1, int(archives_to_keep))

    with lcd("versions"):
        local_archives = sorted(os.listdir("."))
        local_archives_to_delete = local_archives[:-archives_to_keep]
        [local(f"rm ./{archive}") for archive in local_archives_to_delete]

    with cd("/data/web_static/releases"):
        remote_archives = run("ls -tr").split()
        web_static_archives = [a for a in remote_archives if "web_static_" in a]
        remote_archives_to_delete = web_static_archives[:-archives_to_keep]
        [run(f"rm -rf ./{archive}") for archive in remote_archives_to_delete]
