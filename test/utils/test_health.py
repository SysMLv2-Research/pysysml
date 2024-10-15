import pytest

from pysysml.utils import FileHashNotMatchError, file_health_check, HashFileNotFoundError
from ..testings import get_testfile


@pytest.mark.unittest
class TestUtilsHealth:
    @pytest.mark.parametrize(['file', 'expected_error'], [
        (get_testfile('hashes', 'match_requirements-where.txt', 'requirements-where.txt'), None),
        (get_testfile('hashes', 'match_korean.txt', 'korean.txt'), None),
        (get_testfile('hashes', 'non_match_raw.tar.xz', 'raw.tar.xz'), FileHashNotMatchError),
        (get_testfile('hashes', 'match_empty', 'empty'), None),
        (get_testfile('hashes', 'match_raw.tar.gz', 'raw.tar.gz'), None),
        (get_testfile('hashes', 'non_match_requirements-1.txt', 'requirements-1.txt'), FileHashNotMatchError),
        (get_testfile('hashes', 'non_match_raw.tar.bz2', 'raw.tar.bz2'), FileHashNotMatchError),
        (get_testfile('hashes', 'non_match_raw.7z', 'raw.7z'), FileHashNotMatchError),
        (get_testfile('hashes', 'match_raw.tar', 'raw.tar'), None),
        (get_testfile('hashes', 'match_raw.zip', 'raw.zip'), None),
        (get_testfile('hashes', 'non_match_english.txt', 'english.txt'), FileHashNotMatchError),
        (get_testfile('hashes', 'non_match_raw.rar', 'raw.rar'), FileHashNotMatchError),
        (get_testfile('hashes', 'match_japanese.txt', 'japanese.txt'), None),
        (get_testfile('hashes', 'non_match_requirements-2.txt', 'requirements-2.txt'), FileHashNotMatchError),
        (get_testfile('hashes', 'match_russian.txt', 'russian.txt'), None),

        (get_testfile('hashes', 'non_match_english.txt', 'english.txt_not_found'), FileNotFoundError),
        (get_testfile('hashes', 'non_match_raw.rar', 'raw.rar_not_found'), FileNotFoundError),
        (get_testfile('hashes', 'match_japanese.txt', 'japanese.txt_not_found'), FileNotFoundError),
        (get_testfile('hashes', 'non_match_requirements-2.txt', 'requirements-2.txt_not_found'), FileNotFoundError),
        (get_testfile('hashes', 'match_russian.txt', 'russian.txt_not_found'), FileNotFoundError),

        (get_testfile('hashes', 'non_match_english.txt'), IsADirectoryError),
        (get_testfile('hashes', 'non_match_raw.rar'), IsADirectoryError),
        (get_testfile('hashes', 'match_japanese.txt'), IsADirectoryError),
        (get_testfile('hashes', 'non_match_requirements-2.txt'), IsADirectoryError),
        (get_testfile('hashes', 'match_russian.txt'), IsADirectoryError),

        (get_testfile('english.txt'), HashFileNotFoundError),
        (get_testfile('raw.rar'), HashFileNotFoundError),
        (get_testfile('japanese.txt'), HashFileNotFoundError),
        (get_testfile('requirements-2.txt'), HashFileNotFoundError),
        (get_testfile('russian.txt'), HashFileNotFoundError),
    ])
    def test_file_health_check_common(self, file, expected_error):
        if expected_error:
            with pytest.raises(expected_error):
                _ = file_health_check(file)
        else:
            _ = file_health_check(file)

    @pytest.mark.parametrize(['file', 'expected_error'], [
        (get_testfile('hashes', 'match_requirements-where.txt', 'requirements-where.txt'), None),
        (get_testfile('hashes', 'match_korean.txt', 'korean.txt'), None),
        (get_testfile('hashes', 'non_match_raw.tar.xz', 'raw.tar.xz'), FileHashNotMatchError),
        (get_testfile('hashes', 'match_empty', 'empty'), None),
        (get_testfile('hashes', 'match_raw.tar.gz', 'raw.tar.gz'), None),
        (get_testfile('hashes', 'non_match_requirements-1.txt', 'requirements-1.txt'), FileHashNotMatchError),
        (get_testfile('hashes', 'non_match_raw.tar.bz2', 'raw.tar.bz2'), FileHashNotMatchError),
        (get_testfile('hashes', 'non_match_raw.7z', 'raw.7z'), FileHashNotMatchError),
        (get_testfile('hashes', 'match_raw.tar', 'raw.tar'), None),
        (get_testfile('hashes', 'match_raw.zip', 'raw.zip'), None),
        (get_testfile('hashes', 'non_match_english.txt', 'english.txt'), FileHashNotMatchError),
        (get_testfile('hashes', 'non_match_raw.rar', 'raw.rar'), FileHashNotMatchError),
        (get_testfile('hashes', 'match_japanese.txt', 'japanese.txt'), None),
        (get_testfile('hashes', 'non_match_requirements-2.txt', 'requirements-2.txt'), FileHashNotMatchError),
        (get_testfile('hashes', 'match_russian.txt', 'russian.txt'), None),

        (get_testfile('hashes', 'non_match_english.txt', 'english.txt_not_found'), FileNotFoundError),
        (get_testfile('hashes', 'non_match_raw.rar', 'raw.rar_not_found'), FileNotFoundError),
        (get_testfile('hashes', 'match_japanese.txt', 'japanese.txt_not_found'), FileNotFoundError),
        (get_testfile('hashes', 'non_match_requirements-2.txt', 'requirements-2.txt_not_found'), FileNotFoundError),
        (get_testfile('hashes', 'match_russian.txt', 'russian.txt_not_found'), FileNotFoundError),

        (get_testfile('hashes', 'non_match_english.txt'), IsADirectoryError),
        (get_testfile('hashes', 'non_match_raw.rar'), IsADirectoryError),
        (get_testfile('hashes', 'match_japanese.txt'), IsADirectoryError),
        (get_testfile('hashes', 'non_match_requirements-2.txt'), IsADirectoryError),
        (get_testfile('hashes', 'match_russian.txt'), IsADirectoryError),

        (get_testfile('english.txt'), None),
        (get_testfile('raw.rar'), None),
        (get_testfile('japanese.txt'), None),
        (get_testfile('requirements-2.txt'), None),
        (get_testfile('russian.txt'), None),
    ])
    def test_file_health_check_common_allow_no_hash(self, file, expected_error):
        if expected_error:
            with pytest.raises(expected_error):
                _ = file_health_check(file, allow_no_hash=True)
        else:
            _ = file_health_check(file, allow_no_hash=True)
