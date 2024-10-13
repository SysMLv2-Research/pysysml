import pytest

from pysysml.kerml.models import Class, Identification, PrefixMetadataAnnotation, QualifiedName, SuperclassingPart, \
    MultiplicityBounds, IntValue, ConjugationPart, DisjoiningPart, UnioningPart, IntersectingPart, DifferencingPart, \
    NonFeatureMember, Documentation, Comment, Type, SpecializationPart, Visibility, Feature, SubsettingsPart, \
    RedefinitionsPart, TypingsPart, ReferencesPart, ChainingPart, InvertingPart, TypeFeaturingPart, FeatureDirection, \
    FeatureRelationshipType, OwnedFeatureMember, InfValue, FeatureChain, RealValue, FeatureValueType, Namespace, \
    TypeFeatureMember, Specialization, Conjugation, Disjoining, Classifier, Subclassification, FeatureTyping, \
    Subsetting, Redefinition, FeatureInverting, TypeFeaturing, BinOp, InvocationExpression
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
        ('type Super specializes Base::Anything {\n'
         '    private namespace N {\n'
         '        type Sub specializes Super;\n'
         '    }\n'
         '    protected feature f : N::Sub;\n'
         '    member feature f1 : Super featured by N::Sub;\n'
         '}',
         Type(is_abstract=False, annotations=[], is_all=False,
              identification=Identification(short_name=None, name='Super'), multiplicity_bounds=None, conjugation=None,
              specialization=SpecializationPart(items=[QualifiedName(names=['Base', 'Anything'])]), relationships=[],
              body=[NonFeatureMember(visibility=Visibility.PRIVATE,
                                     element=Namespace(annotations=[],
                                                       identification=Identification(
                                                           short_name=None, name='N'),
                                                       body=[NonFeatureMember(
                                                           visibility=None, element=Type(
                                                               is_abstract=False,
                                                               annotations=[],
                                                               is_all=False,
                                                               identification=Identification(
                                                                   short_name=None,
                                                                   name='Sub'),
                                                               multiplicity_bounds=None,
                                                               conjugation=None,
                                                               specialization=SpecializationPart(
                                                                   items=[QualifiedName(
                                                                       names=[
                                                                           'Super'])]),
                                                               relationships=[],
                                                               body=[]))])),
                    OwnedFeatureMember(visibility=Visibility.PROTECTED,
                                       element=Feature(direction=None, is_abstract=False, relationship_type=None,
                                                       is_readonly=False, is_derived=False, is_end=False,
                                                       annotations=[], is_all=False,
                                                       identification=Identification(short_name=None, name='f'),
                                                       specializations=[
                                                           TypingsPart(items=[QualifiedName(names=['N', 'Sub'])])],
                                                       multiplicity=None, is_ordered=False, is_nonunique=False,
                                                       conjugation=None, relationships=[], is_default=False,
                                                       value_type=None, value=None, body=[])),
                    TypeFeatureMember(visibility=None,
                                      element=Feature(direction=None, is_abstract=False, relationship_type=None,
                                                      is_readonly=False, is_derived=False, is_end=False, annotations=[],
                                                      is_all=False,
                                                      identification=Identification(short_name=None, name='f1'),
                                                      specializations=[
                                                          TypingsPart(items=[QualifiedName(names=['Super'])])],
                                                      multiplicity=None, is_ordered=False, is_nonunique=False,
                                                      conjugation=None, relationships=[
                                              TypeFeaturingPart(items=[QualifiedName(names=['N', 'Sub'])])],
                                                      is_default=False, value_type=None, value=None, body=[]))])),
    ])
    def test_type(self, text, expected):
        parser = _parser_for_rule('type')
        if isinstance(expected, type) and issubclass(expected, Exception):
            with pytest.raises(expected):
                _ = parser(text)
        else:
            v, rules = parser(text)
            assert v == expected
            assert 'type' in rules

    @pytest.mark.parametrize(['text', 'expected'], [
        ('feature X;',
         Feature(direction=None, is_abstract=False, relationship_type=None, is_readonly=False, is_derived=False,
                 is_end=False, annotations=[], is_all=False, identification=Identification(short_name=None, name='X'),
                 specializations=[], multiplicity=None, is_ordered=False, is_nonunique=False, conjugation=None,
                 relationships=[], is_default=False, value_type=None, value=None, body=[])),
        ("feature <'+'> X;",
         Feature(direction=None, is_abstract=False, relationship_type=None, is_readonly=False, is_derived=False,
                 is_end=False, annotations=[], is_all=False, identification=Identification(short_name='+', name='X'),
                 specializations=[], multiplicity=None, is_ordered=False, is_nonunique=False, conjugation=None,
                 relationships=[], is_default=False, value_type=None, value=None, body=[])),
        ("feature <'+'>;",
         Feature(direction=None, is_abstract=False, relationship_type=None, is_readonly=False, is_derived=False,
                 is_end=False, annotations=[], is_all=False, identification=Identification(short_name='+', name=None),
                 specializations=[], multiplicity=None, is_ordered=False, is_nonunique=False, conjugation=None,
                 relationships=[], is_default=False, value_type=None, value=None, body=[])),
        ('feature ~X;',
         Feature(direction=None, is_abstract=False, relationship_type=None, is_readonly=False, is_derived=False,
                 is_end=False, annotations=[], is_all=False, identification=None, specializations=[], multiplicity=None,
                 is_ordered=False, is_nonunique=False, conjugation=ConjugationPart(item=QualifiedName(names=['X'])),
                 relationships=[], is_default=False, value_type=None, value=None, body=[])),
        ('feature :> X;',
         Feature(direction=None, is_abstract=False, relationship_type=None, is_readonly=False, is_derived=False,
                 is_end=False, annotations=[], is_all=False, identification=None,
                 specializations=[SubsettingsPart(items=[QualifiedName(names=['X'])])], multiplicity=None,
                 is_ordered=False, is_nonunique=False, conjugation=None, relationships=[], is_default=False,
                 value_type=None, value=None, body=[])),
        ('feature X ~ Y ;',
         Feature(direction=None, is_abstract=False, relationship_type=None, is_readonly=False, is_derived=False,
                 is_end=False, annotations=[], is_all=False, identification=Identification(short_name=None, name='X'),
                 specializations=[], multiplicity=None, is_ordered=False, is_nonunique=False,
                 conjugation=ConjugationPart(item=QualifiedName(names=['Y'])), relationships=[], is_default=False,
                 value_type=None, value=None, body=[])),
        ('feature X :> Y, Z;',
         Feature(direction=None, is_abstract=False, relationship_type=None, is_readonly=False, is_derived=False,
                 is_end=False, annotations=[], is_all=False, identification=Identification(short_name=None, name='X'),
                 specializations=[SubsettingsPart(items=[QualifiedName(names=['Y']), QualifiedName(names=['Z'])])],
                 multiplicity=None, is_ordered=False, is_nonunique=False, conjugation=None, relationships=[],
                 is_default=False, value_type=None, value=None, body=[])),
        ('feature X :> Y [1..10] :>> Z;',
         Feature(direction=None, is_abstract=False, relationship_type=None, is_readonly=False, is_derived=False,
                 is_end=False, annotations=[], is_all=False, identification=Identification(short_name=None, name='X'),
                 specializations=[SubsettingsPart(items=[QualifiedName(names=['Y'])]),
                                  RedefinitionsPart(items=[QualifiedName(names=['Z'])])],
                 multiplicity=MultiplicityBounds(lower_bound=IntValue(raw='1'), upper_bound=IntValue(raw='10')),
                 is_ordered=False, is_nonunique=False, conjugation=None, relationships=[], is_default=False,
                 value_type=None, value=None, body=[])),
        ('feature all X : Y [10] :> Z :>> T ::> K;',
         Feature(direction=None, is_abstract=False, relationship_type=None, is_readonly=False, is_derived=False,
                 is_end=False, annotations=[], is_all=True, identification=Identification(short_name=None, name='X'),
                 specializations=[TypingsPart(items=[QualifiedName(names=['Y'])]),
                                  SubsettingsPart(items=[QualifiedName(names=['Z'])]),
                                  RedefinitionsPart(items=[QualifiedName(names=['T'])]),
                                  ReferencesPart(item=QualifiedName(names=['K']))],
                 multiplicity=MultiplicityBounds(lower_bound=None, upper_bound=IntValue(raw='10')), is_ordered=False,
                 is_nonunique=False, conjugation=None, relationships=[], is_default=False, value_type=None, value=None,
                 body=[])),
        ('feature X [0..10] ;',
         Feature(direction=None, is_abstract=False, relationship_type=None, is_readonly=False, is_derived=False,
                 is_end=False, annotations=[], is_all=False, identification=Identification(short_name=None, name='X'),
                 specializations=[],
                 multiplicity=MultiplicityBounds(lower_bound=IntValue(raw='0'), upper_bound=IntValue(raw='10')),
                 is_ordered=False, is_nonunique=False, conjugation=None, relationships=[], is_default=False,
                 value_type=None, value=None, body=[])),
        ('feature X [0..10] ordered;',
         Feature(direction=None, is_abstract=False, relationship_type=None, is_readonly=False, is_derived=False,
                 is_end=False, annotations=[], is_all=False, identification=Identification(short_name=None, name='X'),
                 specializations=[],
                 multiplicity=MultiplicityBounds(lower_bound=IntValue(raw='0'), upper_bound=IntValue(raw='10')),
                 is_ordered=True, is_nonunique=False, conjugation=None, relationships=[], is_default=False,
                 value_type=None, value=None, body=[])),
        ('feature X [0..10] nonunique;',
         Feature(direction=None, is_abstract=False, relationship_type=None, is_readonly=False, is_derived=False,
                 is_end=False, annotations=[], is_all=False, identification=Identification(short_name=None, name='X'),
                 specializations=[],
                 multiplicity=MultiplicityBounds(lower_bound=IntValue(raw='0'), upper_bound=IntValue(raw='10')),
                 is_ordered=False, is_nonunique=True, conjugation=None, relationships=[], is_default=False,
                 value_type=None, value=None, body=[])),
        ('feature X [0..10] ordered nonunique;',
         Feature(direction=None, is_abstract=False, relationship_type=None, is_readonly=False, is_derived=False,
                 is_end=False, annotations=[], is_all=False, identification=Identification(short_name=None, name='X'),
                 specializations=[],
                 multiplicity=MultiplicityBounds(lower_bound=IntValue(raw='0'), upper_bound=IntValue(raw='10')),
                 is_ordered=True, is_nonunique=True, conjugation=None, relationships=[], is_default=False,
                 value_type=None, value=None, body=[])),
        ('feature X [0..10] nonunique ordered ;',
         Feature(direction=None, is_abstract=False, relationship_type=None, is_readonly=False, is_derived=False,
                 is_end=False, annotations=[], is_all=False, identification=Identification(short_name=None, name='X'),
                 specializations=[],
                 multiplicity=MultiplicityBounds(lower_bound=IntValue(raw='0'), upper_bound=IntValue(raw='10')),
                 is_ordered=True, is_nonunique=True, conjugation=None, relationships=[], is_default=False,
                 value_type=None, value=None, body=[])),
        ('feature X ordered;',
         Feature(direction=None, is_abstract=False, relationship_type=None, is_readonly=False, is_derived=False,
                 is_end=False, annotations=[], is_all=False, identification=Identification(short_name=None, name='X'),
                 specializations=[], multiplicity=None, is_ordered=True, is_nonunique=False, conjugation=None,
                 relationships=[], is_default=False, value_type=None, value=None, body=[])),
        ('feature X nonunique;',
         Feature(direction=None, is_abstract=False, relationship_type=None, is_readonly=False, is_derived=False,
                 is_end=False, annotations=[], is_all=False, identification=Identification(short_name=None, name='X'),
                 specializations=[], multiplicity=None, is_ordered=False, is_nonunique=True, conjugation=None,
                 relationships=[], is_default=False, value_type=None, value=None, body=[])),
        ('feature X ordered nonunique;',
         Feature(direction=None, is_abstract=False, relationship_type=None, is_readonly=False, is_derived=False,
                 is_end=False, annotations=[], is_all=False, identification=Identification(short_name=None, name='X'),
                 specializations=[], multiplicity=None, is_ordered=True, is_nonunique=True, conjugation=None,
                 relationships=[], is_default=False, value_type=None, value=None, body=[])),
        ('feature X nonunique ordered ;',
         Feature(direction=None, is_abstract=False, relationship_type=None, is_readonly=False, is_derived=False,
                 is_end=False, annotations=[], is_all=False, identification=Identification(short_name=None, name='X'),
                 specializations=[], multiplicity=None, is_ordered=True, is_nonunique=True, conjugation=None,
                 relationships=[], is_default=False, value_type=None, value=None, body=[])),
        ("feature <'+'> chains X inverse of child featured by Vehicle;",
         Feature(direction=None, is_abstract=False, relationship_type=None, is_readonly=False, is_derived=False,
                 is_end=False, annotations=[], is_all=False, identification=Identification(short_name='+', name=None),
                 specializations=[], multiplicity=None, is_ordered=False, is_nonunique=False, conjugation=None,
                 relationships=[ChainingPart(item=QualifiedName(names=['X'])),
                                InvertingPart(item=QualifiedName(names=['child'])),
                                TypeFeaturingPart(items=[QualifiedName(names=['Vehicle'])])], is_default=False,
                 value_type=None, value=None, body=[])),
        ("in feature <'+'> X;",
         Feature(direction=FeatureDirection.IN, is_abstract=False, relationship_type=None, is_readonly=False,
                 is_derived=False, is_end=False, annotations=[], is_all=False,
                 identification=Identification(short_name='+', name='X'), specializations=[], multiplicity=None,
                 is_ordered=False, is_nonunique=False, conjugation=None, relationships=[], is_default=False,
                 value_type=None, value=None, body=[])),
        ("in <'+'> X;",
         Feature(direction=FeatureDirection.IN, is_abstract=False, relationship_type=None, is_readonly=False,
                 is_derived=False, is_end=False, annotations=[], is_all=False,
                 identification=Identification(short_name='+', name='X'), specializations=[], multiplicity=None,
                 is_ordered=False, is_nonunique=False, conjugation=None, relationships=[], is_default=False,
                 value_type=None, value=None, body=[])),
        ("out <'+'> X;",
         Feature(direction=FeatureDirection.OUT, is_abstract=False, relationship_type=None, is_readonly=False,
                 is_derived=False, is_end=False, annotations=[], is_all=False,
                 identification=Identification(short_name='+', name='X'), specializations=[], multiplicity=None,
                 is_ordered=False, is_nonunique=False, conjugation=None, relationships=[], is_default=False,
                 value_type=None, value=None, body=[])),
        ("inout <'+'> X;",
         Feature(direction=FeatureDirection.INOUT, is_abstract=False, relationship_type=None, is_readonly=False,
                 is_derived=False, is_end=False, annotations=[], is_all=False,
                 identification=Identification(short_name='+', name='X'), specializations=[], multiplicity=None,
                 is_ordered=False, is_nonunique=False, conjugation=None, relationships=[], is_default=False,
                 value_type=None, value=None, body=[])),
        ("abstract <'+'> X;",
         Feature(direction=None, is_abstract=True, relationship_type=None, is_readonly=False, is_derived=False,
                 is_end=False, annotations=[], is_all=False, identification=Identification(short_name='+', name='X'),
                 specializations=[], multiplicity=None, is_ordered=False, is_nonunique=False, conjugation=None,
                 relationships=[], is_default=False, value_type=None, value=None, body=[])),
        ("in abstract portion <'+'> X;",
         Feature(direction=FeatureDirection.IN, is_abstract=True, relationship_type=FeatureRelationshipType.PORTION,
                 is_readonly=False, is_derived=False, is_end=False, annotations=[], is_all=False,
                 identification=Identification(short_name='+', name='X'), specializations=[], multiplicity=None,
                 is_ordered=False, is_nonunique=False, conjugation=None, relationships=[], is_default=False,
                 value_type=None, value=None, body=[])),
        ("inout composite <'+'> X;",
         Feature(direction=FeatureDirection.INOUT, is_abstract=False,
                 relationship_type=FeatureRelationshipType.COMPOSITE, is_readonly=False, is_derived=False, is_end=False,
                 annotations=[], is_all=False, identification=Identification(short_name='+', name='X'),
                 specializations=[], multiplicity=None, is_ordered=False, is_nonunique=False, conjugation=None,
                 relationships=[], is_default=False, value_type=None, value=None, body=[])),
        ('readonly derived end #command f : X ;',
         Feature(direction=None, is_abstract=False, relationship_type=None, is_readonly=True, is_derived=True,
                 is_end=True, annotations=[PrefixMetadataAnnotation(feature=QualifiedName(names=['command']))],
                 is_all=False, identification=Identification(short_name=None, name='f'),
                 specializations=[TypingsPart(items=[QualifiedName(names=['X'])])], multiplicity=None, is_ordered=False,
                 is_nonunique=False, conjugation=None, relationships=[], is_default=False, value_type=None, value=None,
                 body=[])),
        ('x {\n    /* 123 */\n}',
         Feature(direction=None, is_abstract=False, relationship_type=None, is_readonly=False, is_derived=False,
                 is_end=False, annotations=[], is_all=False, identification=Identification(short_name=None, name='x'),
                 specializations=[], multiplicity=None, is_ordered=False, is_nonunique=False, conjugation=None,
                 relationships=[], is_default=False, value_type=None, value=None, body=[
                 NonFeatureMember(visibility=None, element=Comment(identification=None, about_list=None, locale=None,
                                                                   comment='/* 123 */'))])),
        ('feature x typed by A, B subsets f redefines g;',
         Feature(direction=None, is_abstract=False, relationship_type=None, is_readonly=False, is_derived=False,
                 is_end=False, annotations=[], is_all=False, identification=Identification(short_name=None, name='x'),
                 specializations=[TypingsPart(items=[QualifiedName(names=['A']), QualifiedName(names=['B'])]),
                                  SubsettingsPart(items=[QualifiedName(names=['f'])]),
                                  RedefinitionsPart(items=[QualifiedName(names=['g'])])], multiplicity=None,
                 is_ordered=False, is_nonunique=False, conjugation=None, relationships=[], is_default=False,
                 value_type=None, value=None, body=[])),
        ('feature x redefines g typed by A subsets f typed by B;',
         Feature(direction=None, is_abstract=False, relationship_type=None, is_readonly=False, is_derived=False,
                 is_end=False, annotations=[], is_all=False, identification=Identification(short_name=None, name='x'),
                 specializations=[RedefinitionsPart(items=[QualifiedName(names=['g'])]),
                                  TypingsPart(items=[QualifiedName(names=['A'])]),
                                  SubsettingsPart(items=[QualifiedName(names=['f'])]),
                                  TypingsPart(items=[QualifiedName(names=['B'])])], multiplicity=None, is_ordered=False,
                 is_nonunique=False, conjugation=None, relationships=[], is_default=False, value_type=None, value=None,
                 body=[])),
        ('abstract feature person : Person; // Default subsets Base::things.',
         Feature(direction=None, is_abstract=True, relationship_type=None, is_readonly=False, is_derived=False,
                 is_end=False, annotations=[], is_all=False,
                 identification=Identification(short_name=None, name='person'),
                 specializations=[TypingsPart(items=[QualifiedName(names=['Person'])])], multiplicity=None,
                 is_ordered=False, is_nonunique=False, conjugation=None, relationships=[], is_default=False,
                 value_type=None, value=None, body=[])),
        ('feature child subsets person;',
         Feature(direction=None, is_abstract=False, relationship_type=None, is_readonly=False, is_derived=False,
                 is_end=False, annotations=[], is_all=False,
                 identification=Identification(short_name=None, name='child'),
                 specializations=[SubsettingsPart(items=[QualifiedName(names=['person'])])], multiplicity=None,
                 is_ordered=False, is_nonunique=False, conjugation=None, relationships=[], is_default=False,
                 value_type=None, value=None, body=[])),
        ('in feature fuelFlow : Fuel;',
         Feature(direction=FeatureDirection.IN, is_abstract=False, relationship_type=None, is_readonly=False,
                 is_derived=False, is_end=False, annotations=[], is_all=False,
                 identification=Identification(short_name=None, name='fuelFlow'),
                 specializations=[TypingsPart(items=[QualifiedName(names=['Fuel'])])], multiplicity=None,
                 is_ordered=False, is_nonunique=False, conjugation=None, relationships=[], is_default=False,
                 value_type=None, value=None, body=[])),
        ('feature fuelOutPort ~ fuelInPort;',
         Feature(direction=None, is_abstract=False, relationship_type=None, is_readonly=False, is_derived=False,
                 is_end=False, annotations=[], is_all=False,
                 identification=Identification(short_name=None, name='fuelOutPort'), specializations=[],
                 multiplicity=None, is_ordered=False, is_nonunique=False,
                 conjugation=ConjugationPart(item=QualifiedName(names=['fuelInPort'])), relationships=[],
                 is_default=False, value_type=None, value=None, body=[])),
        ('feature parent[2] : Person;',
         Feature(direction=None, is_abstract=False, relationship_type=None, is_readonly=False, is_derived=False,
                 is_end=False, annotations=[], is_all=False,
                 identification=Identification(short_name=None, name='parent'),
                 specializations=[TypingsPart(items=[QualifiedName(names=['Person'])])],
                 multiplicity=MultiplicityBounds(lower_bound=None, upper_bound=IntValue(raw='2')), is_ordered=False,
                 is_nonunique=False, conjugation=None, relationships=[], is_default=False, value_type=None, value=None,
                 body=[])),
        ('feature mother : Person[1] :> parent;',
         Feature(direction=None, is_abstract=False, relationship_type=None, is_readonly=False, is_derived=False,
                 is_end=False, annotations=[], is_all=False,
                 identification=Identification(short_name=None, name='mother'),
                 specializations=[TypingsPart(items=[QualifiedName(names=['Person'])]),
                                  SubsettingsPart(items=[QualifiedName(names=['parent'])])],
                 multiplicity=MultiplicityBounds(lower_bound=None, upper_bound=IntValue(raw='1')), is_ordered=False,
                 is_nonunique=False, conjugation=None, relationships=[], is_default=False, value_type=None, value=None,
                 body=[])),
        ('feature redefines children[0];',
         Feature(direction=None, is_abstract=False, relationship_type=None, is_readonly=False, is_derived=False,
                 is_end=False, annotations=[], is_all=False, identification=None,
                 specializations=[RedefinitionsPart(items=[QualifiedName(names=['children'])])],
                 multiplicity=MultiplicityBounds(lower_bound=None, upper_bound=IntValue(raw='0')), is_ordered=False,
                 is_nonunique=False, conjugation=None, relationships=[], is_default=False, value_type=None, value=None,
                 body=[])),
        ('feature fuelInPort {\n    in feature fuelFlow : Fuel;\n}',
         Feature(direction=None, is_abstract=False, relationship_type=None, is_readonly=False, is_derived=False,
                 is_end=False, annotations=[], is_all=False,
                 identification=Identification(short_name=None, name='fuelInPort'), specializations=[],
                 multiplicity=None, is_ordered=False, is_nonunique=False, conjugation=None, relationships=[],
                 is_default=False, value_type=None, value=None,
                 body=[OwnedFeatureMember(visibility=None,
                                          element=Feature(
                                              direction=FeatureDirection.IN,
                                              is_abstract=False,
                                              relationship_type=None,
                                              is_readonly=False,
                                              is_derived=False,
                                              is_end=False,
                                              annotations=[],
                                              is_all=False,
                                              identification=Identification(
                                                  short_name=None,
                                                  name='fuelFlow'),
                                              specializations=[
                                                  TypingsPart(items=[
                                                      QualifiedName(
                                                          names=[
                                                              'Fuel'])])],
                                              multiplicity=None,
                                              is_ordered=False,
                                              is_nonunique=False,
                                              conjugation=None,
                                              relationships=[],
                                              is_default=False,
                                              value_type=None,
                                              value=None, body=[]))])),
        ('feature sensorReadings : ScalarValues::Real [*] nonunique ordered;',
         Feature(direction=None, is_abstract=False, relationship_type=None, is_readonly=False, is_derived=False,
                 is_end=False, annotations=[], is_all=False,
                 identification=Identification(short_name=None, name='sensorReadings'),
                 specializations=[TypingsPart(items=[QualifiedName(names=['ScalarValues', 'Real'])])],
                 multiplicity=MultiplicityBounds(lower_bound=None, upper_bound=InfValue()), is_ordered=True,
                 is_nonunique=True, conjugation=None, relationships=[], is_default=False, value_type=None, value=None,
                 body=[])),
        ('feature cousins : Person[*] chains parents.siblings.children featured by '
         'Person;',
         Feature(direction=None, is_abstract=False, relationship_type=None, is_readonly=False, is_derived=False,
                 is_end=False, annotations=[], is_all=False,
                 identification=Identification(short_name=None, name='cousins'),
                 specializations=[TypingsPart(items=[QualifiedName(names=['Person'])])],
                 multiplicity=MultiplicityBounds(lower_bound=None, upper_bound=InfValue()), is_ordered=False,
                 is_nonunique=False, conjugation=None, relationships=[ChainingPart(item=FeatureChain(
                 items=[QualifiedName(names=['parents']), QualifiedName(names=['siblings']),
                        QualifiedName(names=['children'])])), TypeFeaturingPart(
                 items=[QualifiedName(names=['Person'])])], is_default=False, value_type=None, value=None, body=[])),
        ('feature children : Person[*] featured by Person inverse of parents;',
         Feature(direction=None, is_abstract=False, relationship_type=None, is_readonly=False, is_derived=False,
                 is_end=False, annotations=[], is_all=False,
                 identification=Identification(short_name=None, name='children'),
                 specializations=[TypingsPart(items=[QualifiedName(names=['Person'])])],
                 multiplicity=MultiplicityBounds(lower_bound=None, upper_bound=InfValue()), is_ordered=False,
                 is_nonunique=False, conjugation=None,
                 relationships=[TypeFeaturingPart(items=[QualifiedName(names=['Person'])]),
                                InvertingPart(item=QualifiedName(names=['parents']))], is_default=False,
                 value_type=None, value=None, body=[])),
        ('portion feature fuelPortion : Fuel;',
         Feature(direction=None, is_abstract=False, relationship_type=FeatureRelationshipType.PORTION,
                 is_readonly=False, is_derived=False, is_end=False, annotations=[], is_all=False,
                 identification=Identification(short_name=None, name='fuelPortion'),
                 specializations=[TypingsPart(items=[QualifiedName(names=['Fuel'])])], multiplicity=None,
                 is_ordered=False, is_nonunique=False, conjugation=None, relationships=[], is_default=False,
                 value_type=None, value=None, body=[])),
        ('in feature fuelFlow: Fuel;',
         Feature(direction=FeatureDirection.IN, is_abstract=False, relationship_type=None, is_readonly=False,
                 is_derived=False, is_end=False, annotations=[], is_all=False,
                 identification=Identification(short_name=None, name='fuelFlow'),
                 specializations=[TypingsPart(items=[QualifiedName(names=['Fuel'])])], multiplicity=None,
                 is_ordered=False, is_nonunique=False, conjugation=None, relationships=[], is_default=False,
                 value_type=None, value=None, body=[])),
        ('composite feature fuel : Fuel;',
         Feature(direction=None, is_abstract=False, relationship_type=FeatureRelationshipType.COMPOSITE,
                 is_readonly=False, is_derived=False, is_end=False, annotations=[], is_all=False,
                 identification=Identification(short_name=None, name='fuel'),
                 specializations=[TypingsPart(items=[QualifiedName(names=['Fuel'])])], multiplicity=None,
                 is_ordered=False, is_nonunique=False, conjugation=None, relationships=[], is_default=False,
                 value_type=None, value=None, body=[])),
        ('end feature owner[1] : Person;',
         Feature(direction=None, is_abstract=False, relationship_type=None, is_readonly=False, is_derived=False,
                 is_end=True, annotations=[], is_all=False,
                 identification=Identification(short_name=None, name='owner'),
                 specializations=[TypingsPart(items=[QualifiedName(names=['Person'])])],
                 multiplicity=MultiplicityBounds(lower_bound=None, upper_bound=IntValue(raw='1')), is_ordered=False,
                 is_nonunique=False, conjugation=None, relationships=[], is_default=False, value_type=None, value=None,
                 body=[])),
        ('end feature vehicle[*] : Vehicle;',
         Feature(direction=None, is_abstract=False, relationship_type=None, is_readonly=False, is_derived=False,
                 is_end=True, annotations=[], is_all=False,
                 identification=Identification(short_name=None, name='vehicle'),
                 specializations=[TypingsPart(items=[QualifiedName(names=['Vehicle'])])],
                 multiplicity=MultiplicityBounds(lower_bound=None, upper_bound=InfValue()), is_ordered=False,
                 is_nonunique=False, conjugation=None, relationships=[], is_default=False, value_type=None, value=None,
                 body=[])),
        ('feature mass[1] : Real default 1500.0;',
         Feature(direction=None, is_abstract=False, relationship_type=None, is_readonly=False, is_derived=False,
                 is_end=False, annotations=[], is_all=False,
                 identification=Identification(short_name=None, name='mass'),
                 specializations=[TypingsPart(items=[QualifiedName(names=['Real'])])],
                 multiplicity=MultiplicityBounds(lower_bound=None, upper_bound=IntValue(raw='1')), is_ordered=False,
                 is_nonunique=False, conjugation=None, relationships=[], is_default=True,
                 value_type=FeatureValueType.BIND, value=RealValue(raw='1500.0'), body=[])),
        ('feature engine[1] : Engine default := standardEngine;',
         Feature(direction=None, is_abstract=False, relationship_type=None, is_readonly=False, is_derived=False,
                 is_end=False, annotations=[], is_all=False,
                 identification=Identification(short_name=None, name='engine'),
                 specializations=[TypingsPart(items=[QualifiedName(names=['Engine'])])],
                 multiplicity=MultiplicityBounds(lower_bound=None, upper_bound=IntValue(raw='1')), is_ordered=False,
                 is_nonunique=False, conjugation=None, relationships=[], is_default=True,
                 value_type=FeatureValueType.INITIAL, value=QualifiedName(names=['standardEngine']), body=[])),
        ('feature cutoff[1] : Rational default = 0.75;',
         Feature(direction=None, is_abstract=False, relationship_type=None, is_readonly=False, is_derived=False,
                 is_end=False, annotations=[], is_all=False,
                 identification=Identification(short_name=None, name='cutoff'),
                 specializations=[TypingsPart(items=[QualifiedName(names=['Rational'])])],
                 multiplicity=MultiplicityBounds(lower_bound=None, upper_bound=IntValue(raw='1')), is_ordered=False,
                 is_nonunique=False, conjugation=None, relationships=[], is_default=True,
                 value_type=FeatureValueType.BIND, value=RealValue(raw='0.75'), body=[])),
        ('derived feature averageScore[1] : Rational = sx;',
         Feature(direction=None, is_abstract=False, relationship_type=None, is_readonly=False, is_derived=True,
                 is_end=False, annotations=[], is_all=False,
                 identification=Identification(short_name=None, name='averageScore'),
                 specializations=[TypingsPart(items=[QualifiedName(names=['Rational'])])],
                 multiplicity=MultiplicityBounds(lower_bound=None, upper_bound=IntValue(raw='1')), is_ordered=False,
                 is_nonunique=False, conjugation=None, relationships=[], is_default=False,
                 value_type=FeatureValueType.BIND, value=QualifiedName(names=['sx']), body=[])),
        ('feature count[1] : Natural := 0;',
         Feature(direction=None, is_abstract=False, relationship_type=None, is_readonly=False, is_derived=False,
                 is_end=False, annotations=[], is_all=False,
                 identification=Identification(short_name=None, name='count'),
                 specializations=[TypingsPart(items=[QualifiedName(names=['Natural'])])],
                 multiplicity=MultiplicityBounds(lower_bound=None, upper_bound=IntValue(raw='1')), is_ordered=False,
                 is_nonunique=False, conjugation=None, relationships=[], is_default=False,
                 value_type=FeatureValueType.INITIAL, value=IntValue(raw='0'), body=[])),
        ('feature dependents : Child[*];',
         Feature(direction=None, is_abstract=False, relationship_type=None, is_readonly=False, is_derived=False,
                 is_end=False, annotations=[], is_all=False,
                 identification=Identification(short_name=None, name='dependents'),
                 specializations=[TypingsPart(items=[QualifiedName(names=['Child'])])],
                 multiplicity=MultiplicityBounds(lower_bound=None, upper_bound=InfValue()), is_ordered=False,
                 is_nonunique=False, conjugation=None, relationships=[], is_default=False, value_type=None, value=None,
                 body=[])),
        ('feature grownOffspring : Adult[*] :> offspring;',
         Feature(direction=None, is_abstract=False, relationship_type=None, is_readonly=False, is_derived=False,
                 is_end=False, annotations=[], is_all=False,
                 identification=Identification(short_name=None, name='grownOffspring'),
                 specializations=[TypingsPart(items=[QualifiedName(names=['Adult'])]),
                                  SubsettingsPart(items=[QualifiedName(names=['offspring'])])],
                 multiplicity=MultiplicityBounds(lower_bound=None, upper_bound=InfValue()), is_ordered=False,
                 is_nonunique=False, conjugation=None, relationships=[], is_default=False, value_type=None, value=None,
                 body=[])),
        ('feature dependentOffspring : Child[*] :> dependents, offspring\n'
         '    differences offspring, grownOffspring\n'
         '    intersects dependents, offspring;',
         Feature(direction=None, is_abstract=False, relationship_type=None, is_readonly=False, is_derived=False,
                 is_end=False, annotations=[], is_all=False,
                 identification=Identification(short_name=None, name='dependentOffspring'),
                 specializations=[TypingsPart(items=[QualifiedName(names=['Child'])]), SubsettingsPart(
                     items=[QualifiedName(names=['dependents']), QualifiedName(names=['offspring'])])],
                 multiplicity=MultiplicityBounds(lower_bound=None, upper_bound=InfValue()), is_ordered=False,
                 is_nonunique=False, conjugation=None, relationships=[
                 DifferencingPart(items=[QualifiedName(names=['offspring']), QualifiedName(names=['grownOffspring'])]),
                 IntersectingPart(items=[QualifiedName(names=['dependents']), QualifiedName(names=['offspring'])])],
                 is_default=False, value_type=None, value=None, body=[])),
        ('feature foodItem typed by Food, InventoryItem;',
         Feature(direction=None, is_abstract=False, relationship_type=None, is_readonly=False, is_derived=False,
                 is_end=False, annotations=[], is_all=False,
                 identification=Identification(short_name=None, name='foodItem'), specializations=[
                 TypingsPart(items=[QualifiedName(names=['Food']), QualifiedName(names=['InventoryItem'])])],
                 multiplicity=None, is_ordered=False, is_nonunique=False, conjugation=None, relationships=[],
                 is_default=False, value_type=None, value=None, body=[])),
        ('derived feature averageScore[1] : Rational = sum(scores)/size(scores);',
         Feature(direction=None, is_abstract=False, relationship_type=None, is_readonly=False, is_derived=True,
                 is_end=False, annotations=[], is_all=False,
                 identification=Identification(short_name=None, name='averageScore'),
                 specializations=[TypingsPart(items=[QualifiedName(names=['Rational'])])],
                 multiplicity=MultiplicityBounds(lower_bound=None, upper_bound=IntValue(raw='1')), is_ordered=False,
                 is_nonunique=False, conjugation=None, relationships=[], is_default=False,
                 value_type=FeatureValueType.BIND,
                 value=BinOp(op='/', x=InvocationExpression(name=QualifiedName(names=['sum']),
                                                            arguments=[QualifiedName(names=['scores'])]),
                             y=InvocationExpression(name=QualifiedName(names=['size']),
                                                    arguments=[QualifiedName(names=['scores'])])),
                 body=[])),
        ('feature e = 1e-6 + m * c ^2;',
         Feature(direction=None, is_abstract=False, relationship_type=None, is_readonly=False, is_derived=False,
                 is_end=False, annotations=[], is_all=False, identification=Identification(short_name=None, name='e'),
                 specializations=[], multiplicity=None, is_ordered=False, is_nonunique=False, conjugation=None,
                 relationships=[], is_default=False, value_type=FeatureValueType.BIND,
                 value=BinOp(op='+', x=RealValue(raw='1e-6'), y=BinOp(op='*', x=QualifiedName(names=['m']),
                                                                      y=BinOp(op='^', x=QualifiedName(names=['c']),
                                                                              y=IntValue(raw='2')))), body=[])),
    ])
    def test_feature(self, text, expected):
        parser = _parser_for_rule('feature')
        if isinstance(expected, type) and issubclass(expected, Exception):
            with pytest.raises(expected):
                _ = parser(text)
        else:
            v, rules = parser(text)
            assert v == expected
            assert 'feature' in rules

    @pytest.mark.parametrize(['text', 'expected'], [
        ('specialization Gen subtype A specializes B;',
         Specialization(identification=Identification(short_name=None, name='Gen'),
                        specific_type=QualifiedName(names=['A']), general_type=QualifiedName(names=['B']), body=[])),
        ('subtype A specializes B;',
         Specialization(identification=None, specific_type=QualifiedName(names=['A']),
                        general_type=QualifiedName(names=['B']), body=[])),
        ('specialization subtype x :> Base::things {\n'
         '    doc /* This specialization is unnamed. */\n'
         '}',
         Specialization(identification=Identification(short_name=None, name=None),
                        specific_type=QualifiedName(names=['x']), general_type=QualifiedName(names=['Base', 'things']),
                        body=[Documentation(identification=Identification(short_name=None, name=None), locale=None,
                                            comment='/* This specialization is unnamed. */')])),
    ])
    def test_specialization(self, text, expected):
        parser = _parser_for_rule('specialization')
        if isinstance(expected, type) and issubclass(expected, Exception):
            with pytest.raises(expected):
                _ = parser(text)
        else:
            v, rules = parser(text)
            assert v == expected
            assert 'specialization' in rules

    @pytest.mark.parametrize(['text', 'expected'], [
        ('conjugation c1 conjugate Conjugate1 conjugates Original;',
         Conjugation(identification=Identification(short_name=None, name='c1'),
                     conjugate_type=QualifiedName(names=['Conjugate1']),
                     conjugated_type=QualifiedName(names=['Original']), body=[])),
        ('conjugation c2 conjugate Conjugate2 ~ Original {\n'
         '    doc /* This conjugation is equivalent to c1. */\n'
         '}',
         Conjugation(identification=Identification(short_name=None, name='c2'),
                     conjugate_type=QualifiedName(names=['Conjugate2']),
                     conjugated_type=QualifiedName(names=['Original']), body=[
                 Documentation(identification=Identification(short_name=None, name=None), locale=None,
                               comment='/* This conjugation is equivalent to c1. */')])),
        ('conjugate Conjugate1 conjugates Original;',
         Conjugation(identification=None, conjugate_type=QualifiedName(names=['Conjugate1']),
                     conjugated_type=QualifiedName(names=['Original']), body=[])),
        ('conjugate Conjugate2 ~ Original::X;',
         Conjugation(identification=None, conjugate_type=QualifiedName(names=['Conjugate2']),
                     conjugated_type=QualifiedName(names=['Original', 'X']), body=[])),
    ])
    def test_conjugation(self, text, expected):
        parser = _parser_for_rule('conjugation')
        if isinstance(expected, type) and issubclass(expected, Exception):
            with pytest.raises(expected):
                _ = parser(text)
        else:
            v, rules = parser(text)
            assert v == expected
            assert 'conjugation' in rules

    @pytest.mark.parametrize(['text', 'expected'], [
        ('disjoining Disj disjoint A from B;',
         Disjoining(identification=Identification(short_name=None, name='Disj'),
                    disjoint_type=QualifiedName(names=['A']), separated_type=QualifiedName(names=['B']), body=[])),
        ('disjoining disjoint Mammal from Mineral;',
         Disjoining(identification=Identification(short_name=None, name=None),
                    disjoint_type=QualifiedName(names=['Mammal']), separated_type=QualifiedName(names=['Mineral']),
                    body=[])),
        ('disjoining disjoint Person::parents from Person::children {\n'
         'doc /* No Person can have a parent as a child. */\n'
         '}',
         Disjoining(identification=Identification(short_name=None, name=None),
                    disjoint_type=QualifiedName(names=['Person', 'parents']),
                    separated_type=QualifiedName(names=['Person', 'children']), body=[
                 Documentation(identification=Identification(short_name=None, name=None), locale=None,
                               comment='/* No Person can have a parent as a child. */')])),
        ('disjoint A from B;',
         Disjoining(identification=None, disjoint_type=QualifiedName(names=['A']),
                    separated_type=QualifiedName(names=['B']), body=[])),
        ('disjoint Mammal from Mineral;',
         Disjoining(identification=None, disjoint_type=QualifiedName(names=['Mammal']),
                    separated_type=QualifiedName(names=['Mineral']), body=[])),
        ('disjoint Person::parents from Person::children;',
         Disjoining(identification=None, disjoint_type=QualifiedName(names=['Person', 'parents']),
                    separated_type=QualifiedName(names=['Person', 'children']), body=[])),
    ])
    def test_disjoining(self, text, expected):
        parser = _parser_for_rule('disjoining')
        if isinstance(expected, type) and issubclass(expected, Exception):
            with pytest.raises(expected):
                _ = parser(text)
        else:
            v, rules = parser(text)
            assert v == expected
            assert 'disjoining' in rules

    @pytest.mark.parametrize(['text', 'expected'], [
        ('classifier Person { // Default superclassifier is Base::Anything.\n'
         '    feature age : ScalarValues::Integer;\n'
         '}',
         Classifier(is_abstract=False, annotations=[], is_all=False,
                    identification=Identification(short_name=None, name='Person'), multiplicity_bounds=None,
                    conjugation=None, superclassing=None, relationships=[],
                    body=[OwnedFeatureMember(
                        visibility=None,
                        element=Feature(direction=None, is_abstract=False, relationship_type=None, is_readonly=False,
                                        is_derived=False, is_end=False, annotations=[], is_all=False,
                                        identification=Identification(short_name=None, name='age'),
                                        specializations=[
                                            TypingsPart(items=[QualifiedName(names=['ScalarValues', 'Integer'])])],
                                        multiplicity=None, is_ordered=False, is_nonunique=False, conjugation=None,
                                        relationships=[], is_default=False, value_type=None, value=None, body=[]))])),
        ('classifier Child specializes Person;',
         Classifier(is_abstract=False, annotations=[], is_all=False,
                    identification=Identification(short_name=None, name='Child'), multiplicity_bounds=None,
                    conjugation=None, superclassing=SuperclassingPart(items=[QualifiedName(names=['Person'])]),
                    relationships=[], body=[])),
        ('classifier FuelInPort {\n    in feature fuelFlow : Fuel;\n}',
         Classifier(is_abstract=False, annotations=[], is_all=False,
                    identification=Identification(short_name=None, name='FuelInPort'), multiplicity_bounds=None,
                    conjugation=None, superclassing=None, relationships=[],
                    body=[OwnedFeatureMember(visibility=None, element=Feature(
                        direction=FeatureDirection.IN, is_abstract=False, relationship_type=None,
                        is_readonly=False, is_derived=False, is_end=False, annotations=[], is_all=False,
                        identification=Identification(short_name=None, name='fuelFlow'),
                        specializations=[TypingsPart(items=[QualifiedName(names=['Fuel'])])],
                        multiplicity=None, is_ordered=False, is_nonunique=False, conjugation=None,
                        relationships=[], is_default=False, value_type=None, value=None, body=[]))])),
        ('classifier FuelOutPort conjugates FuelInPort;',
         Classifier(is_abstract=False, annotations=[], is_all=False,
                    identification=Identification(short_name=None, name='FuelOutPort'), multiplicity_bounds=None,
                    conjugation=ConjugationPart(item=QualifiedName(names=['FuelInPort'])), superclassing=None,
                    relationships=[], body=[])),
        ('classifier FuelOutPort ~ FuelInPort;',
         Classifier(is_abstract=False, annotations=[], is_all=False,
                    identification=Identification(short_name=None, name='FuelOutPort'), multiplicity_bounds=None,
                    conjugation=ConjugationPart(item=QualifiedName(names=['FuelInPort'])), superclassing=None,
                    relationships=[], body=[])),
        ('classifier C specializes A, B;',
         Classifier(is_abstract=False, annotations=[], is_all=False,
                    identification=Identification(short_name=None, name='C'), multiplicity_bounds=None,
                    conjugation=None,
                    superclassing=SuperclassingPart(items=[QualifiedName(names=['A']), QualifiedName(names=['B'])]),
                    relationships=[], body=[])),
    ])
    def test_classifier(self, text, expected):
        parser = _parser_for_rule('classifier')
        if isinstance(expected, type) and issubclass(expected, Exception):
            with pytest.raises(expected):
                _ = parser(text)
        else:
            v, rules = parser(text)
            assert v == expected
            assert 'classifier' in rules

    @pytest.mark.parametrize(['text', 'expected'], [
        ("specialization <'+'> Super subclassifier A specializes B;",
         Subclassification(identification=Identification(short_name='+', name='Super'),
                           subclassifier=QualifiedName(names=['A']), superclassifier=QualifiedName(names=['B']),
                           body=[])),
        ('specialization subclassifier B :> A {\n'
         '    /* This subclassification is unnamed. */\n'
         '}',
         Subclassification(identification=Identification(short_name=None, name=None),
                           subclassifier=QualifiedName(names=['B']), superclassifier=QualifiedName(names=['A']), body=[
                 Comment(identification=None, about_list=None, locale=None,
                         comment='/* This subclassification is unnamed. */')])),
        ('subclassifier C specializes A;',
         Subclassification(identification=None, subclassifier=QualifiedName(names=['C']),
                           superclassifier=QualifiedName(names=['A']), body=[])),
    ])
    def test_subclassification(self, text, expected):
        parser = _parser_for_rule('subclassification')
        if isinstance(expected, type) and issubclass(expected, Exception):
            with pytest.raises(expected):
                _ = parser(text)
        else:
            v, rules = parser(text)
            assert v == expected
            assert 'subclassification' in rules

    @pytest.mark.parametrize(['text', 'expected'], [
        ('specialization t1 typing customer typed by Person;',
         FeatureTyping(identification=Identification(short_name=None, name='t1'),
                       typed_entity=QualifiedName(names=['customer']), typing_type=QualifiedName(names=['Person']),
                       body=[])),
        ('specialization t2 typing employer : Organization {\n'
         '    doc /* An employer is an Organization. */\n'
         '}',
         FeatureTyping(identification=Identification(short_name=None, name='t2'),
                       typed_entity=QualifiedName(names=['employer']),
                       typing_type=QualifiedName(names=['Organization']), body=[
                 Documentation(identification=Identification(short_name=None, name=None), locale=None,
                               comment='/* An employer is an Organization. */')])),
        ('typing customer typed by Person;',
         FeatureTyping(identification=None, typed_entity=QualifiedName(names=['customer']),
                       typing_type=QualifiedName(names=['Person']), body=[])),
        ('typing employer : Organization;',
         FeatureTyping(identification=None, typed_entity=QualifiedName(names=['employer']),
                       typing_type=QualifiedName(names=['Organization']), body=[])),
    ])
    def test_feature_typing(self, text, expected):
        parser = _parser_for_rule('feature_typing')
        if isinstance(expected, type) and issubclass(expected, Exception):
            with pytest.raises(expected):
                _ = parser(text)
        else:
            v, rules = parser(text)
            assert v == expected
            assert 'feature_typing' in rules

    @pytest.mark.parametrize(['text', 'expected'], [
        ('specialization Sub subset parent subsets person;',
         Subsetting(identification=Identification(short_name=None, name='Sub'), subset=QualifiedName(names=['parent']),
                    superset=QualifiedName(names=['person']), body=[])),
        ('specialization subset mother subsets parent {\n'
         '    doc /* All mothers are parents. */\n'
         '}',
         Subsetting(identification=Identification(short_name=None, name=None), subset=QualifiedName(names=['mother']),
                    superset=QualifiedName(names=['parent']), body=[
                 Documentation(identification=Identification(short_name=None, name=None), locale=None,
                               comment='/* All mothers are parents. */')])),
        ('subset rearWheels subsets driveWheels;',
         Subsetting(identification=None, subset=QualifiedName(names=['rearWheels']),
                    superset=QualifiedName(names=['driveWheels']), body=[])),
        ('subset rearWheels subsets wheels;',
         Subsetting(identification=None, subset=QualifiedName(names=['rearWheels']),
                    superset=QualifiedName(names=['wheels']), body=[])),
    ])
    def test_subsetting(self, text, expected):
        parser = _parser_for_rule('subsetting')
        if isinstance(expected, type) and issubclass(expected, Exception):
            with pytest.raises(expected):
                _ = parser(text)
        else:
            v, rules = parser(text)
            assert v == expected
            assert 'subsetting' in rules

    @pytest.mark.parametrize(['text', 'expected'], [
        ('specialization Redef redefinition LegalRecord::guardian redefines parent;',
         Redefinition(identification=Identification(short_name=None, name='Redef'),
                      entity=QualifiedName(names=['LegalRecord', 'guardian']),
                      redefined_to=QualifiedName(names=['parent']), body=[])),
        ('specialization redefinition Vehicle::vin redefines '
         'RegisteredAsset::identifier {\n'
         'doc /* A "vin" is a Vehicle Identification Number. */\n'
         '}',
         Redefinition(identification=Identification(short_name=None, name=None),
                      entity=QualifiedName(names=['Vehicle', 'vin']),
                      redefined_to=QualifiedName(names=['RegisteredAsset', 'identifier']), body=[
                 Documentation(identification=Identification(short_name=None, name=None), locale=None,
                               comment='/* A "vin" is a Vehicle Identification Number. */')])),
        ('redefinition Vehicle::vin redefines RegisteredAsset::identifier;',
         Redefinition(identification=None, entity=QualifiedName(names=['Vehicle', 'vin']),
                      redefined_to=QualifiedName(names=['RegisteredAsset', 'identifier']), body=[])),
        ('redefinition Vehicle::vin redefines legalIdentification;',
         Redefinition(identification=None, entity=QualifiedName(names=['Vehicle', 'vin']),
                      redefined_to=QualifiedName(names=['legalIdentification']), body=[])),
    ])
    def test_redefinition(self, text, expected):
        parser = _parser_for_rule('redefinition')
        if isinstance(expected, type) and issubclass(expected, Exception):
            with pytest.raises(expected):
                _ = parser(text)
        else:
            v, rules = parser(text)
            assert v == expected
            assert 'redefinition' in rules

    @pytest.mark.parametrize(['text', 'expected'], [
        ('inverting parent_child inverse Person::parent of Person::child {\n'
         '    doc /* A Person is the parent of their children. */\n'
         '}',
         FeatureInverting(identification=Identification(short_name=None, name='parent_child'),
                          inverted=QualifiedName(names=['Person', 'parent']),
                          target=QualifiedName(names=['Person', 'child']), body=[
                 Documentation(identification=Identification(short_name=None, name=None), locale=None,
                               comment='/* A Person is the parent of their children. */')])),
        ('inverse Person::parents of Person::children;',
         FeatureInverting(identification=None, inverted=QualifiedName(names=['Person', 'parents']),
                          target=QualifiedName(names=['Person', 'children']), body=[])),
    ])
    def test_feature_inverting(self, text, expected):
        parser = _parser_for_rule('feature_inverting')
        if isinstance(expected, type) and issubclass(expected, Exception):
            with pytest.raises(expected):
                _ = parser(text)
        else:
            v, rules = parser(text)
            assert v == expected
            assert 'feature_inverting' in rules

    @pytest.mark.parametrize(['text', 'expected'], [
        ('featuring engine_by_Vehicle of engine featured by Vehicle;',
         TypeFeaturing(identification=Identification(short_name=None, name='engine_by_Vehicle'),
                       featured_entity=QualifiedName(names=['engine']),
                       feature_provider=QualifiedName(names=['Vehicle']), body=[])),
        ('featuring engine_by_Vehicle of engine by Vehicle;',
         TypeFeaturing(identification=Identification(short_name=None, name='engine_by_Vehicle'),
                       featured_entity=QualifiedName(names=['engine']),
                       feature_provider=QualifiedName(names=['Vehicle']), body=[])),
        ('featuring power featured by engine {\n'
         '    doc /* The engine of a Vehicle has power. */\n'
         '}',
         TypeFeaturing(identification=None, featured_entity=QualifiedName(names=['power']),
                       feature_provider=QualifiedName(names=['engine']), body=[
                 Documentation(identification=Identification(short_name=None, name=None), locale=None,
                               comment='/* The engine of a Vehicle has power. */')])),
        ('featuring power by engine {\n'
         '    doc /* The engine of a Vehicle has power. */\n'
         '}',
         TypeFeaturing(identification=None, featured_entity=QualifiedName(names=['power']),
                       feature_provider=QualifiedName(names=['engine']), body=[
                 Documentation(identification=Identification(short_name=None, name=None), locale=None,
                               comment='/* The engine of a Vehicle has power. */')])),
    ])
    def test_type_featuring(self, text, expected):
        parser = _parser_for_rule('type_featuring')
        if isinstance(expected, type) and issubclass(expected, Exception):
            with pytest.raises(expected):
                _ = parser(text)
        else:
            v, rules = parser(text)
            assert v == expected
            assert 'type_featuring' in rules
