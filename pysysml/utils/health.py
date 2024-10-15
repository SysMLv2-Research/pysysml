import os.path
import pathlib

from .hash import file_sha256


class FileHashNotMatchError(Exception):
    pass


def file_health_check(file, allow_no_hash: bool = False):
    hash_file = f'{file}.sha256'
    if not os.path.exists(file):
        raise FileNotFoundError(f'Resource file {file!r} not found.')
    if not os.path.isfile(file):
        raise IsADirectoryError(f'Resource file {file!r} not a file.')

    if os.path.exists(hash_file):
        expected_hash = pathlib.Path(hash_file).read_text().strip()
        actual_hash = file_sha256(file)
        if actual_hash != expected_hash:
            raise FileHashNotMatchError(f'File hash for {file!r} not match, '
                                        f'{expected_hash!r} expected but {actual_hash!r} found.')
    else:
        if not allow_no_hash:
            raise FileNotFoundError(f'Hash file {hash_file!r} not found.')
