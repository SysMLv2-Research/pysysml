import logging

from pysysml.utils import file_sha256
from .resource import list_resources

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)

    all_files = [file for file in list_resources() if not file.endswith('.sha256')]
    for file in all_files:
        sha256_file = f'{file}.sha256'
        logging.info(f'Getting hash for {file!r} ...')
        with open(sha256_file, 'w') as f:
            print(file_sha256(file), file=f)
