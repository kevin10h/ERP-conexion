import io
import logging
import paramiko
from app.core.config import get_settings

log = logging.getLogger("bank_client")
cfg = get_settings()


def _connect():
    """Abre una conexión SSH + SFTP con el servidor del banco."""
    private = paramiko.RSAKey(filename=cfg.BANK_KEY)
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(
        hostname=cfg.BANK_HOST,
        port=cfg.BANK_PORT,
        username=cfg.BANK_USER,
        pkey=private,
    )
    return ssh, ssh.open_sftp()


def send_payment(file_bytes: bytes, filename: str) -> None:
    """
    Envía el archivo recibido al directorio `upload/` del usuario bancario.

    Parameters
    ----------
    file_bytes : bytes
        Contenido binario del archivo a transferir.
    filename : str
        Nombre con el que se guardará en el servidor remoto.
    """
    ssh, sftp = _connect()
    try:
        remote_path = f"upload/{filename.lstrip('/')}"  # ⇢ /home/pivot_user/upload/…
        sftp.putfo(io.BytesIO(file_bytes), remote_path)
        log.info("Sent %s to bank server", remote_path)
    finally:
        sftp.close()
        ssh.close()
