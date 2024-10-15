"""
This module provides functions for calculating SHA256 hashes of files.

It includes utilities for handling both binary and text files, with an option
to ignore line wrapping in text files. The module uses the hashlib library for
SHA256 hash generation and the hbutils.system module for file type detection.
"""

import hashlib

from hbutils.system import is_binary_file


def _binary_file_sha256(file: str, chunk_size: int = 1 << 20) -> str:
    """
    Calculate the SHA256 hash of a binary file.

    This function reads the file in chunks to efficiently handle large files.

    :param file: Path to the binary file.
    :type file: str
    :param chunk_size: Size of each chunk to read, defaults to 1MB (1 << 20 bytes).
    :type chunk_size: int

    :return: Hexadecimal representation of the SHA256 hash.
    :rtype: str
    """
    file_sha = hashlib.sha256()
    with open(file, 'rb') as f:
        while True:
            data = f.read(chunk_size)
            if not data:
                break
            file_sha.update(data)
    return file_sha.hexdigest()


def _text_file_sha256(file: str) -> str:
    """
    Calculate the SHA256 hash of a text file, ignoring line wrapping.

    This function reads the file line by line, adding a newline character
    after each line to standardize line endings.

    :param file: Path to the text file.
    :type file: str

    :return: Hexadecimal representation of the SHA256 hash.
    :rtype: str
    """
    file_sha = hashlib.sha256()
    with open(file, 'rb') as f:
        for line in f.read().splitlines(keepends=False):
            file_sha.update(line + b'\n')
    return file_sha.hexdigest()


def file_sha256(file: str, ignore_linewrap: bool = True) -> str:
    """
    Calculate the SHA256 hash of a file, with an option to ignore line wrapping for text files.

    This function determines whether the file is binary or text, and uses the appropriate
    method to calculate the hash. For text files, it can optionally ignore line wrapping.

    :param file: Path to the file.
    :type file: str
    :param ignore_linewrap: Whether to ignore line wrapping for text files, defaults to True.
    :type ignore_linewrap: bool

    :return: Hexadecimal representation of the SHA256 hash.
    :rtype: str
    """
    if not is_binary_file(file) and ignore_linewrap:
        return _text_file_sha256(file)
    else:
        return _binary_file_sha256(file)
