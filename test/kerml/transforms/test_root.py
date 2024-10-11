import pytest

from pysysml.kerml.models import Comment, Identification, QualifiedName, Documentation, Dependency, \
    PrefixMetadataAnnotation, RelationshipBody, FeatureChain
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
    def test_documentation(self, text, expected):
        parser = _parser_for_rule('documentation')
        if isinstance(expected, type) and issubclass(expected, Exception):
            with pytest.raises(expected):
                _ = parser(text)
        else:
            v, rules = parser(text)
            assert v == expected
            assert 'documentation' in rules

    @pytest.mark.parametrize(['text', 'expected'], [
        ("dependency Use from 'Application Layer' to 'Service Layer';",
         Dependency(annotations=[], identification=Identification(short_name=None, name='Use'),
                    from_list=[QualifiedName(names=['Application Layer'])],
                    to_list=[QualifiedName(names=['Service Layer'])], relationship_body=RelationshipBody(elements=[]))),
        ("#command # xx::xx.xx dependency Use from 'Application Layer' to 'Service "
         "Layer';",
         Dependency(annotations=[PrefixMetadataAnnotation(feature=QualifiedName(names=['command'])),
                                 PrefixMetadataAnnotation(feature=FeatureChain(
                                     items=[QualifiedName(names=['xx', 'xx']), QualifiedName(names=['xx'])]))],
                    identification=Identification(short_name=None, name='Use'),
                    from_list=[QualifiedName(names=['Application Layer'])],
                    to_list=[QualifiedName(names=['Service Layer'])], relationship_body=RelationshipBody(elements=[]))),
        ("dependency 'Service Layer' to 'Data Layer', 'External Interface Layer';",
         Dependency(annotations=[], identification=None, from_list=[QualifiedName(names=['Service Layer'])],
                    to_list=[QualifiedName(names=['Data Layer']), QualifiedName(names=['External Interface Layer'])],
                    relationship_body=RelationshipBody(elements=[]))),
        ("dependency 'Service Layer'\n"
         "    to 'Data Layer', 'External Interface Layer' {\n"
         "    /* 'Service Layer' is the client of this dependency,\n"
         '    * not its name. */\n'
         '}',
         Dependency(annotations=[], identification=None, from_list=[QualifiedName(names=['Service Layer'])],
                    to_list=[QualifiedName(names=['Data Layer']), QualifiedName(names=['External Interface Layer'])],
                    relationship_body=RelationshipBody(elements=[
                        Comment(identification=None, about_list=None, locale=None,
                                comment="/* 'Service Layer' is the client of this dependency,\n    * not its name. */")]))),
    ])
    def test_dependency(self, text, expected):
        parser = _parser_for_rule('dependency')
        if isinstance(expected, type) and issubclass(expected, Exception):
            with pytest.raises(expected):
                _ = parser(text)
        else:
            v, rules = parser(text)
            assert v == expected
            assert 'dependency' in rules
