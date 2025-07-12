from pathlib import Path
from app.utils.puttygen_py import gen_ppk

KEY_PATH = Path("keys/pivot_user.ppk")

def main():
    if KEY_PATH.exists():
        print(f"🔑 Clave ya presente → {KEY_PATH}")
    else:
        print("[1/1] Generando pivot_user.ppk…")
        KEY_PATH.parent.mkdir(exist_ok=True)
        gen_ppk(str(KEY_PATH))

if __name__ == "__main__":
    main()
