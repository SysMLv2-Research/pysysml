import pytest

from pysysml.kerml.models import Comment, Identification, QualifiedName, Documentation
from .base import _parser_for_rule


@pytest.mark.unittest
class TestKerMLTransformsRoot:
    @pytest.mark.parametrize(['text', 'expected'], [
        (
                """
    comment about x, y locale "zh" /* sgd */
                """,
                Comment(identification=Identification(short_name=None, name=None),
                        about_list=[QualifiedName(names=['x']), QualifiedName(names=['y'])], locale='zh',
                        comment='/* sgd */')
        ),
        (
                """
                comment locale "zh" /* sgd */
                """,
                Comment(identification=Identification(short_name=None, name=None), about_list=None, locale='zh',
                        comment='/* sgd */'),
        ),
        (
                """
                comment about x::y /* sgd */
                """,
                Comment(identification=Identification(short_name=None, name=None),
                        about_list=[QualifiedName(names=['x', 'y'])], locale=None, comment='/* sgd */')
        ),
        (
                """
                /* sgd */
                """,
                Comment(identification=None, about_list=None, locale=None, comment='/* sgd */')
        )

    ])
    @pytest.mark.focus
    def test_comment(self, text, expected):
        parser = _parser_for_rule('comment')
        if isinstance(expected, type) and issubclass(expected, Exception):
            with pytest.raises(expected):
                _ = parser(text)
        else:
            v, rules = parser(text)
            assert v == expected
            assert 'comment' in rules

    @pytest.mark.parametrize(['text', 'expected'], [
        ('doc full_name locale "zh" /* kdfg */',
         Documentation(identification=Identification(short_name=None, name='full_name'), locale='zh',
                       comment='/* kdfg */')),
        ('doc full_name  /* kdfg */',
         Documentation(identification=Identification(short_name=None, name='full_name'), locale=None,
                       comment='/* kdfg */')),
        ('doc <fn> full_name  /* kdfg */',
         Documentation(identification=Identification(short_name='fn', name='full_name'), locale=None,
                       comment='/* kdfg */')),
        ("doc <fn> 'full \\'name'  /* kdfg */",
         Documentation(identification=Identification(short_name='fn', name="full 'name"), locale=None,
                       comment='/* kdfg */')),
        ('doc <fn>  /* kdfg */',
         Documentation(identification=Identification(short_name='fn', name=None), locale=None, comment='/* kdfg */')),
        ('doc   /* kdfg */',
         Documentation(identification=Identification(short_name=None, name=None), locale=None, comment='/* kdfg */')),
    ])
    @pytest.mark.focus
    def test_documentation(self, text, expected):
        parser = _parser_for_rule('documentation')
        if isinstance(expected, type) and issubclass(expected, Exception):
            with pytest.raises(expected):
                _ = parser(text)
        else:
            v, rules = parser(text)
            assert v == expected
            assert 'documentation' in rules
