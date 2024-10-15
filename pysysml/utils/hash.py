import hashlib

from hbutils.system import is_binary_file


def _binary_file_sha256(file: str, chunk_size: int = 1 << 20) -> str:
    file_sha = hashlib.sha256()
    with open(file, 'rb') as f:
        while True:
            data = f.read(chunk_size)
            if not data:
                break
            file_sha.update(data)
    return file_sha.hexdigest()


def _text_file_sha256(file: str) -> str:
    file_sha = hashlib.sha256()
    with open(file, 'rb') as f:
        for line in f.read().splitlines(keepends=False):
            file_sha.update(line + b'\n')
    return file_sha.hexdigest()


def file_sha256(file: str, ignore_linewrap: bool = True) -> str:
    if not is_binary_file(file) and ignore_linewrap:
        return _text_file_sha256(file)
    else:
        return _binary_file_sha256(file)
