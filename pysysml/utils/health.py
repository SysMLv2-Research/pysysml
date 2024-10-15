"""
This module provides functionality for file health checks, including file existence verification and hash validation.

The module includes custom exceptions for hash-related errors and a main function for performing file health checks.
It utilizes the `file_sha256` function from the `.hash` module to calculate file hashes.
"""

import os.path
import pathlib

from .hash import file_sha256


class FileHashNotMatchError(Exception):
    """
    Exception raised when the calculated file hash does not match the expected hash.

    This exception is typically raised in the `file_health_check` function when the SHA256 hash
    of the file does not match the hash stored in the corresponding .sha256 file.
    """
    pass


class HashFileNotFoundError(Exception):
    """
    Exception raised when the hash file for a given file is not found.

    This exception is typically raised in the `file_health_check` function when the .sha256 file
    for the checked file does not exist and `allow_no_hash` is set to False.
    """
    pass


def file_health_check(file, allow_no_hash: bool = False):
    """
    Perform a health check on the specified file.

    This function checks for the existence of the file, verifies that it's not a directory,
    and validates its SHA256 hash against an expected hash stored in a .sha256 file.

    :param file: The path to the file to be checked.
    :type file: str
    :param allow_no_hash: If True, the function will not raise an exception when the .sha256 file is missing.
                          Default is False.
    :type allow_no_hash: bool

    :raises FileNotFoundError: If the specified file does not exist.
    :raises IsADirectoryError: If the specified file path points to a directory instead of a file.
    :raises FileHashNotMatchError: If the calculated hash of the file does not match the expected hash.
    :raises HashFileNotFoundError: If the .sha256 file is not found and allow_no_hash is False.

    :return: None

    Usage:
        file_health_check('path/to/your/file.txt')
        file_health_check('path/to/your/file.txt', allow_no_hash=True)
    """
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
            raise HashFileNotFoundError(f'Hash file {hash_file!r} not found.')
