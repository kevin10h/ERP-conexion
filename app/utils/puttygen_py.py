"""
Mini-PuTTYgen: genera clave RSA y la convierte a .ppk.
Requiere los binarios ssh-keygen y puttygen (paquete putty-tools).
"""
import argparse
import getpass
import subprocess
import tempfile
import pathlib

def _run(cmd: list[str]):
    subprocess.run(cmd, check=True, text=True)

def gen_ppk(path: str, bits: int = 4096, passphrase: str = ""):
    with tempfile.TemporaryDirectory() as td:
        td = pathlib.Path(td)
        pem = td / "id_rsa"
        # 1) Generar clave OpenSSH (PEM)
        _run([
            "ssh-keygen", "-q", "-t", "rsa", "-b", str(bits),
            "-m", "PEM", "-N", passphrase, "-f", str(pem)
        ])
        # 2) Convertir a PPK con puttygen
        putty_cmd = ["puttygen", str(pem), "-O", "private", "-o", path]
        if passphrase:
            putty_cmd += ["-P"]          # mantiene la misma passphrase
        _run(putty_cmd)
    print(f"PPK saved to {path}")

if __name__ == "__main__":
    ap = argparse.ArgumentParser(description="Generate .ppk key")
    ap.add_argument("outfile")
    ap.add_argument("--bits", type=int, default=4096)
    ap.add_argument("--passphrase", default=None)
    args = ap.parse_args()
    if args.passphrase is None:
        args.passphrase = getpass.getpass("Passphrase (enter for none): ")
    gen_ppk(args.outfile, args.bits, args.passphrase or "")
