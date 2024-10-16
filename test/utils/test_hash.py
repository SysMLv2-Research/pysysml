import pytest

from pysysml.utils import file_sha256
from ..testings import get_testfile


@pytest.mark.unittest
class TestUtilsHash:
    @pytest.mark.parametrize(['file', 'sha256_hash'], [
        (get_testfile('requirements-where.txt'), '37e7e0279f187d929f971389fde33c741fed792bba9270bcc5ab57af5025107b'),
        (get_testfile('korean.txt'), '27dfb496555177ff9870bcd0d3d03ebd4d614f5546a8e6f9a60fcf8019d773ab'),
        (get_testfile('raw.tar.xz'), 'b96da203a067fb1d96e888c90f5eef94a4a2e24a01dfc9ae4490304740f807b7'),
        (get_testfile('empty'), 'e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855'),
        (get_testfile('raw.tar.gz'), 'b6f395295aa8817c086cc83fc442d6a531de326703490ba43611af1b9c775356'),
        (get_testfile('requirements-1.txt'), '9e2b58a5342733681b4a53b7c984c3619ffd1e243a4cc4334c9eb950b8856da0'),
        (get_testfile('raw.tar.bz2'), '9c954b21b622a3bca86237f74c76a1b4197f5f37a61f793739d676d233c36326'),
        (get_testfile('raw.7z'), '43782e881008a17df55388d742f4774d3b4726c11a043a726d67aeb86e10dc75'),
        (get_testfile('raw.tar'), 'be9ae98f74065d2df47f38263644941532b6615b5a60c34db8cc864b4ade147a'),
        (get_testfile('raw.zip'), 'c6e28d6aede12bb9fe4127dd7cfa8ec0e624167916bee1c09ed105bd363f3b00'),
        (get_testfile('english.txt'), '29919581dcdf442a45b8951095e9ded5064b19d7f5a00471f6c7b31602943f31'),
        (get_testfile('raw.rar'), 'ccf08326523db3ace93485038e281239f6b4d4a2d8be79ac979c25dd0c7cee2f'),
        (get_testfile('japanese.txt'), '4726a42b6891181853ce4a6b384792060798a8ad9f4dcc157d389f2bfb72474b'),
        (get_testfile('requirements-2.txt'), '91c66888159080dff9762c023c1e6635a05ed904bbdcfac5385ef5c01c027c5a'),
        (get_testfile('russian.txt'), 'd29b9985516960c306a652bdf0b318146005ee27cc4805a47d87c700053126be'),
    ])
    def test_file_sha256(self, file, sha256_hash):
        assert file_sha256(file) == sha256_hash
