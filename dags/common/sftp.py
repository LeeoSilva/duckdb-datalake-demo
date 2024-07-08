import glob

import paramiko
from common.settings import get_settings

# def get_transport() -> paramiko.Transport:
#     url = get_settings().SFTP_URL
#     port = get_settings().SFTP_PORT

#     socket = (url, port)
#     return paramiko.Transport(socket)


# def connect_to_sftp():
# transport = get_transport()
# private_key_path = get_settings().SFTP_PKEY
# username = get_settings().SFTP_USERNAME
# password = get_settings().SFTP_PASSWORD

# pkey = paramiko.RSAKey.from_private_key_file(private_key_path)
# transport.connect(username=username, password=password, pkey=pkey)
# sftp = paramiko.SFTPClient.from_transport(transport)
# return sftp


def connect_to_sftp():
    return None


def list_files(sftp):
    files = glob.glob("./sftp/*.csv")
    return files


def download_file(sftp, filename, target_path):
    


# def list_files(sftp):
#     files = sftp.listdir("/")
#     sftp.close()
#     return files


# def download_file(filename: str):
#     sftp = connect_to_sftp()
#     sftp.get(filename, filename)
#     sftp.close()
#     return filename
