import pytest

from pysysml.kerml.models import Comment, Identification, QualifiedName, Documentation, Dependency, \
    PrefixMetadataAnnotation, FeatureChain, TextualRepresentation, Namespace, NonFeatureMember, Visibility, Class
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
    def test_textual_representation(self, text, expected):
        parser = _parser_for_rule('textual_representation')
        if isinstance(expected, type) and issubclass(expected, Exception):
            with pytest.raises(expected):
                _ = parser(text)
        else:
            v, rules = parser(text)
            assert v == expected
            assert 'textual_representation' in rules

    @pytest.mark.parametrize(['text', 'expected'], [
        ("namespace <'1.1'> N1; // This is an empty namespace.",
         Namespace(annotations=[], identification=Identification(short_name='1.1', name='N1'), body=[])),
        ("#command namespace <'1.1'> N1; // This is an empty namespace.",
         Namespace(annotations=[PrefixMetadataAnnotation(feature=QualifiedName(names=['command']))],
                   identification=Identification(short_name='1.1', name='N1'), body=[])),
        ('namespace N5 {\n'
         'comment Comment1 about A\n'
         '/* This is a comment about class A. */\n'
         'comment Comment2\n'
         '/* This is a comment about namespace N5. */\n'
         '/* This is also a comment about namespace N5. */\n'
         'doc N9_Doc\n'
         '/* This is documentation about namespace N5. */\n'
         '}',
         Namespace(annotations=[], identification=Identification(short_name=None, name='N5'), body=[
             NonFeatureMember(visibility=None,
                              element=Comment(identification=Identification(short_name=None, name='Comment1'),
                                              about_list=[QualifiedName(names=['A'])], locale=None,
                                              comment='/* This is a comment about class A. */')),
             NonFeatureMember(visibility=None,
                              element=Comment(identification=Identification(short_name=None, name='Comment2'),
                                              about_list=None, locale=None,
                                              comment='/* This is a comment about namespace N5. */')),
             NonFeatureMember(visibility=None, element=Comment(identification=None, about_list=None, locale=None,
                                                               comment='/* This is also a comment about namespace N5. */')),
             NonFeatureMember(visibility=None,
                              element=Documentation(identification=Identification(short_name=None, name='N9_Doc'),
                                                    locale=None,
                                                    comment='/* This is documentation about namespace N5. */'))])),
        ('namespace N5 {\n'
         '    public /* 1 2 3 */\n'
         '    protected class X;\n'
         '    private namespace Nested {\n'
         '        doc A /* 4 5 6 */\n'
         '    }\n'
         '}',
         Namespace(
             annotations=[],
             identification=Identification(short_name=None, name='N5'),
             body=[
                 NonFeatureMember(
                     visibility=Visibility.PUBLIC,
                     element=Comment(identification=None, about_list=None, locale=None,
                                     comment='/* 1 2 3 */')),
                 NonFeatureMember(
                     visibility=Visibility.PROTECTED,
                     element=Class(
                         is_abstract=False,
                         annotations=[],
                         is_all=False,
                         identification=Identification(
                             short_name=None,
                             name='X'
                         ),
                         multiplicity_bounds=None,
                         conjugation=None,
                         superclassing=None,
                         relationships=[],
                         body=[]
                     ),
                 ),
                 NonFeatureMember(
                     visibility=Visibility.PRIVATE,
                     element=Namespace(
                         annotations=[],
                         identification=Identification(
                             short_name=None, name='Nested'),
                         body=[
                             NonFeatureMember(visibility=None,
                                              element=Documentation(
                                                  identification=Identification(
                                                      short_name=None,
                                                      name='A'),
                                                  locale=None,
                                                  comment='/* 4 5 6 */'))
                         ]
                     )
                 ),
             ]
         )
         ),
    ])
    def test_namespace(self, text, expected):
        parser = _parser_for_rule('namespace')
        if isinstance(expected, type) and issubclass(expected, Exception):
            with pytest.raises(expected):
                _ = parser(text)
        else:
            v, rules = parser(text)
            assert v == expected
            assert 'namespace' in rules
