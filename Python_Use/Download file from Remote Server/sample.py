#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Download file resources from remote server to local through paramiko
author: gxcuizy
time: 2018-08-01
"""

import  paramiko
import  you
from stat import S_ISDIR as isdir


def down_from_remote(sftp_obj, remote_dir_name, local_dir_name):
    """Remote download file"""
    remote_file = sftp_obj.stat(remote_dir_name)
    if isdir(remote_file.st_mode):
        # Folder, cannot be downloaded directly, need to continue to loop
        check_local_dir(local_dir_name)
        print ( 'Start downloading folder:'  +  remote_dir_name )
        for remote_file_name in sftp.listdir(remote_dir_name):
            sub_remote = os.path.join(remote_dir_name, remote_file_name)
            sub_remote = sub_remote.replace('\\', '/')
            sub_local = os.path.join(local_dir_name, remote_file_name)
            sub_local = sub_local.replace('\\', '/')
            down_from_remote(sftp_obj, sub_remote, sub_local)
    else:
        # File, download directly
        print ( 'Start downloading files:'  +  remote_dir_name )
        sftp.get(remote_dir_name, local_dir_name)


def check_local_dir(local_dir_name):
    """Does the local folder exist, create it if it does not exist"""
    if not os.path.exists(local_dir_name):
        os.makedirs(local_dir_name)


if __name__ == "__main__":
    """Program main entrance"""
    # Server connection information
    host_name = '172.17.2.18'
    user_name = 'dev'
    password = 'dev@zdlh'
    port = 22
    # Remote file path (requires absolute path)
    remote_dir = '/data/nfs/zdlh/pdf/2018/07/31'
    # Local file storage path (absolute path or relative path can be used)
    local_dir = 'file_download/'

    # Connect to remote server
    t = paramiko.Transport((host_name, port))
    t.connect(username=user_name, password=password)
    sftp = paramiko.SFTPClient.from_transport(t)

    # The remote file starts to download
    down_from_remote(sftp, remote_dir, local_dir)

    # Close connection
    t.close()
