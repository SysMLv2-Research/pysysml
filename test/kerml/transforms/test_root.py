import pytest

from pysysml.kerml.models import Comment, Identification, QualifiedName, Documentation, Dependency, \
    PrefixMetadataAnnotation, FeatureChain, TextualRepresentation
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
        ),
        ('comment Comment1 about A, B\n/* This is the comment body text. */',
         Comment(identification=Identification(short_name=None, name='Comment1'),
                 about_list=[QualifiedName(names=['A']), QualifiedName(names=['B'])], locale=None,
                 comment='/* This is the comment body text. */')),
        ('comment C /* This is a comment about N. */',
         Comment(identification=Identification(short_name=None, name='C'), about_list=None, locale=None,
                 comment='/* This is a comment about N. */')),
        ('/* This is also a comment about N. */',
         Comment(identification=None, about_list=None, locale=None, comment='/* This is also a comment about N. */')),
        ('comment C_US_English locale "en_US"\n/* This is US English comment text */',
         Comment(identification=Identification(short_name=None, name='C_US_English'), about_list=None, locale='en_US',
                 comment='/* This is US English comment text */')),
        ('/*\n'
         '* This is an example of multiline\n'
         '* comment text with typical formatting\n'
         '* for readable display in a text editor.\n'
         '*/',
         Comment(identification=None, about_list=None, locale=None,
                 comment='/*\n* This is an example of multiline\n* comment text with typical formatting\n'
                         '* for readable display in a text editor.\n*/')),
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
        ('doc X_Comment\n/* This is a documentation comment about X. */',
         Documentation(identification=Identification(short_name=None, name='X_Comment'), locale=None,
                       comment='/* This is a documentation comment about X. */')),
        ('doc /* This is more documentation about X. */',
         Documentation(identification=Identification(short_name=None, name=None), locale=None,
                       comment='/* This is more documentation about X. */')),
        ('doc P_Comment /* This is a documentation comment about P. */',
         Documentation(identification=Identification(short_name=None, name='P_Comment'), locale=None,
                       comment='/* This is a documentation comment about P. */')),
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
                    to_list=[QualifiedName(names=['Service Layer'])], body=[])),
        ("#command # xx::xx.xx dependency Use from 'Application Layer' to 'Service "
         "Layer';",
         Dependency(annotations=[PrefixMetadataAnnotation(feature=QualifiedName(names=['command'])),
                                 PrefixMetadataAnnotation(feature=FeatureChain(
                                     items=[QualifiedName(names=['xx', 'xx']), QualifiedName(names=['xx'])]))],
                    identification=Identification(short_name=None, name='Use'),
                    from_list=[QualifiedName(names=['Application Layer'])],
                    to_list=[QualifiedName(names=['Service Layer'])], body=[])),
        ("dependency 'Service Layer' to 'Data Layer', 'External Interface Layer';",
         Dependency(annotations=[], identification=None, from_list=[QualifiedName(names=['Service Layer'])],
                    to_list=[QualifiedName(names=['Data Layer']), QualifiedName(names=['External Interface Layer'])],
                    body=[])),
        ("dependency 'Service Layer'\n"
         "    to 'Data Layer', 'External Interface Layer' {\n"
         "    /* 'Service Layer' is the client of this dependency,\n"
         '    * not its name. */\n'
         '}',
         Dependency(annotations=[], identification=None, from_list=[QualifiedName(names=['Service Layer'])],
                    to_list=[QualifiedName(names=['Data Layer']), QualifiedName(names=['External Interface Layer'])],
                    body=[
                        Comment(identification=None, about_list=None, locale=None,
                                comment="/* 'Service Layer' is the client of this dependency,\n    * not its name. */")])),
    ])
    @pytest.mark.focus
    def test_dependency(self, text, expected):
        parser = _parser_for_rule('dependency')
        if isinstance(expected, type) and issubclass(expected, Exception):
            with pytest.raises(expected):
                _ = parser(text)
        else:
            v, rules = parser(text)
            assert v == expected
            assert 'dependency' in rules

    @pytest.mark.parametrize(['text', 'expected'], [
        ('rep inOCL language "ocl"\n/* self.x > 0.0 */',
         TextualRepresentation(identification=Identification(short_name=None, name='inOCL'), language='"ocl"',
                               comment='/* self.x > 0.0 */')),
        ('language "alf"\n/* c.x = newX;\n* WriteLine("Set new x");\n*/',
         TextualRepresentation(identification=None, language='"alf"',
                               comment='/* c.x = newX;\n* WriteLine("Set new x");\n*/')),
    ])
    @pytest.mark.focus
    def test_textual_representation(self, text, expected):
        parser = _parser_for_rule('textual_representation')
        if isinstance(expected, type) and issubclass(expected, Exception):
            with pytest.raises(expected):
                _ = parser(text)
        else:
            v, rules = parser(text)
            assert v == expected
            assert 'textual_representation' in rules
