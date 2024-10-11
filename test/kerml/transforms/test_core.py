import pytest

from pysysml.kerml.models import Class, Identification, PrefixMetadataAnnotation, QualifiedName, SuperclassingPart, \
    MultiplicityBounds, IntValue, ConjugationPart, DisjoiningPart, UnioningPart, IntersectingPart, DifferencingPart, \
    NonFeatureMember, Documentation, Comment, Type, SpecializationPart, Visibility
from .base import _parser_for_rule


@pytest.mark.unittest
class TestKerMLTransformsCore:
    @pytest.mark.parametrize(['text', 'expected'], [
        ('class X;',
         Class(is_abstract=False, annotations=[], is_all=False,
               identification=Identification(short_name=None, name='X'), multiplicity_bounds=None, conjugation=None,
               superclassing=None, relationships=[], body=[])),
        ('#command class X;',
         Class(is_abstract=False, annotations=[PrefixMetadataAnnotation(feature=QualifiedName(names=['command']))],
               is_all=False, identification=Identification(short_name=None, name='X'), multiplicity_bounds=None,
               conjugation=None, superclassing=None, relationships=[], body=[])),
        ('abstract #command class X;',
         Class(is_abstract=True, annotations=[PrefixMetadataAnnotation(feature=QualifiedName(names=['command']))],
               is_all=False, identification=Identification(short_name=None, name='X'), multiplicity_bounds=None,
               conjugation=None, superclassing=None, relationships=[], body=[])),
        ('abstract #command class all X;',
         Class(is_abstract=True, annotations=[PrefixMetadataAnnotation(feature=QualifiedName(names=['command']))],
               is_all=True, identification=Identification(short_name=None, name='X'), multiplicity_bounds=None,
               conjugation=None, superclassing=None, relationships=[], body=[])),
        ('class X :> Y;',
         Class(is_abstract=False, annotations=[], is_all=False,
               identification=Identification(short_name=None, name='X'), multiplicity_bounds=None, conjugation=None,
               superclassing=SuperclassingPart(items=[QualifiedName(names=['Y'])]), relationships=[], body=[])),
        ('class X[10] :> Y;',
         Class(is_abstract=False, annotations=[], is_all=False,
               identification=Identification(short_name=None, name='X'),
               multiplicity_bounds=MultiplicityBounds(lower_bound=None, upper_bound=IntValue(raw='10')),
               conjugation=None, superclassing=SuperclassingPart(items=[QualifiedName(names=['Y'])]), relationships=[],
               body=[])),
        ('class X[1..Z] :> Y;',
         Class(is_abstract=False, annotations=[], is_all=False,
               identification=Identification(short_name=None, name='X'),
               multiplicity_bounds=MultiplicityBounds(lower_bound=IntValue(raw='1'),
                                                      upper_bound=QualifiedName(names=['Z'])), conjugation=None,
               superclassing=SuperclassingPart(items=[QualifiedName(names=['Y'])]), relationships=[], body=[])),
        ('class X ~ Y;',
         Class(is_abstract=False, annotations=[], is_all=False,
               identification=Identification(short_name=None, name='X'), multiplicity_bounds=None,
               conjugation=ConjugationPart(item=QualifiedName(names=['Y'])), superclassing=None, relationships=[],
               body=[])),
        ('class X ~ Y disjoint from Z, T;',
         Class(is_abstract=False, annotations=[], is_all=False,
               identification=Identification(short_name=None, name='X'), multiplicity_bounds=None,
               conjugation=ConjugationPart(item=QualifiedName(names=['Y'])), superclassing=None,
               relationships=[DisjoiningPart(items=[QualifiedName(names=['Z']), QualifiedName(names=['T'])])],
               body=[])),
        ('abstract class X ~ Y disjoint from Z1, T1 unions Z2, T2 intersects Z3, T3 '
         'differences Z4, T4;',
         Class(is_abstract=True, annotations=[], is_all=False, identification=Identification(short_name=None, name='X'),
               multiplicity_bounds=None, conjugation=ConjugationPart(item=QualifiedName(names=['Y'])),
               superclassing=None,
               relationships=[DisjoiningPart(items=[QualifiedName(names=['Z1']), QualifiedName(names=['T1'])]),
                              UnioningPart(items=[QualifiedName(names=['Z2']), QualifiedName(names=['T2'])]),
                              IntersectingPart(items=[QualifiedName(names=['Z3']), QualifiedName(names=['T3'])]),
                              DifferencingPart(items=[QualifiedName(names=['Z4']), QualifiedName(names=['T4'])])],
               body=[])),
        ('class X ~ Y disjoint from Z, T {\n'
         '\n'
         '    /* 123 */\n'
         '\n'
         '    doc X /* 456 */\n'
         '\n'
         '}',
         Class(is_abstract=False, annotations=[], is_all=False,
               identification=Identification(short_name=None, name='X'), multiplicity_bounds=None,
               conjugation=ConjugationPart(item=QualifiedName(names=['Y'])), superclassing=None,
               relationships=[DisjoiningPart(items=[QualifiedName(names=['Z']), QualifiedName(names=['T'])])], body=[
                 NonFeatureMember(visibility=None, element=Comment(identification=None, about_list=None, locale=None,
                                                                   comment='/* 123 */')),
                 NonFeatureMember(visibility=None,
                                  element=Documentation(identification=Identification(short_name=None, name='X'),
                                                        locale=None, comment='/* 456 */'))])),
    ])
    def test_class_statement(self, text, expected):
        parser = _parser_for_rule('class_statement')
        if isinstance(expected, type) and issubclass(expected, Exception):
            with pytest.raises(expected):
                _ = parser(text)
        else:
            v, rules = parser(text)
            assert v == expected
            assert 'class_statement' in rules

    @pytest.mark.parametrize(['text', 'expected'], [
        ('type A  disjoint from B;',
         Type(is_abstract=False, annotations=[], is_all=False, identification=Identification(short_name=None, name='A'),
              multiplicity_bounds=None, conjugation=None, specialization=None,
              relationships=[DisjoiningPart(items=[QualifiedName(names=['B'])])], body=[])),
        ('type A specializes Base::Anything disjoint from B;',
         Type(is_abstract=False, annotations=[], is_all=False, identification=Identification(short_name=None, name='A'),
              multiplicity_bounds=None, conjugation=None,
              specialization=SpecializationPart(items=[QualifiedName(names=['Base', 'Anything'])]),
              relationships=[DisjoiningPart(items=[QualifiedName(names=['B'])])], body=[])),
        ("type <'+'> C conjugates A;",
         Type(is_abstract=False, annotations=[], is_all=False, identification=Identification(short_name='+', name='C'),
              multiplicity_bounds=None, conjugation=ConjugationPart(item=QualifiedName(names=['A'])),
              specialization=None, relationships=[], body=[])),
        ('#command type C ~ A;',
         Type(is_abstract=False, annotations=[PrefixMetadataAnnotation(feature=QualifiedName(names=['command']))],
              is_all=False, identification=Identification(short_name=None, name='C'), multiplicity_bounds=None,
              conjugation=ConjugationPart(item=QualifiedName(names=['A'])), specialization=None, relationships=[],
              body=[])),
        ('abstract type A specializes Base::Anything;',
         Type(is_abstract=True, annotations=[], is_all=False, identification=Identification(short_name=None, name='A'),
              multiplicity_bounds=None, conjugation=None,
              specialization=SpecializationPart(items=[QualifiedName(names=['Base', 'Anything'])]), relationships=[],
              body=[])),
        ('type all A1 specializes A;',
         Type(is_abstract=False, annotations=[], is_all=True, identification=Identification(short_name=None, name='A1'),
              multiplicity_bounds=None, conjugation=None,
              specialization=SpecializationPart(items=[QualifiedName(names=['A'])]), relationships=[], body=[])),
        ('type A2 [1..10] :> A {\n    private /* 123 */\n}',
         Type(is_abstract=False, annotations=[], is_all=False,
              identification=Identification(short_name=None, name='A2'),
              multiplicity_bounds=MultiplicityBounds(lower_bound=IntValue(raw='1'), upper_bound=IntValue(raw='10')),
              conjugation=None, specialization=SpecializationPart(items=[QualifiedName(names=['A'])]), relationships=[],
              body=[NonFeatureMember(visibility=Visibility.PRIVATE,
                                     element=Comment(identification=None, about_list=None, locale=None,
                                                     comment='/* 123 */'))])),
    ])
    @pytest.mark.focus
    def test_type(self, text, expected):
        parser = _parser_for_rule('type')
        if isinstance(expected, type) and issubclass(expected, Exception):
            with pytest.raises(expected):
                _ = parser(text)
        else:
            v, rules = parser(text)
            assert v == expected
            assert 'type' in rules
