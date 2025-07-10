import paramiko, os, io, logging
from app.core.config import get_settings

log = logging.getLogger("bank_client")
cfg = get_settings()

def _connect():
    private = paramiko.RSAKey(filename=cfg.BANK_KEY)
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(cfg.BANK_HOST, port=cfg.BANK_PORT, username=cfg.BANK_USER, pkey=private)
    return ssh, ssh.open_sftp()

def send_payment(file_bytes: bytes, remote_name: str):
    ssh, sftp = _connect()
    try:
        sftp.putfo(io.BytesIO(file_bytes), remote_name)
        log.info("Sent %s to bank server", remote_name)
    finally:
        sftp.close()
        ssh.close()
