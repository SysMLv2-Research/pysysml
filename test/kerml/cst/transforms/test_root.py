import pytest

from pysysml.kerml.cst.models import Comment, Identification, QualifiedName, Documentation, Dependency, \
    PrefixMetadataAnnotation, FeatureChain, TextualRepresentation, Namespace, NonFeatureMember, Visibility, Class, \
    Import, Alias, NamespaceFeatureMember, Feature
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
                         identification=Identification(short_name=None, name='Nested'),
                         body=[
                             NonFeatureMember(visibility=None, element=Documentation(
                                 identification=Identification(short_name=None, name='A'), locale=None,
                                 comment='/* 4 5 6 */'))
                         ]
                     )
                 ),
             ]
         )
         ),
        ('namespace N6 {\n'
         '    import N4::A;\n'
         '    import N4::C; // Imported with name "C".\n'
         '    namespace M {\n'
         '        import C; // "C" is re-imported from N4 into M.\n'
         '    }\n'
         '}',
         Namespace(annotations=[], identification=Identification(short_name=None, name='N6'), body=[
             Import(visibility=None, is_all=False, is_recursive=False, is_namespace=False,
                    name=QualifiedName(names=['N4', 'A']), filters=[], body=[]),
             Import(visibility=None, is_all=False, is_recursive=False, is_namespace=False,
                    name=QualifiedName(names=['N4', 'C']), filters=[], body=[]),
             NonFeatureMember(
                 visibility=None,
                 element=Namespace(
                     annotations=[],
                     identification=Identification(short_name=None, name='M'),
                     body=[Import(visibility=None, is_all=False, is_recursive=False, is_namespace=False,
                                  name=QualifiedName(names=['C']), filters=[], body=[])]
                 )
             )
         ]
                   )
         ),
        ('namespace N7 {\n'
         '    // Memberships A, B and C are all imported from N4.\n'
         '    import N4::*;\n'
         '}',
         Namespace(annotations=[], identification=Identification(short_name=None, name='N7'), body=[
             Import(visibility=None, is_all=False, is_recursive=False, is_namespace=True,
                    name=QualifiedName(names=['N4']), filters=[], body=[])])),
        ('namespace N8 {\n'
         '    class A;\n'
         '    class B;\n'
         '    namespace M {\n'
         '        class C;\n'
         '    }\n'
         '}',
         Namespace(annotations=[], identification=Identification(short_name=None, name='N8'), body=[
             NonFeatureMember(visibility=None,
                              element=Class(is_abstract=False, annotations=[], is_all=False,
                                            identification=Identification(short_name=None, name='A'),
                                            multiplicity_bounds=None, conjugation=None,
                                            superclassing=None, relationships=[], body=[])),
             NonFeatureMember(visibility=None,
                              element=Class(is_abstract=False, annotations=[], is_all=False,
                                            identification=Identification(short_name=None, name='B'),
                                            multiplicity_bounds=None, conjugation=None,
                                            superclassing=None, relationships=[], body=[])),
             NonFeatureMember(visibility=None,
                              element=Namespace(
                                  annotations=[],
                                  identification=Identification(short_name=None, name='M'),
                                  body=[
                                      NonFeatureMember(
                                          visibility=None,
                                          element=Class(
                                              is_abstract=False, annotations=[], is_all=False,
                                              identification=Identification(short_name=None, name='C'),
                                              multiplicity_bounds=None, conjugation=None,
                                              superclassing=None, relationships=[],
                                              body=[]
                                          )
                                      )
                                  ]
                              )
                              )
         ]
                   )
         ),
        ('namespace N9 {\n'
         '    import N8::**;\n'
         '    // The above recursive import is equivalent to all\n'
         '    // of the following taken together:\n'
         '    // import N8;\n'
         '    // import N8::*;\n'
         '    // import N8::M::*;\n'
         '}',
         Namespace(annotations=[], identification=Identification(short_name=None, name='N9'), body=[
             Import(visibility=None, is_all=False, is_recursive=True, is_namespace=False,
                    name=QualifiedName(names=['N8']), filters=[], body=[])])),
        ('namespace N10 {\n'
         '    import N8::*::**;\n'
         '    // The above recursive import is equivalent to all\n'
         '    // of the following taken together:\n'
         '    // import N8::*;\n'
         '    // import N8::M::*;\n'
         '    // (Note that N8 itself is not imported.)\n'
         '}',
         Namespace(annotations=[], identification=Identification(short_name=None, name='N10'), body=[
             Import(visibility=None, is_all=False, is_recursive=True, is_namespace=True,
                    name=QualifiedName(names=['N8']), filters=[], body=[])])),
        ('namespace N11 {\n'
         '    public import N4::A {\n'
         '        /* The imported membership is visible outside N11. */\n'
         '    }\n'
         '    private import N5::* {\n'
         '        doc /* None of the imported memberships are visible\n'
         '        * outside of N11. */\n'
         '    }\n'
         '}',
         Namespace(annotations=[], identification=Identification(short_name=None, name='N11'), body=[
             Import(visibility=Visibility.PUBLIC, is_all=False, is_recursive=False, is_namespace=False,
                    name=QualifiedName(names=['N4', 'A']), filters=[], body=[
                     Comment(identification=None, about_list=None, locale=None,
                             comment='/* The imported membership is visible outside N11. */')]),
             Import(visibility=Visibility.PRIVATE, is_all=False, is_recursive=False, is_namespace=True,
                    name=QualifiedName(names=['N5']), filters=[], body=[
                     Documentation(identification=Identification(short_name=None, name=None), locale=None,
                                   comment='/* None of the imported memberships are visible\n        * outside of N11. */')])])),
        ("namespace N12 {\n  import Annotations::*;\n  import NA::*[x::'1'];\n}",
         Namespace(annotations=[], identification=Identification(short_name=None, name='N12'), body=[
             Import(visibility=None, is_all=False, is_recursive=False, is_namespace=True,
                    name=QualifiedName(names=['Annotations']), filters=[], body=[]),
             Import(visibility=None, is_all=False, is_recursive=False, is_namespace=True,
                    name=QualifiedName(names=['NA']), filters=[QualifiedName(names=['x', '1'])], body=[])])),
        ('namespace N4 {\n'
         '    alias <C> CCC for B {\n'
         '        doc /* Documentation of the alias. */\n'
         '    }\n'
         '    private alias D for B;\n'
         '}',
         Namespace(annotations=[], identification=Identification(short_name=None, name='N4'), body=[
             Alias(visibility=None, identification=Identification(short_name='C', name='CCC'),
                   name=QualifiedName(names=['B']), body=[
                     Documentation(identification=Identification(short_name=None, name=None), locale=None,
                                   comment='/* Documentation of the alias. */')]),
             Alias(visibility=Visibility.PRIVATE, identification=Identification(short_name=None, name='D'),
                   name=QualifiedName(names=['B']), body=[])])),
        ("namespace <'+'> {\n    protected feature x;\n}",
         Namespace(annotations=[], identification=Identification(short_name='+', name=None), body=[
             NamespaceFeatureMember(visibility=Visibility.PROTECTED,
                                    element=Feature(direction=None, is_abstract=False, relationship_type=None,
                                                    is_readonly=False, is_derived=False, is_end=False, annotations=[],
                                                    is_all=False,
                                                    identification=Identification(short_name=None, name='x'),
                                                    specializations=[], multiplicity=None, is_ordered=False,
                                                    is_nonunique=False, conjugation=None, relationships=[],
                                                    is_default=False, value_type=None, value=None, body=[]))])),
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

    @pytest.mark.parametrize(['text', 'expected'], [
        ('import N4::C; // Imported with name "C".',
         Import(visibility=None, is_all=False, is_recursive=False, is_namespace=False,
                name=QualifiedName(names=['N4', 'C']), filters=[], body=[])),
        ('import N4::*;',
         Import(visibility=None, is_all=False, is_recursive=False, is_namespace=True, name=QualifiedName(names=['N4']),
                filters=[], body=[])),
        ('public import N4::A {\n'
         '        /* The imported membership is visible outside N11. */\n'
         '    }',
         Import(visibility=Visibility.PUBLIC, is_all=False, is_recursive=False, is_namespace=False,
                name=QualifiedName(names=['N4', 'A']), filters=[], body=[
                 Comment(identification=None, about_list=None, locale=None,
                         comment='/* The imported membership is visible outside N11. */')])),
        ('private import N5::* {\n'
         '    doc /* None of the imported memberships are visible\n'
         '    * outside of N11. */\n'
         '}',
         Import(visibility=Visibility.PRIVATE, is_all=False, is_recursive=False, is_namespace=True,
                name=QualifiedName(names=['N5']), filters=[], body=[
                 Documentation(identification=Identification(short_name=None, name=None), locale=None,
                               comment='/* None of the imported memberships are visible\n    * outside of N11. */')])),
        ('import N8::**;',
         Import(visibility=None, is_all=False, is_recursive=True, is_namespace=False, name=QualifiedName(names=['N8']),
                filters=[], body=[])),
        ('import N8::*::**;',
         Import(visibility=None, is_all=False, is_recursive=True, is_namespace=True, name=QualifiedName(names=['N8']),
                filters=[], body=[])),
        ("import all NA::*[x::'1'];",
         Import(visibility=None, is_all=True, is_recursive=False, is_namespace=True, name=QualifiedName(names=['NA']),
                filters=[QualifiedName(names=['x', '1'])], body=[])),
        ("protected import NA::X[x::'1'];",
         Import(visibility=Visibility.PROTECTED, is_all=False, is_recursive=False, is_namespace=False,
                name=QualifiedName(names=['NA', 'X']), filters=[QualifiedName(names=['x', '1'])], body=[])),
    ])
    def test_import_statement(self, text, expected):
        parser = _parser_for_rule('import_statement')
        if isinstance(expected, type) and issubclass(expected, Exception):
            with pytest.raises(expected):
                _ = parser(text)
        else:
            v, rules = parser(text)
            assert v == expected
            assert 'import_statement' in rules

    @pytest.mark.parametrize(['text', 'expected'], [
        ('alias <C> CCC for B {\n    doc /* Documentation of the alias. */\n}',
         Alias(visibility=None, identification=Identification(short_name='C', name='CCC'),
               name=QualifiedName(names=['B']), body=[
                 Documentation(identification=Identification(short_name=None, name=None), locale=None,
                               comment='/* Documentation of the alias. */')])),
        ('private alias D for B;',
         Alias(visibility=Visibility.PRIVATE, identification=Identification(short_name=None, name='D'),
               name=QualifiedName(names=['B']), body=[])),
    ])
    def test_alias_member(self, text, expected):
        parser = _parser_for_rule('alias_member')
        if isinstance(expected, type) and issubclass(expected, Exception):
            with pytest.raises(expected):
                _ = parser(text)
        else:
            v, rules = parser(text)
            assert v == expected
            assert 'alias_member' in rules
