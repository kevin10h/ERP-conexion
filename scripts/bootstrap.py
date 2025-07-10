"""Utility to bootstrap demo environment: generate model and key"""
import pathlib
from app.utils.puttygen_py import gen_ppk
from app.models.ml import _train_dummy, MODEL_PATH

def main():
    print('[1/2] Generating ML model...')
    _train_dummy()
    print(f'  -> saved at {MODEL_PATH}')
    print('[2/2] Generating pivot_user.ppk...')
    key_path = pathlib.Path('pivot_user.ppk')
    gen_ppk(str(key_path))
    print('Done.')

if __name__ == '__main__':
    main()
