import pytest
from lark import UnexpectedInput, GrammarError

from pysysml.kerml.models import Class, Identification, PrefixMetadataAnnotation, SuperclassingPart, \
    MultiplicityBounds, ConjugationPart, DisjoiningPart, UnioningPart, IntersectingPart, DifferencingPart, \
    NonFeatureMember, Documentation, Comment, OwnedFeatureMember, Feature, TypingsPart, DataType, Struct, \
    FeatureRelationshipType, InfValue, Association, AssociationStruct, Connector, ConnectorType, ConnectorEnd, \
    FeatureChain, FeatureValueType, BindingConnector, Succession, Behavior, Step, Function, FeatureDirection, Return, \
    Result, BinOp, Expression, SubsettingsPart, Predicate, BooleanExpression, Invariant, \
    BoolValue, IndexExpression, SequenceExpression, FeatureChainExpression, CollectExpression, SelectExpression, \
    BodyExpression, IfTestOp, ClsTestOp, ClsCastOp, FunctionOperationExpression, UnaryOp, Interaction, ItemFlowEnd, \
    ItemFeature, ItemFlow, MultiplicitySubset, MultiplicityRange, Metaclass, SuccessionItemFlow, MetadataRedefine, \
    Metadata, ElementFilter, CondBinOp, Visibility, Package, Import, LibraryPackage, \
    NullValue, MetadataAccessExpression, QualifiedName, IntValue, StringValue, InvocationExpression, NamedArgument
from .base import _parser_for_rule


@pytest.mark.unittest
class TestKerMLTransformsKernel:
    @pytest.mark.parametrize(['text', 'expected'], [
        ('datatype IdNumber specializes ScalarValues::Integer;',
         DataType(is_abstract=False, annotations=[], is_all=False,
                  identification=Identification(short_name=None, name='IdNumber'), multiplicity_bounds=None,
                  conjugation=None,
                  superclassing=SuperclassingPart(items=[QualifiedName(names=['ScalarValues', 'Integer'])]),
                  relationships=[], body=[])),
        ('datatype Reading { // Subtypes Base::DataValue by default\n'
         '    feature sensorId : IdNumber; // Subsets Base::dataValues by default.\n'
         '    feature value : ScalarValues::Real;\n'
         '}',
         DataType(is_abstract=False, annotations=[], is_all=False,
                  identification=Identification(short_name=None, name='Reading'), multiplicity_bounds=None,
                  conjugation=None, superclassing=None, relationships=[], body=[OwnedFeatureMember(visibility=None,
                                                                                                   element=Feature(
                                                                                                       direction=None,
                                                                                                       is_abstract=False,
                                                                                                       relationship_type=None,
                                                                                                       is_readonly=False,
                                                                                                       is_derived=False,
                                                                                                       is_end=False,
                                                                                                       annotations=[],
                                                                                                       is_all=False,
                                                                                                       identification=Identification(
                                                                                                           short_name=None,
                                                                                                           name='sensorId'),
                                                                                                       specializations=[
                                                                                                           TypingsPart(
                                                                                                               items=[
                                                                                                                   QualifiedName(
                                                                                                                       names=[
                                                                                                                           'IdNumber'])])],
                                                                                                       multiplicity=None,
                                                                                                       is_ordered=False,
                                                                                                       is_nonunique=False,
                                                                                                       conjugation=None,
                                                                                                       relationships=[],
                                                                                                       is_default=False,
                                                                                                       value_type=None,
                                                                                                       value=None,
                                                                                                       body=[])),
                                                                                OwnedFeatureMember(visibility=None,
                                                                                                   element=Feature(
                                                                                                       direction=None,
                                                                                                       is_abstract=False,
                                                                                                       relationship_type=None,
                                                                                                       is_readonly=False,
                                                                                                       is_derived=False,
                                                                                                       is_end=False,
                                                                                                       annotations=[],
                                                                                                       is_all=False,
                                                                                                       identification=Identification(
                                                                                                           short_name=None,
                                                                                                           name='value'),
                                                                                                       specializations=[
                                                                                                           TypingsPart(
                                                                                                               items=[
                                                                                                                   QualifiedName(
                                                                                                                       names=[
                                                                                                                           'ScalarValues',
                                                                                                                           'Real'])])],
                                                                                                       multiplicity=None,
                                                                                                       is_ordered=False,
                                                                                                       is_nonunique=False,
                                                                                                       conjugation=None,
                                                                                                       relationships=[],
                                                                                                       is_default=False,
                                                                                                       value_type=None,
                                                                                                       value=None,
                                                                                                       body=[]))])),
    ])
    def test_data_type(self, text, expected):
        parser = _parser_for_rule('data_type')
        if isinstance(expected, type) and issubclass(expected, Exception):
            with pytest.raises(expected):
                _ = parser(text)
        else:
            v, rules = parser(text)
            assert v == expected
            assert 'data_type' in rules

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
        ('struct Sensor { // Specializes Objects::Object by default.\n'
         '    feature id : IdNumber;\n'
         '    feature currentReading : ScalarValues::Real;\n'
         '}',
         Struct(is_abstract=False, annotations=[], is_all=False,
                identification=Identification(short_name=None, name='Sensor'), multiplicity_bounds=None,
                conjugation=None, superclassing=None, relationships=[], body=[OwnedFeatureMember(visibility=None,
                                                                                                 element=Feature(
                                                                                                     direction=None,
                                                                                                     is_abstract=False,
                                                                                                     relationship_type=None,
                                                                                                     is_readonly=False,
                                                                                                     is_derived=False,
                                                                                                     is_end=False,
                                                                                                     annotations=[],
                                                                                                     is_all=False,
                                                                                                     identification=Identification(
                                                                                                         short_name=None,
                                                                                                         name='id'),
                                                                                                     specializations=[
                                                                                                         TypingsPart(
                                                                                                             items=[
                                                                                                                 QualifiedName(
                                                                                                                     names=[
                                                                                                                         'IdNumber'])])],
                                                                                                     multiplicity=None,
                                                                                                     is_ordered=False,
                                                                                                     is_nonunique=False,
                                                                                                     conjugation=None,
                                                                                                     relationships=[],
                                                                                                     is_default=False,
                                                                                                     value_type=None,
                                                                                                     value=None,
                                                                                                     body=[])),
                                                                              OwnedFeatureMember(visibility=None,
                                                                                                 element=Feature(
                                                                                                     direction=None,
                                                                                                     is_abstract=False,
                                                                                                     relationship_type=None,
                                                                                                     is_readonly=False,
                                                                                                     is_derived=False,
                                                                                                     is_end=False,
                                                                                                     annotations=[],
                                                                                                     is_all=False,
                                                                                                     identification=Identification(
                                                                                                         short_name=None,
                                                                                                         name='currentReading'),
                                                                                                     specializations=[
                                                                                                         TypingsPart(
                                                                                                             items=[
                                                                                                                 QualifiedName(
                                                                                                                     names=[
                                                                                                                         'ScalarValues',
                                                                                                                         'Real'])])],
                                                                                                     multiplicity=None,
                                                                                                     is_ordered=False,
                                                                                                     is_nonunique=False,
                                                                                                     conjugation=None,
                                                                                                     relationships=[],
                                                                                                     is_default=False,
                                                                                                     value_type=None,
                                                                                                     value=None,
                                                                                                     body=[]))])),
        ('struct SensorAssembly specializes Assembly {\n'
         '    composite feature sensors[*] : Sensor; // Subsets Objects::objects by '
         'default.\n'
         '}',
         Struct(is_abstract=False, annotations=[], is_all=False,
                identification=Identification(short_name=None, name='SensorAssembly'), multiplicity_bounds=None,
                conjugation=None, superclassing=SuperclassingPart(items=[QualifiedName(names=['Assembly'])]),
                relationships=[], body=[OwnedFeatureMember(visibility=None,
                                                           element=Feature(direction=None, is_abstract=False,
                                                                           relationship_type=FeatureRelationshipType.COMPOSITE,
                                                                           is_readonly=False, is_derived=False,
                                                                           is_end=False, annotations=[], is_all=False,
                                                                           identification=Identification(
                                                                               short_name=None, name='sensors'),
                                                                           specializations=[TypingsPart(items=[
                                                                               QualifiedName(names=['Sensor'])])],
                                                                           multiplicity=MultiplicityBounds(
                                                                               lower_bound=None,
                                                                               upper_bound=InfValue()),
                                                                           is_ordered=False, is_nonunique=False,
                                                                           conjugation=None, relationships=[],
                                                                           is_default=False, value_type=None,
                                                                           value=None, body=[]))])),
    ])
    def test_structure(self, text, expected):
        parser = _parser_for_rule('structure')
        if isinstance(expected, type) and issubclass(expected, Exception):
            with pytest.raises(expected):
                _ = parser(text)
        else:
            v, rules = parser(text)
            assert v == expected
            assert 'structure' in rules

    @pytest.mark.parametrize(['text', 'expected'], [
        ('assoc Ownership { // Specializes Links::BinaryLink by default.\n'
         '    feature valuationOnPurchase : MonetaryValue;\n'
         '    end feature owner[1..*] : LegalEntity; // Redefines BinaryLink::source.\n'
         '    end feature ownedAsset[*] : Asset; // Redefines BinaryLink::target.\n'
         '}',
         Association(is_abstract=False, annotations=[], is_all=False,
                     identification=Identification(short_name=None, name='Ownership'), multiplicity_bounds=None,
                     conjugation=None, superclassing=None, relationships=[], body=[OwnedFeatureMember(visibility=None,
                                                                                                      element=Feature(
                                                                                                          direction=None,
                                                                                                          is_abstract=False,
                                                                                                          relationship_type=None,
                                                                                                          is_readonly=False,
                                                                                                          is_derived=False,
                                                                                                          is_end=False,
                                                                                                          annotations=[],
                                                                                                          is_all=False,
                                                                                                          identification=Identification(
                                                                                                              short_name=None,
                                                                                                              name='valuationOnPurchase'),
                                                                                                          specializations=[
                                                                                                              TypingsPart(
                                                                                                                  items=[
                                                                                                                      QualifiedName(
                                                                                                                          names=[
                                                                                                                              'MonetaryValue'])])],
                                                                                                          multiplicity=None,
                                                                                                          is_ordered=False,
                                                                                                          is_nonunique=False,
                                                                                                          conjugation=None,
                                                                                                          relationships=[],
                                                                                                          is_default=False,
                                                                                                          value_type=None,
                                                                                                          value=None,
                                                                                                          body=[])),
                                                                                   OwnedFeatureMember(visibility=None,
                                                                                                      element=Feature(
                                                                                                          direction=None,
                                                                                                          is_abstract=False,
                                                                                                          relationship_type=None,
                                                                                                          is_readonly=False,
                                                                                                          is_derived=False,
                                                                                                          is_end=True,
                                                                                                          annotations=[],
                                                                                                          is_all=False,
                                                                                                          identification=Identification(
                                                                                                              short_name=None,
                                                                                                              name='owner'),
                                                                                                          specializations=[
                                                                                                              TypingsPart(
                                                                                                                  items=[
                                                                                                                      QualifiedName(
                                                                                                                          names=[
                                                                                                                              'LegalEntity'])])],
                                                                                                          multiplicity=MultiplicityBounds(
                                                                                                              lower_bound=IntValue(
                                                                                                                  raw='1'),
                                                                                                              upper_bound=InfValue()),
                                                                                                          is_ordered=False,
                                                                                                          is_nonunique=False,
                                                                                                          conjugation=None,
                                                                                                          relationships=[],
                                                                                                          is_default=False,
                                                                                                          value_type=None,
                                                                                                          value=None,
                                                                                                          body=[])),
                                                                                   OwnedFeatureMember(visibility=None,
                                                                                                      element=Feature(
                                                                                                          direction=None,
                                                                                                          is_abstract=False,
                                                                                                          relationship_type=None,
                                                                                                          is_readonly=False,
                                                                                                          is_derived=False,
                                                                                                          is_end=True,
                                                                                                          annotations=[],
                                                                                                          is_all=False,
                                                                                                          identification=Identification(
                                                                                                              short_name=None,
                                                                                                              name='ownedAsset'),
                                                                                                          specializations=[
                                                                                                              TypingsPart(
                                                                                                                  items=[
                                                                                                                      QualifiedName(
                                                                                                                          names=[
                                                                                                                              'Asset'])])],
                                                                                                          multiplicity=MultiplicityBounds(
                                                                                                              lower_bound=None,
                                                                                                              upper_bound=InfValue()),
                                                                                                          is_ordered=False,
                                                                                                          is_nonunique=False,
                                                                                                          conjugation=None,
                                                                                                          relationships=[],
                                                                                                          is_default=False,
                                                                                                          value_type=None,
                                                                                                          value=None,
                                                                                                          body=[]))])),
        ('assoc SoleOwnership specializes Ownership {\n'
         '    end feature owner[1]; // Redefines Ownership::owner.\n'
         '    // ownedAsset is inherited.\n'
         '}',
         Association(is_abstract=False, annotations=[], is_all=False,
                     identification=Identification(short_name=None, name='SoleOwnership'), multiplicity_bounds=None,
                     conjugation=None, superclassing=SuperclassingPart(items=[QualifiedName(names=['Ownership'])]),
                     relationships=[], body=[OwnedFeatureMember(visibility=None,
                                                                element=Feature(direction=None, is_abstract=False,
                                                                                relationship_type=None,
                                                                                is_readonly=False, is_derived=False,
                                                                                is_end=True, annotations=[],
                                                                                is_all=False,
                                                                                identification=Identification(
                                                                                    short_name=None, name='owner'),
                                                                                specializations=[],
                                                                                multiplicity=MultiplicityBounds(
                                                                                    lower_bound=None,
                                                                                    upper_bound=IntValue(raw='1')),
                                                                                is_ordered=False, is_nonunique=False,
                                                                                conjugation=None, relationships=[],
                                                                                is_default=False, value_type=None,
                                                                                value=None, body=[]))])),
    ])
    def test_association(self, text, expected):
        parser = _parser_for_rule('association')
        if isinstance(expected, type) and issubclass(expected, Exception):
            with pytest.raises(expected):
                _ = parser(text)
        else:
            v, rules = parser(text)
            assert v == expected
            assert 'association' in rules

    @pytest.mark.parametrize(['text', 'expected'], [
        ('assoc struct ExtendedOwnership specializes Ownership {\n'
         '    // End features are inherited from Ownership.\n'
         '    // The values of the feature "revaluations" may change over time.\n'
         '    feature revaluations[*] ordered : MonetaryValue;\n'
         '}',
         AssociationStruct(is_abstract=False, annotations=[], is_all=False,
                           identification=Identification(short_name=None, name='ExtendedOwnership'),
                           multiplicity_bounds=None, conjugation=None,
                           superclassing=SuperclassingPart(items=[QualifiedName(names=['Ownership'])]),
                           relationships=[], body=[OwnedFeatureMember(visibility=None,
                                                                      element=Feature(direction=None, is_abstract=False,
                                                                                      relationship_type=None,
                                                                                      is_readonly=False,
                                                                                      is_derived=False, is_end=False,
                                                                                      annotations=[], is_all=False,
                                                                                      identification=Identification(
                                                                                          short_name=None,
                                                                                          name='revaluations'),
                                                                                      specializations=[TypingsPart(
                                                                                          items=[QualifiedName(names=[
                                                                                              'MonetaryValue'])])],
                                                                                      multiplicity=MultiplicityBounds(
                                                                                          lower_bound=None,
                                                                                          upper_bound=InfValue()),
                                                                                      is_ordered=True,
                                                                                      is_nonunique=False,
                                                                                      conjugation=None,
                                                                                      relationships=[],
                                                                                      is_default=False, value_type=None,
                                                                                      value=None, body=[]))])),
    ])
    def test_association_structure(self, text, expected):
        parser = _parser_for_rule('association_structure')
        if isinstance(expected, type) and issubclass(expected, Exception):
            with pytest.raises(expected):
                _ = parser(text)
        else:
            v, rules = parser(text)
            assert v == expected
            assert 'association_structure' in rules

    @pytest.mark.parametrize(['text', 'expected'], [
        ('connector mount : Mounting from axle to wheels;',
         Connector(direction=None, is_abstract=False, relationship_type=None, is_readonly=False, is_derived=False,
                   is_end=False, annotations=[], is_all=False,
                   identification=Identification(short_name=None, name='mount'),
                   specializations=[TypingsPart(items=[QualifiedName(names=['Mounting'])])], multiplicity=None,
                   is_ordered=False, is_nonunique=False, conjugation=None, relationships=[], type=ConnectorType.BINARY,
                   is_default=False, value_type=None, value=None, is_all_connect=False,
                   ends=[ConnectorEnd(name=None, reference=QualifiedName(names=['axle']), multiplicity=None),
                         ConnectorEnd(name=None, reference=QualifiedName(names=['wheels']), multiplicity=None)],
                   body=[])),
        ('connector mount[2] : Mounting (axle, wheels);',
         Connector(direction=None, is_abstract=False, relationship_type=None, is_readonly=False, is_derived=False,
                   is_end=False, annotations=[], is_all=False,
                   identification=Identification(short_name=None, name='mount'),
                   specializations=[TypingsPart(items=[QualifiedName(names=['Mounting'])])],
                   multiplicity=MultiplicityBounds(lower_bound=None, upper_bound=IntValue(raw='2')), is_ordered=False,
                   is_nonunique=False, conjugation=None, relationships=[], type=ConnectorType.NARY, is_default=False,
                   value_type=None, value=None, is_all_connect=False,
                   ends=[ConnectorEnd(name=None, reference=QualifiedName(names=['axle']), multiplicity=None),
                         ConnectorEnd(name=None, reference=QualifiedName(names=['wheels']), multiplicity=None)],
                   body=[])),
        ('connector mount[2] : Mounting (\n'
         '    mountingAxle ::> axle,\n'
         '    mountedWheel ::> wheels\n'
         ');',
         Connector(direction=None, is_abstract=False, relationship_type=None, is_readonly=False, is_derived=False,
                   is_end=False, annotations=[], is_all=False,
                   identification=Identification(short_name=None, name='mount'),
                   specializations=[TypingsPart(items=[QualifiedName(names=['Mounting'])])],
                   multiplicity=MultiplicityBounds(lower_bound=None, upper_bound=IntValue(raw='2')), is_ordered=False,
                   is_nonunique=False, conjugation=None, relationships=[], type=ConnectorType.NARY, is_default=False,
                   value_type=None, value=None, is_all_connect=False,
                   ends=[ConnectorEnd(name='mountingAxle', reference=QualifiedName(names=['axle']), multiplicity=None),
                         ConnectorEnd(name='mountedWheel', reference=QualifiedName(names=['wheels']),
                                      multiplicity=None)], body=[])),
        ('connector mount : Mounting from halfAxles[1] to wheels[1];',
         Connector(direction=None, is_abstract=False, relationship_type=None, is_readonly=False, is_derived=False,
                   is_end=False, annotations=[], is_all=False,
                   identification=Identification(short_name=None, name='mount'),
                   specializations=[TypingsPart(items=[QualifiedName(names=['Mounting'])])], multiplicity=None,
                   is_ordered=False, is_nonunique=False, conjugation=None, relationships=[], type=ConnectorType.BINARY,
                   is_default=False, value_type=None, value=None, is_all_connect=False, ends=[
                 ConnectorEnd(name=None, reference=QualifiedName(names=['halfAxles']),
                              multiplicity=MultiplicityBounds(lower_bound=None, upper_bound=IntValue(raw='1'))),
                 ConnectorEnd(name=None, reference=QualifiedName(names=['wheels']),
                              multiplicity=MultiplicityBounds(lower_bound=None, upper_bound=IntValue(raw='1')))],
                   body=[])),
        ('connector mount[2] : Mounting from mountingAxle ::> axle to mountedWheel ::> '
         'wheels;',
         Connector(direction=None, is_abstract=False, relationship_type=None, is_readonly=False, is_derived=False,
                   is_end=False, annotations=[], is_all=False,
                   identification=Identification(short_name=None, name='mount'),
                   specializations=[TypingsPart(items=[QualifiedName(names=['Mounting'])])],
                   multiplicity=MultiplicityBounds(lower_bound=None, upper_bound=IntValue(raw='2')), is_ordered=False,
                   is_nonunique=False, conjugation=None, relationships=[], type=ConnectorType.BINARY, is_default=False,
                   value_type=None, value=None, is_all_connect=False,
                   ends=[ConnectorEnd(name='mountingAxle', reference=QualifiedName(names=['axle']), multiplicity=None),
                         ConnectorEnd(name='mountedWheel', reference=QualifiedName(names=['wheels']),
                                      multiplicity=None)], body=[])),
        ('connector mount : Mounting from axle.halfAxles to wheels.hub;',
         Connector(direction=None, is_abstract=False, relationship_type=None, is_readonly=False, is_derived=False,
                   is_end=False, annotations=[], is_all=False,
                   identification=Identification(short_name=None, name='mount'),
                   specializations=[TypingsPart(items=[QualifiedName(names=['Mounting'])])], multiplicity=None,
                   is_ordered=False, is_nonunique=False, conjugation=None, relationships=[], type=ConnectorType.BINARY,
                   is_default=False, value_type=None, value=None, is_all_connect=False,
                   ends=[ConnectorEnd(name=None, reference=FeatureChain(
                       items=[QualifiedName(names=['axle']), QualifiedName(names=['halfAxles'])]), multiplicity=None),
                         ConnectorEnd(name=None, reference=FeatureChain(
                             items=[QualifiedName(names=['wheels']), QualifiedName(names=['hub'])]),
                                      multiplicity=None)],
                   body=[])),
        ('abstract connector all from axle to wheels;',
         Connector(direction=None, is_abstract=True, relationship_type=None, is_readonly=False, is_derived=False,
                   is_end=False, annotations=[], is_all=False, identification=None, specializations=[],
                   multiplicity=None, is_ordered=False, is_nonunique=False, conjugation=None, relationships=[],
                   type=ConnectorType.BINARY, is_default=False, value_type=None, value=None, is_all_connect=True,
                   ends=[ConnectorEnd(name=None, reference=QualifiedName(names=['axle']), multiplicity=None),
                         ConnectorEnd(name=None, reference=QualifiedName(names=['wheels']), multiplicity=None)],
                   body=[])),
        ('derived connector mounting : Mounting := another_mounting;',
         Connector(direction=None, is_abstract=False, relationship_type=None, is_readonly=False, is_derived=True,
                   is_end=False, annotations=[], is_all=False,
                   identification=Identification(short_name=None, name='mounting'),
                   specializations=[TypingsPart(items=[QualifiedName(names=['Mounting'])])], multiplicity=None,
                   is_ordered=False, is_nonunique=False, conjugation=None, relationships=[], type=ConnectorType.VALUE,
                   is_default=False, value_type=FeatureValueType.INITIAL,
                   value=QualifiedName(names=['another_mounting']), is_all_connect=False, ends=None, body=[])),
        ('connector transitionLink[0..1] to trigger[1..*];',
         Connector(direction=None, is_abstract=False, relationship_type=None, is_readonly=False, is_derived=False,
                   is_end=False, annotations=[], is_all=False, identification=None, specializations=[],
                   multiplicity=None, is_ordered=False, is_nonunique=False, conjugation=None, relationships=[],
                   type=ConnectorType.BINARY, is_default=False, value_type=None, value=None, is_all_connect=False,
                   ends=[ConnectorEnd(name=None, reference=QualifiedName(names=['transitionLink']),
                                      multiplicity=MultiplicityBounds(lower_bound=IntValue(raw='0'),
                                                                      upper_bound=IntValue(raw='1'))),
                         ConnectorEnd(name=None, reference=QualifiedName(names=['trigger']),
                                      multiplicity=MultiplicityBounds(lower_bound=IntValue(raw='1'),
                                                                      upper_bound=InfValue()))], body=[])),
        ('connector all guardConstraint: TPCGuardConstraint[*]\n'
         'from transitionLink[0..1] to guard[*];',
         Connector(direction=None, is_abstract=False, relationship_type=None, is_readonly=False, is_derived=False,
                   is_end=False, annotations=[], is_all=True,
                   identification=Identification(short_name=None, name='guardConstraint'),
                   specializations=[TypingsPart(items=[QualifiedName(names=['TPCGuardConstraint'])])],
                   multiplicity=MultiplicityBounds(lower_bound=None, upper_bound=InfValue()), is_ordered=False,
                   is_nonunique=False, conjugation=None, relationships=[], type=ConnectorType.BINARY, is_default=False,
                   value_type=None, value=None, is_all_connect=False, ends=[
                 ConnectorEnd(name=None, reference=QualifiedName(names=['transitionLink']),
                              multiplicity=MultiplicityBounds(lower_bound=IntValue(raw='0'),
                                                              upper_bound=IntValue(raw='1'))),
                 ConnectorEnd(name=None, reference=QualifiedName(names=['guard']),
                              multiplicity=MultiplicityBounds(lower_bound=None, upper_bound=InfValue()))], body=[])),
    ])
    def test_connector(self, text, expected):
        parser = _parser_for_rule('connector')
        if isinstance(expected, type) and issubclass(expected, Exception):
            with pytest.raises(expected):
                _ = parser(text)
        else:
            v, rules = parser(text)
            assert v == expected
            assert 'connector' in rules

    @pytest.mark.parametrize(['text', 'expected'], [
        ('// Subsets Links::selfLinks by default.\n'
         'binding fuelFlowBinding of fuelTank.fuelFlowOut = engine.fuelFlowIn;',
         BindingConnector(direction=None, is_abstract=False, relationship_type=None, is_readonly=False,
                          is_derived=False, is_end=False, annotations=[], is_all=False,
                          identification=Identification(short_name=None, name='fuelFlowBinding'), specializations=[],
                          multiplicity=None, is_ordered=False, is_nonunique=False, conjugation=None, relationships=[],
                          is_all_binding=False, bind_entity=ConnectorEnd(name=None, reference=FeatureChain(
                 items=[QualifiedName(names=['fuelTank']), QualifiedName(names=['fuelFlowOut'])]), multiplicity=None),
                          bind_to=ConnectorEnd(name=None, reference=FeatureChain(
                              items=[QualifiedName(names=['engine']), QualifiedName(names=['fuelFlowIn'])]),
                                               multiplicity=None), body=[])),
        ('binding fuelTank.fuelFlowOut = engine.fuelFlowIn;',
         BindingConnector(direction=None, is_abstract=False, relationship_type=None, is_readonly=False,
                          is_derived=False, is_end=False, annotations=[], is_all=False, identification=None,
                          specializations=[], multiplicity=None, is_ordered=False, is_nonunique=False, conjugation=None,
                          relationships=[], is_all_binding=False, bind_entity=ConnectorEnd(name=None,
                                                                                           reference=FeatureChain(
                                                                                               items=[QualifiedName(
                                                                                                   names=['fuelTank']),
                                                                                                   QualifiedName(
                                                                                                       names=[
                                                                                                           'fuelFlowOut'])]),
                                                                                           multiplicity=None),
                          bind_to=ConnectorEnd(name=None, reference=FeatureChain(
                              items=[QualifiedName(names=['engine']), QualifiedName(names=['fuelFlowIn'])]),
                                               multiplicity=None), body=[])),
        ('binding x;',
         BindingConnector(direction=None, is_abstract=False, relationship_type=None, is_readonly=False,
                          is_derived=False, is_end=False, annotations=[], is_all=False,
                          identification=Identification(short_name=None, name='x'), specializations=[],
                          multiplicity=None, is_ordered=False, is_nonunique=False, conjugation=None, relationships=[],
                          is_all_binding=False, bind_entity=None, bind_to=None, body=[])),
        ('binding all;',
         BindingConnector(direction=None, is_abstract=False, relationship_type=None, is_readonly=False,
                          is_derived=False, is_end=False, annotations=[], is_all=False, identification=None,
                          specializations=[], multiplicity=None, is_ordered=False, is_nonunique=False, conjugation=None,
                          relationships=[], is_all_binding=True, bind_entity=None, bind_to=None, body=[])),
    ])
    def test_binding_connector(self, text, expected):
        parser = _parser_for_rule('binding_connector')
        if isinstance(expected, type) and issubclass(expected, Exception):
            with pytest.raises(expected):
                _ = parser(text)
        else:
            v, rules = parser(text)
            assert v == expected
            assert 'binding_connector' in rules

    @pytest.mark.parametrize(['text', 'expected'], [
        ('succession controlFlow first focus then shoot;',
         Succession(direction=None, is_abstract=False, relationship_type=None, is_readonly=False, is_derived=False,
                    is_end=False, annotations=[], is_all=False,
                    identification=Identification(short_name=None, name='controlFlow'), specializations=[],
                    multiplicity=None, is_ordered=False, is_nonunique=False, conjugation=None, relationships=[],
                    is_all_succession=False,
                    first=ConnectorEnd(name=None, reference=QualifiedName(names=['focus']), multiplicity=None),
                    then=ConnectorEnd(name=None, reference=QualifiedName(names=['shoot']), multiplicity=None),
                    body=[])),
        ('succession focus then shoot;',
         Succession(direction=None, is_abstract=False, relationship_type=None, is_readonly=False, is_derived=False,
                    is_end=False, annotations=[], is_all=False, identification=None, specializations=[],
                    multiplicity=None, is_ordered=False, is_nonunique=False, conjugation=None, relationships=[],
                    is_all_succession=False,
                    first=ConnectorEnd(name=None, reference=QualifiedName(names=['focus']), multiplicity=None),
                    then=ConnectorEnd(name=None, reference=QualifiedName(names=['shoot']), multiplicity=None),
                    body=[])),
        ('succession focus[0..1] then focus[0..1];',
         Succession(direction=None, is_abstract=False, relationship_type=None, is_readonly=False, is_derived=False,
                    is_end=False, annotations=[], is_all=False, identification=None, specializations=[],
                    multiplicity=None, is_ordered=False, is_nonunique=False, conjugation=None, relationships=[],
                    is_all_succession=False, first=ConnectorEnd(name=None, reference=QualifiedName(names=['focus']),
                                                                multiplicity=MultiplicityBounds(
                                                                    lower_bound=IntValue(raw='0'),
                                                                    upper_bound=IntValue(raw='1'))),
                    then=ConnectorEnd(name=None, reference=QualifiedName(names=['focus']),
                                      multiplicity=MultiplicityBounds(lower_bound=IntValue(raw='0'),
                                                                      upper_bound=IntValue(raw='1'))), body=[])),
        ('succession focus[1] then shoot[0..1];',
         Succession(direction=None, is_abstract=False, relationship_type=None, is_readonly=False, is_derived=False,
                    is_end=False, annotations=[], is_all=False, identification=None, specializations=[],
                    multiplicity=None, is_ordered=False, is_nonunique=False, conjugation=None, relationships=[],
                    is_all_succession=False, first=ConnectorEnd(name=None, reference=QualifiedName(names=['focus']),
                                                                multiplicity=MultiplicityBounds(lower_bound=None,
                                                                                                upper_bound=IntValue(
                                                                                                    raw='1'))),
                    then=ConnectorEnd(name=None, reference=QualifiedName(names=['shoot']),
                                      multiplicity=MultiplicityBounds(lower_bound=IntValue(raw='0'),
                                                                      upper_bound=IntValue(raw='1'))), body=[])),
        ('succession x;',
         Succession(direction=None, is_abstract=False, relationship_type=None, is_readonly=False, is_derived=False,
                    is_end=False, annotations=[], is_all=False,
                    identification=Identification(short_name=None, name='x'), specializations=[], multiplicity=None,
                    is_ordered=False, is_nonunique=False, conjugation=None, relationships=[], is_all_succession=False,
                    first=None, then=None, body=[])),
        ('succession all;',
         Succession(direction=None, is_abstract=False, relationship_type=None, is_readonly=False, is_derived=False,
                    is_end=False, annotations=[], is_all=False, identification=None, specializations=[],
                    multiplicity=None, is_ordered=False, is_nonunique=False, conjugation=None, relationships=[],
                    is_all_succession=True, first=None, then=None, body=[])),
    ])
    def test_succession(self, text, expected):
        parser = _parser_for_rule('succession')
        if isinstance(expected, type) and issubclass(expected, Exception):
            with pytest.raises(expected):
                _ = parser(text)
        else:
            v, rules = parser(text)
            assert v == expected
            assert 'succession' in rules

    @pytest.mark.parametrize(['text', 'expected'], [
        ('behavior TakePicture {\n'
         '    composite step focus : Focus;\n'
         '    composite step shoot : Shoot;\n'
         '    succession controlFlow first focus then shoot;\n'
         '}',
         Behavior(is_abstract=False, annotations=[], is_all=False,
                  identification=Identification(short_name=None, name='TakePicture'), multiplicity_bounds=None,
                  conjugation=None, superclassing=None, relationships=[], body=[OwnedFeatureMember(visibility=None,
                                                                                                   element=Step(
                                                                                                       direction=None,
                                                                                                       is_abstract=False,
                                                                                                       relationship_type=FeatureRelationshipType.COMPOSITE,
                                                                                                       is_readonly=False,
                                                                                                       is_derived=False,
                                                                                                       is_end=False,
                                                                                                       annotations=[],
                                                                                                       is_all=False,
                                                                                                       identification=Identification(
                                                                                                           short_name=None,
                                                                                                           name='focus'),
                                                                                                       specializations=[
                                                                                                           TypingsPart(
                                                                                                               items=[
                                                                                                                   QualifiedName(
                                                                                                                       names=[
                                                                                                                           'Focus'])])],
                                                                                                       multiplicity=None,
                                                                                                       is_ordered=False,
                                                                                                       is_nonunique=False,
                                                                                                       conjugation=None,
                                                                                                       relationships=[],
                                                                                                       is_default=False,
                                                                                                       value_type=None,
                                                                                                       value=None,
                                                                                                       body=[])),
                                                                                OwnedFeatureMember(visibility=None,
                                                                                                   element=Step(
                                                                                                       direction=None,
                                                                                                       is_abstract=False,
                                                                                                       relationship_type=FeatureRelationshipType.COMPOSITE,
                                                                                                       is_readonly=False,
                                                                                                       is_derived=False,
                                                                                                       is_end=False,
                                                                                                       annotations=[],
                                                                                                       is_all=False,
                                                                                                       identification=Identification(
                                                                                                           short_name=None,
                                                                                                           name='shoot'),
                                                                                                       specializations=[
                                                                                                           TypingsPart(
                                                                                                               items=[
                                                                                                                   QualifiedName(
                                                                                                                       names=[
                                                                                                                           'Shoot'])])],
                                                                                                       multiplicity=None,
                                                                                                       is_ordered=False,
                                                                                                       is_nonunique=False,
                                                                                                       conjugation=None,
                                                                                                       relationships=[],
                                                                                                       is_default=False,
                                                                                                       value_type=None,
                                                                                                       value=None,
                                                                                                       body=[])),
                                                                                OwnedFeatureMember(visibility=None,
                                                                                                   element=Succession(
                                                                                                       direction=None,
                                                                                                       is_abstract=False,
                                                                                                       relationship_type=None,
                                                                                                       is_readonly=False,
                                                                                                       is_derived=False,
                                                                                                       is_end=False,
                                                                                                       annotations=[],
                                                                                                       is_all=False,
                                                                                                       identification=Identification(
                                                                                                           short_name=None,
                                                                                                           name='controlFlow'),
                                                                                                       specializations=[],
                                                                                                       multiplicity=None,
                                                                                                       is_ordered=False,
                                                                                                       is_nonunique=False,
                                                                                                       conjugation=None,
                                                                                                       relationships=[],
                                                                                                       is_all_succession=False,
                                                                                                       first=ConnectorEnd(
                                                                                                           name=None,
                                                                                                           reference=QualifiedName(
                                                                                                               names=[
                                                                                                                   'focus']),
                                                                                                           multiplicity=None),
                                                                                                       then=ConnectorEnd(
                                                                                                           name=None,
                                                                                                           reference=QualifiedName(
                                                                                                               names=[
                                                                                                                   'shoot']),
                                                                                                           multiplicity=None),
                                                                                                       body=[]))])),
        ('behavior TakePicture {\n'
         '    composite step focus : Focus;\n'
         '    composite step shoot : Shoot;\n'
         '    succession focus then shoot;\n'
         '}',
         Behavior(is_abstract=False, annotations=[], is_all=False,
                  identification=Identification(short_name=None, name='TakePicture'), multiplicity_bounds=None,
                  conjugation=None, superclassing=None, relationships=[], body=[OwnedFeatureMember(visibility=None,
                                                                                                   element=Step(
                                                                                                       direction=None,
                                                                                                       is_abstract=False,
                                                                                                       relationship_type=FeatureRelationshipType.COMPOSITE,
                                                                                                       is_readonly=False,
                                                                                                       is_derived=False,
                                                                                                       is_end=False,
                                                                                                       annotations=[],
                                                                                                       is_all=False,
                                                                                                       identification=Identification(
                                                                                                           short_name=None,
                                                                                                           name='focus'),
                                                                                                       specializations=[
                                                                                                           TypingsPart(
                                                                                                               items=[
                                                                                                                   QualifiedName(
                                                                                                                       names=[
                                                                                                                           'Focus'])])],
                                                                                                       multiplicity=None,
                                                                                                       is_ordered=False,
                                                                                                       is_nonunique=False,
                                                                                                       conjugation=None,
                                                                                                       relationships=[],
                                                                                                       is_default=False,
                                                                                                       value_type=None,
                                                                                                       value=None,
                                                                                                       body=[])),
                                                                                OwnedFeatureMember(visibility=None,
                                                                                                   element=Step(
                                                                                                       direction=None,
                                                                                                       is_abstract=False,
                                                                                                       relationship_type=FeatureRelationshipType.COMPOSITE,
                                                                                                       is_readonly=False,
                                                                                                       is_derived=False,
                                                                                                       is_end=False,
                                                                                                       annotations=[],
                                                                                                       is_all=False,
                                                                                                       identification=Identification(
                                                                                                           short_name=None,
                                                                                                           name='shoot'),
                                                                                                       specializations=[
                                                                                                           TypingsPart(
                                                                                                               items=[
                                                                                                                   QualifiedName(
                                                                                                                       names=[
                                                                                                                           'Shoot'])])],
                                                                                                       multiplicity=None,
                                                                                                       is_ordered=False,
                                                                                                       is_nonunique=False,
                                                                                                       conjugation=None,
                                                                                                       relationships=[],
                                                                                                       is_default=False,
                                                                                                       value_type=None,
                                                                                                       value=None,
                                                                                                       body=[])),
                                                                                OwnedFeatureMember(visibility=None,
                                                                                                   element=Succession(
                                                                                                       direction=None,
                                                                                                       is_abstract=False,
                                                                                                       relationship_type=None,
                                                                                                       is_readonly=False,
                                                                                                       is_derived=False,
                                                                                                       is_end=False,
                                                                                                       annotations=[],
                                                                                                       is_all=False,
                                                                                                       identification=None,
                                                                                                       specializations=[],
                                                                                                       multiplicity=None,
                                                                                                       is_ordered=False,
                                                                                                       is_nonunique=False,
                                                                                                       conjugation=None,
                                                                                                       relationships=[],
                                                                                                       is_all_succession=False,
                                                                                                       first=ConnectorEnd(
                                                                                                           name=None,
                                                                                                           reference=QualifiedName(
                                                                                                               names=[
                                                                                                                   'focus']),
                                                                                                           multiplicity=None),
                                                                                                       then=ConnectorEnd(
                                                                                                           name=None,
                                                                                                           reference=QualifiedName(
                                                                                                               names=[
                                                                                                                   'shoot']),
                                                                                                           multiplicity=None),
                                                                                                       body=[]))])),
        ('behavior TakePicture {\n'
         '    composite step focus[*] : Focus;\n'
         '    composite step shoot[1] : Shoot;\n'
         '    // A focus may be preceded by a previous focus.\n'
         '    succession focus[0..1] then focus[0..1];\n'
         '    // A shoot must follow a focus.\n'
         '    succession focus[1] then shoot[0..1];\n'
         '}',
         Behavior(is_abstract=False, annotations=[], is_all=False,
                  identification=Identification(short_name=None, name='TakePicture'), multiplicity_bounds=None,
                  conjugation=None, superclassing=None, relationships=[], body=[OwnedFeatureMember(visibility=None,
                                                                                                   element=Step(
                                                                                                       direction=None,
                                                                                                       is_abstract=False,
                                                                                                       relationship_type=FeatureRelationshipType.COMPOSITE,
                                                                                                       is_readonly=False,
                                                                                                       is_derived=False,
                                                                                                       is_end=False,
                                                                                                       annotations=[],
                                                                                                       is_all=False,
                                                                                                       identification=Identification(
                                                                                                           short_name=None,
                                                                                                           name='focus'),
                                                                                                       specializations=[
                                                                                                           TypingsPart(
                                                                                                               items=[
                                                                                                                   QualifiedName(
                                                                                                                       names=[
                                                                                                                           'Focus'])])],
                                                                                                       multiplicity=MultiplicityBounds(
                                                                                                           lower_bound=None,
                                                                                                           upper_bound=InfValue()),
                                                                                                       is_ordered=False,
                                                                                                       is_nonunique=False,
                                                                                                       conjugation=None,
                                                                                                       relationships=[],
                                                                                                       is_default=False,
                                                                                                       value_type=None,
                                                                                                       value=None,
                                                                                                       body=[])),
                                                                                OwnedFeatureMember(visibility=None,
                                                                                                   element=Step(
                                                                                                       direction=None,
                                                                                                       is_abstract=False,
                                                                                                       relationship_type=FeatureRelationshipType.COMPOSITE,
                                                                                                       is_readonly=False,
                                                                                                       is_derived=False,
                                                                                                       is_end=False,
                                                                                                       annotations=[],
                                                                                                       is_all=False,
                                                                                                       identification=Identification(
                                                                                                           short_name=None,
                                                                                                           name='shoot'),
                                                                                                       specializations=[
                                                                                                           TypingsPart(
                                                                                                               items=[
                                                                                                                   QualifiedName(
                                                                                                                       names=[
                                                                                                                           'Shoot'])])],
                                                                                                       multiplicity=MultiplicityBounds(
                                                                                                           lower_bound=None,
                                                                                                           upper_bound=IntValue(
                                                                                                               raw='1')),
                                                                                                       is_ordered=False,
                                                                                                       is_nonunique=False,
                                                                                                       conjugation=None,
                                                                                                       relationships=[],
                                                                                                       is_default=False,
                                                                                                       value_type=None,
                                                                                                       value=None,
                                                                                                       body=[])),
                                                                                OwnedFeatureMember(visibility=None,
                                                                                                   element=Succession(
                                                                                                       direction=None,
                                                                                                       is_abstract=False,
                                                                                                       relationship_type=None,
                                                                                                       is_readonly=False,
                                                                                                       is_derived=False,
                                                                                                       is_end=False,
                                                                                                       annotations=[],
                                                                                                       is_all=False,
                                                                                                       identification=None,
                                                                                                       specializations=[],
                                                                                                       multiplicity=None,
                                                                                                       is_ordered=False,
                                                                                                       is_nonunique=False,
                                                                                                       conjugation=None,
                                                                                                       relationships=[],
                                                                                                       is_all_succession=False,
                                                                                                       first=ConnectorEnd(
                                                                                                           name=None,
                                                                                                           reference=QualifiedName(
                                                                                                               names=[
                                                                                                                   'focus']),
                                                                                                           multiplicity=MultiplicityBounds(
                                                                                                               lower_bound=IntValue(
                                                                                                                   raw='0'),
                                                                                                               upper_bound=IntValue(
                                                                                                                   raw='1'))),
                                                                                                       then=ConnectorEnd(
                                                                                                           name=None,
                                                                                                           reference=QualifiedName(
                                                                                                               names=[
                                                                                                                   'focus']),
                                                                                                           multiplicity=MultiplicityBounds(
                                                                                                               lower_bound=IntValue(
                                                                                                                   raw='0'),
                                                                                                               upper_bound=IntValue(
                                                                                                                   raw='1'))),
                                                                                                       body=[])),
                                                                                OwnedFeatureMember(visibility=None,
                                                                                                   element=Succession(
                                                                                                       direction=None,
                                                                                                       is_abstract=False,
                                                                                                       relationship_type=None,
                                                                                                       is_readonly=False,
                                                                                                       is_derived=False,
                                                                                                       is_end=False,
                                                                                                       annotations=[],
                                                                                                       is_all=False,
                                                                                                       identification=None,
                                                                                                       specializations=[],
                                                                                                       multiplicity=None,
                                                                                                       is_ordered=False,
                                                                                                       is_nonunique=False,
                                                                                                       conjugation=None,
                                                                                                       relationships=[],
                                                                                                       is_all_succession=False,
                                                                                                       first=ConnectorEnd(
                                                                                                           name=None,
                                                                                                           reference=QualifiedName(
                                                                                                               names=[
                                                                                                                   'focus']),
                                                                                                           multiplicity=MultiplicityBounds(
                                                                                                               lower_bound=None,
                                                                                                               upper_bound=IntValue(
                                                                                                                   raw='1'))),
                                                                                                       then=ConnectorEnd(
                                                                                                           name=None,
                                                                                                           reference=QualifiedName(
                                                                                                               names=[
                                                                                                                   'shoot']),
                                                                                                           multiplicity=MultiplicityBounds(
                                                                                                               lower_bound=IntValue(
                                                                                                                   raw='0'),
                                                                                                               upper_bound=IntValue(
                                                                                                                   raw='1'))),
                                                                                                       body=[]))])),
    ])
    def test_behavior(self, text, expected):
        parser = _parser_for_rule('behavior')
        if isinstance(expected, type) and issubclass(expected, Exception):
            with pytest.raises(expected):
                _ = parser(text)
        else:
            v, rules = parser(text)
            assert v == expected
            assert 'behavior' in rules

    @pytest.mark.parametrize(['text', 'expected'], [
        ('composite step shoot : Shoot;',
         Step(direction=None, is_abstract=False, relationship_type=FeatureRelationshipType.COMPOSITE, is_readonly=False,
              is_derived=False, is_end=False, annotations=[], is_all=False,
              identification=Identification(short_name=None, name='shoot'),
              specializations=[TypingsPart(items=[QualifiedName(names=['Shoot'])])], multiplicity=None,
              is_ordered=False, is_nonunique=False, conjugation=None, relationships=[], is_default=False,
              value_type=None, value=None, body=[])),
        ('step x = 1;',
         Step(direction=None, is_abstract=False, relationship_type=None, is_readonly=False, is_derived=False,
              is_end=False, annotations=[], is_all=False, identification=Identification(short_name=None, name='x'),
              specializations=[], multiplicity=None, is_ordered=False, is_nonunique=False, conjugation=None,
              relationships=[], is_default=False, value_type=FeatureValueType.BIND, value=IntValue(raw='1'), body=[])),
    ])
    def test_step(self, text, expected):
        parser = _parser_for_rule('step')
        if isinstance(expected, type) and issubclass(expected, Exception):
            with pytest.raises(expected):
                _ = parser(text)
        else:
            v, rules = parser(text)
            assert v == expected
            assert 'step' in rules

    @pytest.mark.parametrize(['text', 'expected'], [
        ('function Velocity {\n'
         '    in v_i : VelocityValue;\n'
         '    in a : AccelerationValue;\n'
         '    in dt : TimeValue;\n'
         '    return v_f : VelocityValue;\n'
         '}',
         Function(is_abstract=False, annotations=[], is_all=False,
                  identification=Identification(short_name=None, name='Velocity'), multiplicity_bounds=None,
                  conjugation=None, superclassing=None, relationships=[], body=[OwnedFeatureMember(visibility=None,
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
                                                                                                           name='v_i'),
                                                                                                       specializations=[
                                                                                                           TypingsPart(
                                                                                                               items=[
                                                                                                                   QualifiedName(
                                                                                                                       names=[
                                                                                                                           'VelocityValue'])])],
                                                                                                       multiplicity=None,
                                                                                                       is_ordered=False,
                                                                                                       is_nonunique=False,
                                                                                                       conjugation=None,
                                                                                                       relationships=[],
                                                                                                       is_default=False,
                                                                                                       value_type=None,
                                                                                                       value=None,
                                                                                                       body=[])),
                                                                                OwnedFeatureMember(visibility=None,
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
                                                                                                           name='a'),
                                                                                                       specializations=[
                                                                                                           TypingsPart(
                                                                                                               items=[
                                                                                                                   QualifiedName(
                                                                                                                       names=[
                                                                                                                           'AccelerationValue'])])],
                                                                                                       multiplicity=None,
                                                                                                       is_ordered=False,
                                                                                                       is_nonunique=False,
                                                                                                       conjugation=None,
                                                                                                       relationships=[],
                                                                                                       is_default=False,
                                                                                                       value_type=None,
                                                                                                       value=None,
                                                                                                       body=[])),
                                                                                OwnedFeatureMember(visibility=None,
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
                                                                                                           name='dt'),
                                                                                                       specializations=[
                                                                                                           TypingsPart(
                                                                                                               items=[
                                                                                                                   QualifiedName(
                                                                                                                       names=[
                                                                                                                           'TimeValue'])])],
                                                                                                       multiplicity=None,
                                                                                                       is_ordered=False,
                                                                                                       is_nonunique=False,
                                                                                                       conjugation=None,
                                                                                                       relationships=[],
                                                                                                       is_default=False,
                                                                                                       value_type=None,
                                                                                                       value=None,
                                                                                                       body=[])),
                                                                                Return(visibility=None,
                                                                                       feature=Feature(direction=None,
                                                                                                       is_abstract=False,
                                                                                                       relationship_type=None,
                                                                                                       is_readonly=False,
                                                                                                       is_derived=False,
                                                                                                       is_end=False,
                                                                                                       annotations=[],
                                                                                                       is_all=False,
                                                                                                       identification=Identification(
                                                                                                           short_name=None,
                                                                                                           name='v_f'),
                                                                                                       specializations=[
                                                                                                           TypingsPart(
                                                                                                               items=[
                                                                                                                   QualifiedName(
                                                                                                                       names=[
                                                                                                                           'VelocityValue'])])],
                                                                                                       multiplicity=None,
                                                                                                       is_ordered=False,
                                                                                                       is_nonunique=False,
                                                                                                       conjugation=None,
                                                                                                       relationships=[],
                                                                                                       is_default=False,
                                                                                                       value_type=None,
                                                                                                       value=None,
                                                                                                       body=[]))])),
        ('function {\n    in a : Integer;\n    return b: Integer; \n    x + 2\n}',
         Function(is_abstract=False, annotations=[], is_all=False,
                  identification=Identification(short_name=None, name=None), multiplicity_bounds=None, conjugation=None,
                  superclassing=None, relationships=[], body=[OwnedFeatureMember(visibility=None, element=Feature(
                 direction=FeatureDirection.IN, is_abstract=False, relationship_type=None, is_readonly=False,
                 is_derived=False, is_end=False, annotations=[], is_all=False,
                 identification=Identification(short_name=None, name='a'),
                 specializations=[TypingsPart(items=[QualifiedName(names=['Integer'])])], multiplicity=None,
                 is_ordered=False, is_nonunique=False, conjugation=None, relationships=[], is_default=False,
                 value_type=None, value=None, body=[])), Return(visibility=None,
                                                                feature=Feature(direction=None, is_abstract=False,
                                                                                relationship_type=None,
                                                                                is_readonly=False, is_derived=False,
                                                                                is_end=False, annotations=[],
                                                                                is_all=False,
                                                                                identification=Identification(
                                                                                    short_name=None, name='b'),
                                                                                specializations=[TypingsPart(items=[
                                                                                    QualifiedName(names=['Integer'])])],
                                                                                multiplicity=None, is_ordered=False,
                                                                                is_nonunique=False, conjugation=None,
                                                                                relationships=[], is_default=False,
                                                                                value_type=None, value=None, body=[])),
                                                              Result(visibility=None, expression=BinOp(op='+',
                                                                                                       x=QualifiedName(
                                                                                                           names=['x']),
                                                                                                       y=IntValue(
                                                                                                           raw='2')))])),
        ('abstract function Dynamics {\n'
         '    in initialState : DynamicState;\n'
         '    in time : TimeValue;\n'
         '    return : DynamicState;\n'
         '}',
         Function(is_abstract=True, annotations=[], is_all=False,
                  identification=Identification(short_name=None, name='Dynamics'), multiplicity_bounds=None,
                  conjugation=None, superclassing=None, relationships=[], body=[OwnedFeatureMember(visibility=None,
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
                                                                                                           name='initialState'),
                                                                                                       specializations=[
                                                                                                           TypingsPart(
                                                                                                               items=[
                                                                                                                   QualifiedName(
                                                                                                                       names=[
                                                                                                                           'DynamicState'])])],
                                                                                                       multiplicity=None,
                                                                                                       is_ordered=False,
                                                                                                       is_nonunique=False,
                                                                                                       conjugation=None,
                                                                                                       relationships=[],
                                                                                                       is_default=False,
                                                                                                       value_type=None,
                                                                                                       value=None,
                                                                                                       body=[])),
                                                                                OwnedFeatureMember(visibility=None,
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
                                                                                                           name='time'),
                                                                                                       specializations=[
                                                                                                           TypingsPart(
                                                                                                               items=[
                                                                                                                   QualifiedName(
                                                                                                                       names=[
                                                                                                                           'TimeValue'])])],
                                                                                                       multiplicity=None,
                                                                                                       is_ordered=False,
                                                                                                       is_nonunique=False,
                                                                                                       conjugation=None,
                                                                                                       relationships=[],
                                                                                                       is_default=False,
                                                                                                       value_type=None,
                                                                                                       value=None,
                                                                                                       body=[])),
                                                                                Return(visibility=None,
                                                                                       feature=Feature(direction=None,
                                                                                                       is_abstract=False,
                                                                                                       relationship_type=None,
                                                                                                       is_readonly=False,
                                                                                                       is_derived=False,
                                                                                                       is_end=False,
                                                                                                       annotations=[],
                                                                                                       is_all=False,
                                                                                                       identification=None,
                                                                                                       specializations=[
                                                                                                           TypingsPart(
                                                                                                               items=[
                                                                                                                   QualifiedName(
                                                                                                                       names=[
                                                                                                                           'DynamicState'])])],
                                                                                                       multiplicity=None,
                                                                                                       is_ordered=False,
                                                                                                       is_nonunique=False,
                                                                                                       conjugation=None,
                                                                                                       relationships=[],
                                                                                                       is_default=False,
                                                                                                       value_type=None,
                                                                                                       value=None,
                                                                                                       body=[]))])),
        ('function VehicleDynamics specializes Dynamics {\n'
         '    // Each parameter redefines the corresponding superclassifier parameter\n'
         '    in initialState : VehicleState;\n'
         '    in time : TimeValue;\n'
         '    return : VehicleState;\n'
         '}',
         Function(is_abstract=False, annotations=[], is_all=False,
                  identification=Identification(short_name=None, name='VehicleDynamics'), multiplicity_bounds=None,
                  conjugation=None, superclassing=SuperclassingPart(items=[QualifiedName(names=['Dynamics'])]),
                  relationships=[], body=[OwnedFeatureMember(visibility=None,
                                                             element=Feature(direction=FeatureDirection.IN,
                                                                             is_abstract=False, relationship_type=None,
                                                                             is_readonly=False, is_derived=False,
                                                                             is_end=False, annotations=[], is_all=False,
                                                                             identification=Identification(
                                                                                 short_name=None, name='initialState'),
                                                                             specializations=[TypingsPart(items=[
                                                                                 QualifiedName(
                                                                                     names=['VehicleState'])])],
                                                                             multiplicity=None, is_ordered=False,
                                                                             is_nonunique=False, conjugation=None,
                                                                             relationships=[], is_default=False,
                                                                             value_type=None, value=None, body=[])),
                                          OwnedFeatureMember(visibility=None,
                                                             element=Feature(direction=FeatureDirection.IN,
                                                                             is_abstract=False, relationship_type=None,
                                                                             is_readonly=False, is_derived=False,
                                                                             is_end=False, annotations=[], is_all=False,
                                                                             identification=Identification(
                                                                                 short_name=None, name='time'),
                                                                             specializations=[TypingsPart(items=[
                                                                                 QualifiedName(names=['TimeValue'])])],
                                                                             multiplicity=None, is_ordered=False,
                                                                             is_nonunique=False, conjugation=None,
                                                                             relationships=[], is_default=False,
                                                                             value_type=None, value=None, body=[])),
                                          Return(visibility=None, feature=Feature(direction=None, is_abstract=False,
                                                                                  relationship_type=None,
                                                                                  is_readonly=False, is_derived=False,
                                                                                  is_end=False, annotations=[],
                                                                                  is_all=False, identification=None,
                                                                                  specializations=[TypingsPart(items=[
                                                                                      QualifiedName(
                                                                                          names=['VehicleState'])])],
                                                                                  multiplicity=None, is_ordered=False,
                                                                                  is_nonunique=False, conjugation=None,
                                                                                  relationships=[], is_default=False,
                                                                                  value_type=None, value=None,
                                                                                  body=[]))])),
        ('function Average {\n'
         '    in scores[1..*] : Rational;\n'
         '    return : Rational;\n'
         '    sum(scores) / size(scores)\n'
         '}',
         Function(is_abstract=False, annotations=[], is_all=False,
                  identification=Identification(short_name=None, name='Average'), multiplicity_bounds=None,
                  conjugation=None, superclassing=None, relationships=[],
                  body=[OwnedFeatureMember(
                      visibility=None,
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
                              name='scores'),
                          specializations=[
                              TypingsPart(
                                  items=[
                                      QualifiedName(
                                          names=[
                                              'Rational'])])],
                          multiplicity=MultiplicityBounds(
                              lower_bound=IntValue(
                                  raw='1'),
                              upper_bound=InfValue()),
                          is_ordered=False,
                          is_nonunique=False,
                          conjugation=None,
                          relationships=[],
                          is_default=False,
                          value_type=None,
                          value=None,
                          body=[])),
                      Return(visibility=None,
                             feature=Feature(direction=None,
                                             is_abstract=False,
                                             relationship_type=None,
                                             is_readonly=False,
                                             is_derived=False,
                                             is_end=False,
                                             annotations=[],
                                             is_all=False,
                                             identification=None,
                                             specializations=[
                                                 TypingsPart(
                                                     items=[
                                                         QualifiedName(
                                                             names=[
                                                                 'Rational'])])],
                                             multiplicity=None,
                                             is_ordered=False,
                                             is_nonunique=False,
                                             conjugation=None,
                                             relationships=[],
                                             is_default=False,
                                             value_type=None,
                                             value=None,
                                             body=[])),
                      Result(visibility=None,
                             expression=BinOp(op='/',
                                              x=InvocationExpression(
                                                  name=QualifiedName(
                                                      names=[
                                                          'sum']),
                                                  arguments=[
                                                      QualifiedName(
                                                          names=[
                                                              'scores'])]),
                                              y=InvocationExpression(
                                                  name=QualifiedName(
                                                      names=[
                                                          'size']),
                                                  arguments=[
                                                      QualifiedName(
                                                          names=[
                                                              'scores'])])))])),
        ('function Average {\n'
         '    in scores[1..*] : Rational;\n'
         '    return : Rational = sum(scores) / size(scores);\n'
         '}',
         Function(is_abstract=False, annotations=[], is_all=False,
                  identification=Identification(short_name=None, name='Average'), multiplicity_bounds=None,
                  conjugation=None, superclassing=None, relationships=[],
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
                                                   name='scores'),
                                               specializations=[
                                                   TypingsPart(
                                                       items=[
                                                           QualifiedName(
                                                               names=[
                                                                   'Rational'])])],
                                               multiplicity=MultiplicityBounds(
                                                   lower_bound=IntValue(
                                                       raw='1'),
                                                   upper_bound=InfValue()),
                                               is_ordered=False,
                                               is_nonunique=False,
                                               conjugation=None,
                                               relationships=[],
                                               is_default=False,
                                               value_type=None,
                                               value=None,
                                               body=[])),
                        Return(visibility=None,
                               feature=Feature(direction=None,
                                               is_abstract=False,
                                               relationship_type=None,
                                               is_readonly=False,
                                               is_derived=False,
                                               is_end=False,
                                               annotations=[],
                                               is_all=False,
                                               identification=None,
                                               specializations=[
                                                   TypingsPart(
                                                       items=[
                                                           QualifiedName(
                                                               names=[
                                                                   'Rational'])])],
                                               multiplicity=None,
                                               is_ordered=False,
                                               is_nonunique=False,
                                               conjugation=None,
                                               relationships=[],
                                               is_default=False,
                                               value_type=FeatureValueType.BIND,
                                               value=BinOp(
                                                   op='/',
                                                   x=InvocationExpression(
                                                       name=QualifiedName(
                                                           names=[
                                                               'sum']),
                                                       arguments=[
                                                           QualifiedName(
                                                               names=[
                                                                   'scores'])]),
                                                   y=InvocationExpression(
                                                       name=QualifiedName(
                                                           names=[
                                                               'size']),
                                                       arguments=[
                                                           QualifiedName(
                                                               names=[
                                                                   'scores'])])),
                                               body=[]))])),
    ])
    def test_function(self, text, expected):
        parser = _parser_for_rule('function')
        if isinstance(expected, type) and issubclass(expected, Exception):
            with pytest.raises(expected):
                _ = parser(text)
        else:
            v, rules = parser(text)
            assert v == expected
            assert 'function' in rules

    @pytest.mark.parametrize(['text', 'expected'], [
        ('expr computation : ComputeDynamics {\n'
         '    // Parameters redefined parameters of ComputeDynamics.\n'
         '    in state;\n'
         '    in dt;\n'
         '    return result;\n'
         '}',
         Expression(direction=None, is_abstract=False, relationship_type=None, is_readonly=False, is_derived=False,
                    is_end=False, annotations=[], is_all=False,
                    identification=Identification(short_name=None, name='computation'),
                    specializations=[TypingsPart(items=[QualifiedName(names=['ComputeDynamics'])])], multiplicity=None,
                    is_ordered=False, is_nonunique=False, conjugation=None, relationships=[], is_default=False,
                    value_type=None, value=None, body=[OwnedFeatureMember(visibility=None,
                                                                          element=Feature(direction=FeatureDirection.IN,
                                                                                          is_abstract=False,
                                                                                          relationship_type=None,
                                                                                          is_readonly=False,
                                                                                          is_derived=False,
                                                                                          is_end=False, annotations=[],
                                                                                          is_all=False,
                                                                                          identification=Identification(
                                                                                              short_name=None,
                                                                                              name='state'),
                                                                                          specializations=[],
                                                                                          multiplicity=None,
                                                                                          is_ordered=False,
                                                                                          is_nonunique=False,
                                                                                          conjugation=None,
                                                                                          relationships=[],
                                                                                          is_default=False,
                                                                                          value_type=None, value=None,
                                                                                          body=[])),
                                                       OwnedFeatureMember(visibility=None,
                                                                          element=Feature(direction=FeatureDirection.IN,
                                                                                          is_abstract=False,
                                                                                          relationship_type=None,
                                                                                          is_readonly=False,
                                                                                          is_derived=False,
                                                                                          is_end=False, annotations=[],
                                                                                          is_all=False,
                                                                                          identification=Identification(
                                                                                              short_name=None,
                                                                                              name='dt'),
                                                                                          specializations=[],
                                                                                          multiplicity=None,
                                                                                          is_ordered=False,
                                                                                          is_nonunique=False,
                                                                                          conjugation=None,
                                                                                          relationships=[],
                                                                                          is_default=False,
                                                                                          value_type=None, value=None,
                                                                                          body=[])),
                                                       Return(visibility=None,
                                                              feature=Feature(direction=None, is_abstract=False,
                                                                              relationship_type=None, is_readonly=False,
                                                                              is_derived=False, is_end=False,
                                                                              annotations=[], is_all=False,
                                                                              identification=Identification(
                                                                                  short_name=None, name='result'),
                                                                              specializations=[], multiplicity=None,
                                                                              is_ordered=False, is_nonunique=False,
                                                                              conjugation=None, relationships=[],
                                                                              is_default=False, value_type=None,
                                                                              value=None, body=[]))])),
        ('expr vehicleComputation subsets computation {\n'
         '// Input parameters are inherited, result is redefined.\n'
         'return : VehicleState;\n'
         '}',
         Expression(direction=None, is_abstract=False, relationship_type=None, is_readonly=False, is_derived=False,
                    is_end=False, annotations=[], is_all=False,
                    identification=Identification(short_name=None, name='vehicleComputation'),
                    specializations=[SubsettingsPart(items=[QualifiedName(names=['computation'])])], multiplicity=None,
                    is_ordered=False, is_nonunique=False, conjugation=None, relationships=[], is_default=False,
                    value_type=None, value=None, body=[Return(visibility=None,
                                                              feature=Feature(direction=None, is_abstract=False,
                                                                              relationship_type=None, is_readonly=False,
                                                                              is_derived=False, is_end=False,
                                                                              annotations=[], is_all=False,
                                                                              identification=None, specializations=[
                                                                      TypingsPart(items=[
                                                                          QualifiedName(names=['VehicleState'])])],
                                                                              multiplicity=None, is_ordered=False,
                                                                              is_nonunique=False, conjugation=None,
                                                                              relationships=[], is_default=False,
                                                                              value_type=None, value=None, body=[]))])),
        ('expr : VehicleDynamics {\n'
         '    in initialState;\n'
         '    in time;\n'
         '    return result;\n'
         '    vehicleComputation(initialState, time)\n'
         '}',
         Expression(direction=None, is_abstract=False, relationship_type=None, is_readonly=False, is_derived=False,
                    is_end=False, annotations=[], is_all=False, identification=None,
                    specializations=[TypingsPart(items=[QualifiedName(names=['VehicleDynamics'])])], multiplicity=None,
                    is_ordered=False, is_nonunique=False, conjugation=None, relationships=[], is_default=False,
                    value_type=None, value=None, body=[OwnedFeatureMember(visibility=None,
                                                                          element=Feature(direction=FeatureDirection.IN,
                                                                                          is_abstract=False,
                                                                                          relationship_type=None,
                                                                                          is_readonly=False,
                                                                                          is_derived=False,
                                                                                          is_end=False, annotations=[],
                                                                                          is_all=False,
                                                                                          identification=Identification(
                                                                                              short_name=None,
                                                                                              name='initialState'),
                                                                                          specializations=[],
                                                                                          multiplicity=None,
                                                                                          is_ordered=False,
                                                                                          is_nonunique=False,
                                                                                          conjugation=None,
                                                                                          relationships=[],
                                                                                          is_default=False,
                                                                                          value_type=None, value=None,
                                                                                          body=[])),
                                                       OwnedFeatureMember(visibility=None,
                                                                          element=Feature(direction=FeatureDirection.IN,
                                                                                          is_abstract=False,
                                                                                          relationship_type=None,
                                                                                          is_readonly=False,
                                                                                          is_derived=False,
                                                                                          is_end=False, annotations=[],
                                                                                          is_all=False,
                                                                                          identification=Identification(
                                                                                              short_name=None,
                                                                                              name='time'),
                                                                                          specializations=[],
                                                                                          multiplicity=None,
                                                                                          is_ordered=False,
                                                                                          is_nonunique=False,
                                                                                          conjugation=None,
                                                                                          relationships=[],
                                                                                          is_default=False,
                                                                                          value_type=None, value=None,
                                                                                          body=[])),
                                                       Return(visibility=None,
                                                              feature=Feature(direction=None, is_abstract=False,
                                                                              relationship_type=None, is_readonly=False,
                                                                              is_derived=False, is_end=False,
                                                                              annotations=[], is_all=False,
                                                                              identification=Identification(
                                                                                  short_name=None, name='result'),
                                                                              specializations=[], multiplicity=None,
                                                                              is_ordered=False, is_nonunique=False,
                                                                              conjugation=None, relationships=[],
                                                                              is_default=False, value_type=None,
                                                                              value=None, body=[])),
                                                       Result(visibility=None, expression=InvocationExpression(
                                                           name=QualifiedName(names=['vehicleComputation']),
                                                           arguments=[QualifiedName(names=['initialState']),
                                                                      QualifiedName(names=['time'])]))])),
        ('expr : Dynamics {\n'
         '    in initialState;\n'
         '    in time;\n'
         '    return result : VehicleState =\n'
         '    vehicleComputation(initialState, time);\n'
         '}',
         Expression(direction=None, is_abstract=False, relationship_type=None, is_readonly=False, is_derived=False,
                    is_end=False, annotations=[], is_all=False, identification=None,
                    specializations=[TypingsPart(items=[QualifiedName(names=['Dynamics'])])], multiplicity=None,
                    is_ordered=False, is_nonunique=False, conjugation=None, relationships=[], is_default=False,
                    value_type=None, value=None, body=[OwnedFeatureMember(visibility=None,
                                                                          element=Feature(direction=FeatureDirection.IN,
                                                                                          is_abstract=False,
                                                                                          relationship_type=None,
                                                                                          is_readonly=False,
                                                                                          is_derived=False,
                                                                                          is_end=False, annotations=[],
                                                                                          is_all=False,
                                                                                          identification=Identification(
                                                                                              short_name=None,
                                                                                              name='initialState'),
                                                                                          specializations=[],
                                                                                          multiplicity=None,
                                                                                          is_ordered=False,
                                                                                          is_nonunique=False,
                                                                                          conjugation=None,
                                                                                          relationships=[],
                                                                                          is_default=False,
                                                                                          value_type=None, value=None,
                                                                                          body=[])),
                                                       OwnedFeatureMember(visibility=None,
                                                                          element=Feature(direction=FeatureDirection.IN,
                                                                                          is_abstract=False,
                                                                                          relationship_type=None,
                                                                                          is_readonly=False,
                                                                                          is_derived=False,
                                                                                          is_end=False, annotations=[],
                                                                                          is_all=False,
                                                                                          identification=Identification(
                                                                                              short_name=None,
                                                                                              name='time'),
                                                                                          specializations=[],
                                                                                          multiplicity=None,
                                                                                          is_ordered=False,
                                                                                          is_nonunique=False,
                                                                                          conjugation=None,
                                                                                          relationships=[],
                                                                                          is_default=False,
                                                                                          value_type=None, value=None,
                                                                                          body=[])),
                                                       Return(visibility=None,
                                                              feature=Feature(direction=None, is_abstract=False,
                                                                              relationship_type=None, is_readonly=False,
                                                                              is_derived=False, is_end=False,
                                                                              annotations=[], is_all=False,
                                                                              identification=Identification(
                                                                                  short_name=None, name='result'),
                                                                              specializations=[TypingsPart(items=[
                                                                                  QualifiedName(
                                                                                      names=['VehicleState'])])],
                                                                              multiplicity=None, is_ordered=False,
                                                                              is_nonunique=False, conjugation=None,
                                                                              relationships=[], is_default=False,
                                                                              value_type=FeatureValueType.BIND,
                                                                              value=InvocationExpression(
                                                                                  name=QualifiedName(
                                                                                      names=['vehicleComputation']),
                                                                                  arguments=[QualifiedName(
                                                                                      names=['initialState']),
                                                                                      QualifiedName(
                                                                                          names=['time'])]),
                                                                              body=[]))])),
        ('expr isFull = false;',
         Expression(direction=None, is_abstract=False, relationship_type=None, is_readonly=False, is_derived=False,
                    is_end=False, annotations=[], is_all=False,
                    identification=Identification(short_name=None, name='isFull'), specializations=[],
                    multiplicity=None, is_ordered=False, is_nonunique=False, conjugation=None, relationships=[],
                    is_default=False, value_type=FeatureValueType.BIND, value=BoolValue(raw='false'), body=[])),
    ])
    def test_expression(self, text, expected):
        parser = _parser_for_rule('expression')
        if isinstance(expected, type) and issubclass(expected, Exception):
            with pytest.raises(expected):
                _ = parser(text)
        else:
            v, rules = parser(text)
            assert v == expected
            assert 'expression' in rules

    @pytest.mark.parametrize(['text', 'expected'], [
        ('predicate isAssembled {\n'
         '    in assembly : Assembly;\n'
         '    in subassemblies[*] : Assembly;\n'
         '}',
         Predicate(is_abstract=False, annotations=[], is_all=False,
                   identification=Identification(short_name=None, name='isAssembled'), multiplicity_bounds=None,
                   conjugation=None, superclassing=None, relationships=[], body=[OwnedFeatureMember(visibility=None,
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
                                                                                                            name='assembly'),
                                                                                                        specializations=[
                                                                                                            TypingsPart(
                                                                                                                items=[
                                                                                                                    QualifiedName(
                                                                                                                        names=[
                                                                                                                            'Assembly'])])],
                                                                                                        multiplicity=None,
                                                                                                        is_ordered=False,
                                                                                                        is_nonunique=False,
                                                                                                        conjugation=None,
                                                                                                        relationships=[],
                                                                                                        is_default=False,
                                                                                                        value_type=None,
                                                                                                        value=None,
                                                                                                        body=[])),
                                                                                 OwnedFeatureMember(visibility=None,
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
                                                                                                            name='subassemblies'),
                                                                                                        specializations=[
                                                                                                            TypingsPart(
                                                                                                                items=[
                                                                                                                    QualifiedName(
                                                                                                                        names=[
                                                                                                                            'Assembly'])])],
                                                                                                        multiplicity=MultiplicityBounds(
                                                                                                            lower_bound=None,
                                                                                                            upper_bound=InfValue()),
                                                                                                        is_ordered=False,
                                                                                                        is_nonunique=False,
                                                                                                        conjugation=None,
                                                                                                        relationships=[],
                                                                                                        is_default=False,
                                                                                                        value_type=None,
                                                                                                        value=None,
                                                                                                        body=[]))])),
        ('predicate isFull {\n'
         '    in tank : FuelTank;\n'
         '    tank_fuelLevel == tank_maxFuelLevel\n'
         '}',
         Predicate(is_abstract=False, annotations=[], is_all=False,
                   identification=Identification(short_name=None, name='isFull'), multiplicity_bounds=None,
                   conjugation=None, superclassing=None, relationships=[], body=[OwnedFeatureMember(visibility=None,
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
                                                                                                            name='tank'),
                                                                                                        specializations=[
                                                                                                            TypingsPart(
                                                                                                                items=[
                                                                                                                    QualifiedName(
                                                                                                                        names=[
                                                                                                                            'FuelTank'])])],
                                                                                                        multiplicity=None,
                                                                                                        is_ordered=False,
                                                                                                        is_nonunique=False,
                                                                                                        conjugation=None,
                                                                                                        relationships=[],
                                                                                                        is_default=False,
                                                                                                        value_type=None,
                                                                                                        value=None,
                                                                                                        body=[])),
                                                                                 Result(visibility=None,
                                                                                        expression=BinOp(op='==',
                                                                                                         x=QualifiedName(
                                                                                                             names=[
                                                                                                                 'tank_fuelLevel']),
                                                                                                         y=QualifiedName(
                                                                                                             names=[
                                                                                                                 'tank_maxFuelLevel'])))])),
    ])
    def test_predicate(self, text, expected):
        parser = _parser_for_rule('predicate')
        if isinstance(expected, type) and issubclass(expected, Exception):
            with pytest.raises(expected):
                _ = parser(text)
        else:
            v, rules = parser(text)
            assert v == expected
            assert 'predicate' in rules

    @pytest.mark.parametrize(['text', 'expected'], [
        ('bool assemblyChecks[*] : isAssembled;',
         BooleanExpression(direction=None, is_abstract=False, relationship_type=None, is_readonly=False,
                           is_derived=False, is_end=False, annotations=[], is_all=False,
                           identification=Identification(short_name=None, name='assemblyChecks'),
                           specializations=[TypingsPart(items=[QualifiedName(names=['isAssembled'])])],
                           multiplicity=MultiplicityBounds(lower_bound=None, upper_bound=InfValue()), is_ordered=False,
                           is_nonunique=False, conjugation=None, relationships=[], is_default=False, value_type=None,
                           value=None, body=[])),
        ('bool isFull { fuelLevel == maxFuelLevel }',
         BooleanExpression(direction=None, is_abstract=False, relationship_type=None, is_readonly=False,
                           is_derived=False, is_end=False, annotations=[], is_all=False,
                           identification=Identification(short_name=None, name='isFull'), specializations=[],
                           multiplicity=None, is_ordered=False, is_nonunique=False, conjugation=None, relationships=[],
                           is_default=False, value_type=None, value=None, body=[Result(visibility=None,
                                                                                       expression=BinOp(op='==',
                                                                                                        x=QualifiedName(
                                                                                                            names=[
                                                                                                                'fuelLevel']),
                                                                                                        y=QualifiedName(
                                                                                                            names=[
                                                                                                                'maxFuelLevel'])))])),
        ('bool isFull = false;',
         BooleanExpression(direction=None, is_abstract=False, relationship_type=None, is_readonly=False,
                           is_derived=False, is_end=False, annotations=[], is_all=False,
                           identification=Identification(short_name=None, name='isFull'), specializations=[],
                           multiplicity=None, is_ordered=False, is_nonunique=False, conjugation=None, relationships=[],
                           is_default=False, value_type=FeatureValueType.BIND, value=BoolValue(raw='false'), body=[])),
    ])
    def test_boolean_expression(self, text, expected):
        parser = _parser_for_rule('boolean_expression')
        if isinstance(expected, type) and issubclass(expected, Exception):
            with pytest.raises(expected):
                _ = parser(text)
        else:
            v, rules = parser(text)
            assert v == expected
            assert 'boolean_expression' in rules

    @pytest.mark.parametrize(['text', 'expected'], [
        ('inv { fuelLevel >= 0 & fuelLevel <= maxFuelLevel }',
         Invariant(direction=None, is_abstract=False, relationship_type=None, is_readonly=False, is_derived=False,
                   is_end=False, annotations=[], is_all=False, identification=None, specializations=[],
                   multiplicity=None, is_ordered=False, is_nonunique=False, conjugation=None, relationships=[],
                   is_default=False, value_type=None, value=None, body=[Result(visibility=None, expression=BinOp(op='&',
                                                                                                                 x=BinOp(
                                                                                                                     op='>=',
                                                                                                                     x=QualifiedName(
                                                                                                                         names=[
                                                                                                                             'fuelLevel']),
                                                                                                                     y=IntValue(
                                                                                                                         raw='0')),
                                                                                                                 y=BinOp(
                                                                                                                     op='<=',
                                                                                                                     x=QualifiedName(
                                                                                                                         names=[
                                                                                                                             'fuelLevel']),
                                                                                                                     y=QualifiedName(
                                                                                                                         names=[
                                                                                                                             'maxFuelLevel']))))],
                   asserted=True)),
        ('inv false { fuelLevel > maxFuelLevel }',
         Invariant(direction=None, is_abstract=False, relationship_type=None, is_readonly=False, is_derived=False,
                   is_end=False, annotations=[], is_all=False, identification=None, specializations=[],
                   multiplicity=None, is_ordered=False, is_nonunique=False, conjugation=None, relationships=[],
                   is_default=False, value_type=None, value=None, body=[Result(visibility=None, expression=BinOp(op='>',
                                                                                                                 x=QualifiedName(
                                                                                                                     names=[
                                                                                                                         'fuelLevel']),
                                                                                                                 y=QualifiedName(
                                                                                                                     names=[
                                                                                                                         'maxFuelLevel'])))],
                   asserted=False)),
        ("inv true <'+'> { 2 > 1 }",
         Invariant(direction=None, is_abstract=False, relationship_type=None, is_readonly=False, is_derived=False,
                   is_end=False, annotations=[], is_all=False, identification=Identification(short_name='+', name=None),
                   specializations=[], multiplicity=None, is_ordered=False, is_nonunique=False, conjugation=None,
                   relationships=[], is_default=False, value_type=None, value=None,
                   body=[Result(visibility=None, expression=BinOp(op='>', x=IntValue(raw='2'), y=IntValue(raw='1')))],
                   asserted=True)),
        ('inv x = 1;',
         Invariant(direction=None, is_abstract=False, relationship_type=None, is_readonly=False, is_derived=False,
                   is_end=False, annotations=[], is_all=False, identification=Identification(short_name=None, name='x'),
                   specializations=[], multiplicity=None, is_ordered=False, is_nonunique=False, conjugation=None,
                   relationships=[], is_default=False, value_type=FeatureValueType.BIND, value=IntValue(raw='1'),
                   body=[], asserted=True)),
    ])
    def test_invariant(self, text, expected):
        parser = _parser_for_rule('invariant')
        if isinstance(expected, type) and issubclass(expected, Exception):
            with pytest.raises(expected):
                _ = parser(text)
        else:
            v, rules = parser(text)
            assert v == expected
            assert 'invariant' in rules

    @pytest.mark.parametrize(['text', 'expected'], [
        ('sensors#(activeSensorIndex)',
         IndexExpression(entity=QualifiedName(names=['sensors']),
                         sequence=[QualifiedName(names=['activeSensorIndex'])])),
        ('detectorArray#(n, m)',
         IndexExpression(entity=QualifiedName(names=['detectorArray']),
                         sequence=[QualifiedName(names=['n']), QualifiedName(names=['m'])])),
        ('detectorArray#(n, m, t, z, x)',
         IndexExpression(entity=QualifiedName(names=['detectorArray']),
                         sequence=[QualifiedName(names=['n']), QualifiedName(names=['m']), QualifiedName(names=['t']),
                                   QualifiedName(names=['z']), QualifiedName(names=['x'])])),
    ])
    def test_index_expression(self, text, expected):
        parser = _parser_for_rule('index_expression')
        if isinstance(expected, type) and issubclass(expected, Exception):
            with pytest.raises(expected):
                _ = parser(text)
        else:
            v, rules = parser(text)
            assert v == expected
            assert 'index_expression' in rules

    @pytest.mark.parametrize(['text', 'expected'], [
        ('(temperatureSensor, windSensor, precipitationSensor)',
         SequenceExpression(sequence=[QualifiedName(names=['temperatureSensor']), QualifiedName(names=['windSensor']),
                                      QualifiedName(names=['precipitationSensor'])])),
        ('( 1, 3, 5, 7, 11, 13, )',
         SequenceExpression(
             sequence=[IntValue(raw='1'), IntValue(raw='3'), IntValue(raw='5'), IntValue(raw='7'), IntValue(raw='11'),
                       IntValue(raw='13')])),
        ('(highValue + lowValue)',
         SequenceExpression(
             sequence=[BinOp(op='+', x=QualifiedName(names=['highValue']), y=QualifiedName(names=['lowValue']))])),
        ('(((1, 2, 3), 4), (1, (2, 3), 4))',
         SequenceExpression(sequence=[SequenceExpression(
             sequence=[SequenceExpression(sequence=[IntValue(raw='1'), IntValue(raw='2'), IntValue(raw='3')]),
                       IntValue(raw='4')]), SequenceExpression(
             sequence=[IntValue(raw='1'), SequenceExpression(sequence=[IntValue(raw='2'), IntValue(raw='3')]),
                       IntValue(raw='4')])])),
    ])
    def test_sequence_expression(self, text, expected):
        parser = _parser_for_rule('sequence_expression')
        if isinstance(expected, type) and issubclass(expected, Exception):
            with pytest.raises(expected):
                _ = parser(text)
        else:
            v, rules = parser(text)
            assert v == expected
            assert 'sequence_expression' in rules

    @pytest.mark.parametrize(['text', 'expected'], [
        ('getPlatform(id).sensors.isActive',
         FeatureChainExpression(entity=InvocationExpression(name=QualifiedName(names=['getPlatform']),
                                                            arguments=[QualifiedName(names=['id'])]),
                                member=FeatureChain(
                                    items=[QualifiedName(names=['sensors']), QualifiedName(names=['isActive'])]))),
        ('(getPlatform(id).sensors).isActive',
         FeatureChainExpression(entity=SequenceExpression(sequence=[FeatureChainExpression(
             entity=InvocationExpression(name=QualifiedName(names=['getPlatform']),
                                         arguments=[QualifiedName(names=['id'])]),
             member=QualifiedName(names=['sensors']))]), member=QualifiedName(names=['isActive']))),
    ])
    def test_feature_chain_expression(self, text, expected):
        parser = _parser_for_rule('feature_chain_expression')
        if isinstance(expected, type) and issubclass(expected, Exception):
            with pytest.raises(expected):
                _ = parser(text)
        else:
            v, rules = parser(text)
            assert v == expected
            assert 'feature_chain_expression' in rules

    @pytest.mark.parametrize(['text', 'expected'], [
        ('sensors.{in s: Sensor; s.reading}',
         CollectExpression(entity=QualifiedName(names=['sensors']), body=[OwnedFeatureMember(visibility=None,
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
                                                                                                     name='s'),
                                                                                                 specializations=[
                                                                                                     TypingsPart(items=[
                                                                                                         QualifiedName(
                                                                                                             names=[
                                                                                                                 'Sensor'])])],
                                                                                                 multiplicity=None,
                                                                                                 is_ordered=False,
                                                                                                 is_nonunique=False,
                                                                                                 conjugation=None,
                                                                                                 relationships=[],
                                                                                                 is_default=False,
                                                                                                 value_type=None,
                                                                                                 value=None, body=[])),
                                                                          Result(visibility=None,
                                                                                 expression=FeatureChainExpression(
                                                                                     entity=QualifiedName(names=['s']),
                                                                                     member=QualifiedName(
                                                                                         names=['reading'])))])),
    ])
    def test_collect_expression(self, text, expected):
        parser = _parser_for_rule('collect_expression')
        if isinstance(expected, type) and issubclass(expected, Exception):
            with pytest.raises(expected):
                _ = parser(text)
        else:
            v, rules = parser(text)
            assert v == expected
            assert 'collect_expression' in rules

    @pytest.mark.parametrize(['text', 'expected'], [
        ('sensors.?{in s: Sensor; s.isActive}',
         SelectExpression(entity=QualifiedName(names=['sensors']), body=[OwnedFeatureMember(visibility=None,
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
                                                                                                    name='s'),
                                                                                                specializations=[
                                                                                                    TypingsPart(items=[
                                                                                                        QualifiedName(
                                                                                                            names=[
                                                                                                                'Sensor'])])],
                                                                                                multiplicity=None,
                                                                                                is_ordered=False,
                                                                                                is_nonunique=False,
                                                                                                conjugation=None,
                                                                                                relationships=[],
                                                                                                is_default=False,
                                                                                                value_type=None,
                                                                                                value=None, body=[])),
                                                                         Result(visibility=None,
                                                                                expression=FeatureChainExpression(
                                                                                    entity=QualifiedName(names=['s']),
                                                                                    member=QualifiedName(
                                                                                        names=['isActive'])))])),
    ])
    def test_select_expression(self, text, expected):
        parser = _parser_for_rule('select_expression')
        if isinstance(expected, type) and issubclass(expected, Exception):
            with pytest.raises(expected):
                _ = parser(text)
        else:
            v, rules = parser(text)
            assert v == expected
            assert 'select_expression' in rules

    @pytest.mark.parametrize(['text', 'expected'], [
        ('{in x: Number; x + 1}',
         BodyExpression(body=[OwnedFeatureMember(visibility=None,
                                                 element=Feature(direction=FeatureDirection.IN, is_abstract=False,
                                                                 relationship_type=None, is_readonly=False,
                                                                 is_derived=False, is_end=False, annotations=[],
                                                                 is_all=False,
                                                                 identification=Identification(short_name=None,
                                                                                               name='x'),
                                                                 specializations=[TypingsPart(
                                                                     items=[QualifiedName(names=['Number'])])],
                                                                 multiplicity=None, is_ordered=False,
                                                                 is_nonunique=False, conjugation=None, relationships=[],
                                                                 is_default=False, value_type=None, value=None,
                                                                 body=[])), Result(visibility=None,
                                                                                   expression=BinOp(op='+',
                                                                                                    x=QualifiedName(
                                                                                                        names=['x']),
                                                                                                    y=IntValue(
                                                                                                        raw='1')))])),
        ('{in x; if x istype Integer? (x as Integer) + 1 else 0}',
         BodyExpression(body=[OwnedFeatureMember(visibility=None,
                                                 element=Feature(direction=FeatureDirection.IN, is_abstract=False,
                                                                 relationship_type=None, is_readonly=False,
                                                                 is_derived=False, is_end=False, annotations=[],
                                                                 is_all=False,
                                                                 identification=Identification(short_name=None,
                                                                                               name='x'),
                                                                 specializations=[], multiplicity=None,
                                                                 is_ordered=False, is_nonunique=False, conjugation=None,
                                                                 relationships=[], is_default=False, value_type=None,
                                                                 value=None, body=[])), Result(visibility=None,
                                                                                               expression=IfTestOp(
                                                                                                   condition=ClsTestOp(
                                                                                                       op='istype',
                                                                                                       x=QualifiedName(
                                                                                                           names=['x']),
                                                                                                       y=QualifiedName(
                                                                                                           names=[
                                                                                                               'Integer'])),
                                                                                                   if_true=BinOp(op='+',
                                                                                                                 x=SequenceExpression(
                                                                                                                     sequence=[
                                                                                                                         ClsCastOp(
                                                                                                                             x=QualifiedName(
                                                                                                                                 names=[
                                                                                                                                     'x']),
                                                                                                                             y=QualifiedName(
                                                                                                                                 names=[
                                                                                                                                     'Integer']))]),
                                                                                                                 y=IntValue(
                                                                                                                     raw='1')),
                                                                                                   if_false=IntValue(
                                                                                                       raw='0')))])),
    ])
    def test_body_expression(self, text, expected):
        parser = _parser_for_rule('body_expression')
        if isinstance(expected, type) and issubclass(expected, Exception):
            with pytest.raises(expected):
                _ = parser(text)
        else:
            v, rules = parser(text)
            assert v == expected
            assert 'body_expression' in rules

    @pytest.mark.parametrize(['text', 'expected'], [
        ('sensors -> selectSensorsOver(limit)',
         FunctionOperationExpression(entity=QualifiedName(names=['sensors']),
                                     name=QualifiedName(names=['selectSensorsOver']),
                                     arguments=[QualifiedName(names=['limit'])])),
        ('sensors -> selectSensorsOver(limit) -> computeCriticalValue()',
         FunctionOperationExpression(entity=FunctionOperationExpression(entity=QualifiedName(names=['sensors']),
                                                                        name=QualifiedName(names=['selectSensorsOver']),
                                                                        arguments=[QualifiedName(names=['limit'])]),
                                     name=QualifiedName(names=['computeCriticalValue']), arguments=[])),
        ('sensors -> select {in s: Sensor; s::isActive}',
         FunctionOperationExpression(entity=QualifiedName(names=['sensors']), name=QualifiedName(names=['select']),
                                     arguments=[BodyExpression(body=[OwnedFeatureMember(visibility=None,
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
                                                                                                name='s'),
                                                                                            specializations=[
                                                                                                TypingsPart(items=[
                                                                                                    QualifiedName(
                                                                                                        names=[
                                                                                                            'Sensor'])])],
                                                                                            multiplicity=None,
                                                                                            is_ordered=False,
                                                                                            is_nonunique=False,
                                                                                            conjugation=None,
                                                                                            relationships=[],
                                                                                            is_default=False,
                                                                                            value_type=None, value=None,
                                                                                            body=[])),
                                                                     Result(visibility=None, expression=QualifiedName(
                                                                         names=['s', 'isActive']))])])),
        ('members -> reject {in mber: Member; not mber->isInGoodStanding()}',
         FunctionOperationExpression(entity=QualifiedName(names=['members']), name=QualifiedName(names=['reject']),
                                     arguments=[BodyExpression(body=[OwnedFeatureMember(visibility=None,
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
                                                                                                name='mber'),
                                                                                            specializations=[
                                                                                                TypingsPart(items=[
                                                                                                    QualifiedName(
                                                                                                        names=[
                                                                                                            'Member'])])],
                                                                                            multiplicity=None,
                                                                                            is_ordered=False,
                                                                                            is_nonunique=False,
                                                                                            conjugation=None,
                                                                                            relationships=[],
                                                                                            is_default=False,
                                                                                            value_type=None, value=None,
                                                                                            body=[])),
                                                                     Result(visibility=None,
                                                                            expression=UnaryOp(op='not',
                                                                                               x=FunctionOperationExpression(
                                                                                                   entity=QualifiedName(
                                                                                                       names=['mber']),
                                                                                                   name=QualifiedName(
                                                                                                       names=[
                                                                                                           'isInGoodStanding']),
                                                                                                   arguments=[])))])])),
        ('factors -> reduce {in x: Real; in y: Real; x * y}',
         FunctionOperationExpression(entity=QualifiedName(names=['factors']), name=QualifiedName(names=['reduce']),
                                     arguments=[BodyExpression(body=[OwnedFeatureMember(visibility=None,
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
                                                                                                name='x'),
                                                                                            specializations=[
                                                                                                TypingsPart(items=[
                                                                                                    QualifiedName(
                                                                                                        names=[
                                                                                                            'Real'])])],
                                                                                            multiplicity=None,
                                                                                            is_ordered=False,
                                                                                            is_nonunique=False,
                                                                                            conjugation=None,
                                                                                            relationships=[],
                                                                                            is_default=False,
                                                                                            value_type=None, value=None,
                                                                                            body=[])),
                                                                     OwnedFeatureMember(visibility=None,
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
                                                                                                name='y'),
                                                                                            specializations=[
                                                                                                TypingsPart(items=[
                                                                                                    QualifiedName(
                                                                                                        names=[
                                                                                                            'Real'])])],
                                                                                            multiplicity=None,
                                                                                            is_ordered=False,
                                                                                            is_nonunique=False,
                                                                                            conjugation=None,
                                                                                            relationships=[],
                                                                                            is_default=False,
                                                                                            value_type=None, value=None,
                                                                                            body=[])),
                                                                     Result(visibility=None, expression=BinOp(op='*',
                                                                                                              x=QualifiedName(
                                                                                                                  names=[
                                                                                                                      'x']),
                                                                                                              y=QualifiedName(
                                                                                                                  names=[
                                                                                                                      'y'])))])])),
        ("factors -> reduce RealFunctions::'*'",
         FunctionOperationExpression(entity=QualifiedName(names=['factors']), name=QualifiedName(names=['reduce']),
                                     arguments=[QualifiedName(names=['RealFunctions', '*'])])),
    ])
    def test_function_operation_expression(self, text, expected):
        parser = _parser_for_rule('function_operation_expression')
        if isinstance(expected, type) and issubclass(expected, Exception):
            with pytest.raises(expected):
                _ = parser(text)
        else:
            v, rules = parser(text)
            assert v == expected
            # assert 'function_operation_expression' in rules

    @pytest.mark.parametrize(['text', 'expected'], [
        ('interaction Authorization {\n'
         '    end feature client[*] : Computer;\n'
         '    end feature server[*] : Computer;\n'
         '    composite step login;\n'
         '    composite step authorize;\n'
         '    composite succession login then authorize;\n'
         '}',
         Interaction(is_abstract=False, annotations=[], is_all=False,
                     identification=Identification(short_name=None, name='Authorization'), multiplicity_bounds=None,
                     conjugation=None, superclassing=None, relationships=[], body=[OwnedFeatureMember(visibility=None,
                                                                                                      element=Feature(
                                                                                                          direction=None,
                                                                                                          is_abstract=False,
                                                                                                          relationship_type=None,
                                                                                                          is_readonly=False,
                                                                                                          is_derived=False,
                                                                                                          is_end=True,
                                                                                                          annotations=[],
                                                                                                          is_all=False,
                                                                                                          identification=Identification(
                                                                                                              short_name=None,
                                                                                                              name='client'),
                                                                                                          specializations=[
                                                                                                              TypingsPart(
                                                                                                                  items=[
                                                                                                                      QualifiedName(
                                                                                                                          names=[
                                                                                                                              'Computer'])])],
                                                                                                          multiplicity=MultiplicityBounds(
                                                                                                              lower_bound=None,
                                                                                                              upper_bound=InfValue()),
                                                                                                          is_ordered=False,
                                                                                                          is_nonunique=False,
                                                                                                          conjugation=None,
                                                                                                          relationships=[],
                                                                                                          is_default=False,
                                                                                                          value_type=None,
                                                                                                          value=None,
                                                                                                          body=[])),
                                                                                   OwnedFeatureMember(visibility=None,
                                                                                                      element=Feature(
                                                                                                          direction=None,
                                                                                                          is_abstract=False,
                                                                                                          relationship_type=None,
                                                                                                          is_readonly=False,
                                                                                                          is_derived=False,
                                                                                                          is_end=True,
                                                                                                          annotations=[],
                                                                                                          is_all=False,
                                                                                                          identification=Identification(
                                                                                                              short_name=None,
                                                                                                              name='server'),
                                                                                                          specializations=[
                                                                                                              TypingsPart(
                                                                                                                  items=[
                                                                                                                      QualifiedName(
                                                                                                                          names=[
                                                                                                                              'Computer'])])],
                                                                                                          multiplicity=MultiplicityBounds(
                                                                                                              lower_bound=None,
                                                                                                              upper_bound=InfValue()),
                                                                                                          is_ordered=False,
                                                                                                          is_nonunique=False,
                                                                                                          conjugation=None,
                                                                                                          relationships=[],
                                                                                                          is_default=False,
                                                                                                          value_type=None,
                                                                                                          value=None,
                                                                                                          body=[])),
                                                                                   OwnedFeatureMember(visibility=None,
                                                                                                      element=Step(
                                                                                                          direction=None,
                                                                                                          is_abstract=False,
                                                                                                          relationship_type=FeatureRelationshipType.COMPOSITE,
                                                                                                          is_readonly=False,
                                                                                                          is_derived=False,
                                                                                                          is_end=False,
                                                                                                          annotations=[],
                                                                                                          is_all=False,
                                                                                                          identification=Identification(
                                                                                                              short_name=None,
                                                                                                              name='login'),
                                                                                                          specializations=[],
                                                                                                          multiplicity=None,
                                                                                                          is_ordered=False,
                                                                                                          is_nonunique=False,
                                                                                                          conjugation=None,
                                                                                                          relationships=[],
                                                                                                          is_default=False,
                                                                                                          value_type=None,
                                                                                                          value=None,
                                                                                                          body=[])),
                                                                                   OwnedFeatureMember(visibility=None,
                                                                                                      element=Step(
                                                                                                          direction=None,
                                                                                                          is_abstract=False,
                                                                                                          relationship_type=FeatureRelationshipType.COMPOSITE,
                                                                                                          is_readonly=False,
                                                                                                          is_derived=False,
                                                                                                          is_end=False,
                                                                                                          annotations=[],
                                                                                                          is_all=False,
                                                                                                          identification=Identification(
                                                                                                              short_name=None,
                                                                                                              name='authorize'),
                                                                                                          specializations=[],
                                                                                                          multiplicity=None,
                                                                                                          is_ordered=False,
                                                                                                          is_nonunique=False,
                                                                                                          conjugation=None,
                                                                                                          relationships=[],
                                                                                                          is_default=False,
                                                                                                          value_type=None,
                                                                                                          value=None,
                                                                                                          body=[])),
                                                                                   OwnedFeatureMember(visibility=None,
                                                                                                      element=Succession(
                                                                                                          direction=None,
                                                                                                          is_abstract=False,
                                                                                                          relationship_type=FeatureRelationshipType.COMPOSITE,
                                                                                                          is_readonly=False,
                                                                                                          is_derived=False,
                                                                                                          is_end=False,
                                                                                                          annotations=[],
                                                                                                          is_all=False,
                                                                                                          identification=None,
                                                                                                          specializations=[],
                                                                                                          multiplicity=None,
                                                                                                          is_ordered=False,
                                                                                                          is_nonunique=False,
                                                                                                          conjugation=None,
                                                                                                          relationships=[],
                                                                                                          is_all_succession=False,
                                                                                                          first=ConnectorEnd(
                                                                                                              name=None,
                                                                                                              reference=QualifiedName(
                                                                                                                  names=[
                                                                                                                      'login']),
                                                                                                              multiplicity=None),
                                                                                                          then=ConnectorEnd(
                                                                                                              name=None,
                                                                                                              reference=QualifiedName(
                                                                                                                  names=[
                                                                                                                      'authorize']),
                                                                                                              multiplicity=None),
                                                                                                          body=[]))])),
    ])
    def test_interaction(self, text, expected):
        parser = _parser_for_rule('interaction')
        if isinstance(expected, type) and issubclass(expected, Exception):
            with pytest.raises(expected):
                _ = parser(text)
        else:
            v, rules = parser(text)
            assert v == expected
            assert 'interaction' in rules

    @pytest.mark.parametrize(['text', 'expected'], [
        ('flow fuelFlow from fuelTank::fuelOut to engine::fuelIn;',
         ItemFlow(direction=None, is_abstract=False, relationship_type=None, is_readonly=False, is_derived=False,
                  is_end=False, annotations=[], is_all=False,
                  identification=Identification(short_name=None, name='fuelFlow'), specializations=[],
                  multiplicity=None, is_ordered=False, is_nonunique=False, conjugation=None, relationships=[],
                  is_default=False, value_type=None, value=None, is_all_flow=False,
                  end_from=ItemFlowEnd(owned=None, member=QualifiedName(names=['fuelTank', 'fuelOut'])),
                  end_to=ItemFlowEnd(owned=None, member=QualifiedName(names=['engine', 'fuelIn'])), item_feature=None,
                  body=[])),
        ('flow fuelFlow from fuelTank.fuelOut to engine.fuelIn;',
         ItemFlow(direction=None, is_abstract=False, relationship_type=None, is_readonly=False, is_derived=False,
                  is_end=False, annotations=[], is_all=False,
                  identification=Identification(short_name=None, name='fuelFlow'), specializations=[],
                  multiplicity=None, is_ordered=False, is_nonunique=False, conjugation=None, relationships=[],
                  is_default=False, value_type=None, value=None, is_all_flow=False,
                  end_from=ItemFlowEnd(owned=QualifiedName(names=['fuelTank']),
                                       member=QualifiedName(names=['fuelOut'])),
                  end_to=ItemFlowEnd(owned=QualifiedName(names=['engine']), member=QualifiedName(names=['fuelIn'])),
                  item_feature=None, body=[])),
        ('flow of flowingFuel : Fuel from fuelTank.fuelOut to engine.fuelIn;',
         ItemFlow(direction=None, is_abstract=False, relationship_type=None, is_readonly=False, is_derived=False,
                  is_end=False, annotations=[], is_all=False, identification=None, specializations=[],
                  multiplicity=None, is_ordered=False, is_nonunique=False, conjugation=None, relationships=[],
                  is_default=False, value_type=None, value=None, is_all_flow=False,
                  end_from=ItemFlowEnd(owned=QualifiedName(names=['fuelTank']),
                                       member=QualifiedName(names=['fuelOut'])),
                  end_to=ItemFlowEnd(owned=QualifiedName(names=['engine']), member=QualifiedName(names=['fuelIn'])),
                  item_feature=ItemFeature(identification=Identification(short_name=None, name='flowingFuel'),
                                           specializations=[TypingsPart(items=[QualifiedName(names=['Fuel'])])],
                                           multiplicity=None, is_ordered=False, is_nonunique=False, feature_typing=None,
                                           is_default=False, value_type=None, value=None), body=[])),
        ('flow fuelTank.fuelOut to engine.fuelIn;',
         ItemFlow(direction=None, is_abstract=False, relationship_type=None, is_readonly=False, is_derived=False,
                  is_end=False, annotations=[], is_all=False, identification=None, specializations=[],
                  multiplicity=None, is_ordered=False, is_nonunique=False, conjugation=None, relationships=[],
                  is_default=False, value_type=None, value=None, is_all_flow=False,
                  end_from=ItemFlowEnd(owned=QualifiedName(names=['fuelTank']),
                                       member=QualifiedName(names=['fuelOut'])),
                  end_to=ItemFlowEnd(owned=QualifiedName(names=['engine']), member=QualifiedName(names=['fuelIn'])),
                  item_feature=None, body=[])),
        ('flow xxx = 1;',
         ItemFlow(direction=None, is_abstract=False, relationship_type=None, is_readonly=False, is_derived=False,
                  is_end=False, annotations=[], is_all=False,
                  identification=Identification(short_name=None, name='xxx'), specializations=[], multiplicity=None,
                  is_ordered=False, is_nonunique=False, conjugation=None, relationships=[], is_default=False,
                  value_type=FeatureValueType.BIND, value=IntValue(raw='1'), is_all_flow=False, end_from=None,
                  end_to=None, item_feature=None, body=[])),
        ('flow of flowingFuel : Fuel := 2 from fuelOut to fuelIn;',
         ItemFlow(direction=None, is_abstract=False, relationship_type=None, is_readonly=False, is_derived=False,
                  is_end=False, annotations=[], is_all=False, identification=None, specializations=[],
                  multiplicity=None, is_ordered=False, is_nonunique=False, conjugation=None, relationships=[],
                  is_default=False, value_type=None, value=None, is_all_flow=False,
                  end_from=ItemFlowEnd(owned=None, member=QualifiedName(names=['fuelOut'])),
                  end_to=ItemFlowEnd(owned=None, member=QualifiedName(names=['fuelIn'])),
                  item_feature=ItemFeature(identification=Identification(short_name=None, name='flowingFuel'),
                                           specializations=[TypingsPart(items=[QualifiedName(names=['Fuel'])])],
                                           multiplicity=None, is_ordered=False, is_nonunique=False, feature_typing=None,
                                           is_default=False, value_type=FeatureValueType.INITIAL,
                                           value=IntValue(raw='2')), body=[])),
    ])
    def test_item_flow(self, text, expected):
        parser = _parser_for_rule('item_flow')
        if isinstance(expected, type) and issubclass(expected, Exception):
            with pytest.raises(expected):
                _ = parser(text)
        else:
            v, rules = parser(text)
            assert v == expected
            assert 'item_flow' in rules

    @pytest.mark.parametrize(['text', 'expected'], [
        ('succession flow focus.image to shoot.image;',
         SuccessionItemFlow(direction=None, is_abstract=False, relationship_type=None, is_readonly=False,
                            is_derived=False, is_end=False, annotations=[], is_all=False, identification=None,
                            specializations=[], multiplicity=None, is_ordered=False, is_nonunique=False,
                            conjugation=None, relationships=[], is_default=False, value_type=None, value=None,
                            is_all_flow=False, end_from=ItemFlowEnd(owned=QualifiedName(names=['focus']),
                                                                    member=QualifiedName(names=['image'])),
                            end_to=ItemFlowEnd(owned=QualifiedName(names=['shoot']),
                                               member=QualifiedName(names=['image'])), item_feature=None, body=[])),
    ])
    def test_succession_item_flow(self, text, expected):
        parser = _parser_for_rule('succession_item_flow')
        if isinstance(expected, type) and issubclass(expected, Exception):
            with pytest.raises(expected):
                _ = parser(text)
        else:
            v, rules = parser(text)
            assert v == expected
            assert 'succession_item_flow' in rules

    @pytest.mark.parametrize(['text', 'expected'], [
        ('multiplicity m subsets zeroOrMore;',
         MultiplicitySubset(identification=Identification(short_name=None, name='m'),
                            superset=QualifiedName(names=['zeroOrMore']), body=[])),
        ('multiplicity m subsets zeroOrMore {\n    /* 123 */\n}',
         MultiplicitySubset(identification=Identification(short_name=None, name='m'),
                            superset=QualifiedName(names=['zeroOrMore']),
                            body=[NonFeatureMember(visibility=None,
                                                   element=Comment(identification=None, about_list=None, locale=None,
                                                                   comment='/* 123 */'))])),
    ])
    def test_multiplicity_subset(self, text, expected):
        parser = _parser_for_rule('multiplicity_subset')
        if isinstance(expected, type) and issubclass(expected, Exception):
            with pytest.raises(expected):
                _ = parser(text)
        else:
            v, rules = parser(text)
            assert v == expected
            assert 'multiplicity_subset' in rules

    @pytest.mark.parametrize(['text', 'expected'], [
        ('multiplicity zeroOrMore [0..*];',
         MultiplicityRange(identification=Identification(short_name=None, name='zeroOrMore'),
                           multiplicity=MultiplicityBounds(lower_bound=IntValue(raw='0'), upper_bound=InfValue()),
                           body=[])),
    ])
    def test_multiplicity_range(self, text, expected):
        parser = _parser_for_rule('multiplicity_range')
        if isinstance(expected, type) and issubclass(expected, Exception):
            with pytest.raises(expected):
                _ = parser(text)
        else:
            v, rules = parser(text)
            assert v == expected
            assert 'multiplicity_range' in rules

    @pytest.mark.parametrize(['text', 'expected'], [
        ('metaclass SecurityRelated;',
         Metaclass(is_abstract=False, annotations=[], is_all=False,
                   identification=Identification(short_name=None, name='SecurityRelated'), multiplicity_bounds=None,
                   conjugation=None, superclassing=None, relationships=[], body=[])),
        ('metaclass ApprovalAnnotation {\n'
         '    feature approved[1] : Boolean;\n'
         '    feature approver[1] : String;\n'
         '}',
         Metaclass(is_abstract=False, annotations=[], is_all=False,
                   identification=Identification(short_name=None, name='ApprovalAnnotation'), multiplicity_bounds=None,
                   conjugation=None, superclassing=None, relationships=[],
                   body=[
                       OwnedFeatureMember(visibility=None, element=Feature(
                           direction=None, is_abstract=False, relationship_type=None, is_readonly=False,
                           is_derived=False, is_end=False, annotations=[], is_all=False,
                           identification=Identification(short_name=None, name='approved'),
                           specializations=[TypingsPart(items=[QualifiedName(names=['Boolean'])])],
                           multiplicity=MultiplicityBounds(lower_bound=None, upper_bound=IntValue(raw='1')),
                           is_ordered=False, is_nonunique=False, conjugation=None, relationships=[],
                           is_default=False, value_type=None, value=None, body=[])),
                       OwnedFeatureMember(visibility=None, element=Feature(
                           direction=None, is_abstract=False, relationship_type=None, is_readonly=False,
                           is_derived=False, is_end=False, annotations=[], is_all=False,
                           identification=Identification(short_name=None, name='approver'),
                           specializations=[TypingsPart(items=[QualifiedName(names=['String'])])],
                           multiplicity=MultiplicityBounds(lower_bound=None, upper_bound=IntValue(raw='1')),
                           is_ordered=False, is_nonunique=False, conjugation=None, relationships=[],
                           is_default=False, value_type=None, value=None, body=[]))
                   ])),
    ])
    def test_metaclass(self, text, expected):
        parser = _parser_for_rule('metaclass')
        if isinstance(expected, type) and issubclass(expected, Exception):
            with pytest.raises(expected):
                _ = parser(text)
        else:
            v, rules = parser(text)
            assert v == expected
            assert 'metaclass' in rules

    @pytest.mark.parametrize(['text', 'expected'], [
        ('metadata securityDesignAnnotation : SecurityRelated about SecurityDesign;',
         Metadata(annotations=[], identification=Identification(short_name=None, name='securityDesignAnnotation'),
                  superclass=QualifiedName(names=['SecurityRelated']), about=[QualifiedName(names=['SecurityDesign'])],
                  body=[])),
        ('metadata ApprovalAnnotation about Design {\n'
         '    feature redefines approved = true;\n'
         '    feature redefines approver = "John Smith";\n'
         '}',
         Metadata(annotations=[], identification=None, superclass=QualifiedName(names=['ApprovalAnnotation']),
                  about=[QualifiedName(names=['Design'])], body=[
                 MetadataRedefine(name=QualifiedName(names=['approved']), specializations=[], multiplicity=None,
                                  is_ordered=False, is_nonunique=False, is_default=False,
                                  value_type=FeatureValueType.BIND, value=BoolValue(raw='true'), body=[]),
                 MetadataRedefine(name=QualifiedName(names=['approver']), specializations=[], multiplicity=None,
                                  is_ordered=False, is_nonunique=False, is_default=False,
                                  value_type=FeatureValueType.BIND, value=StringValue(raw='"John Smith"'), body=[])])),
        ('metadata ApprovalAnnotation about Design {\n'
         '    approved = true;\n'
         '    approver = "John Smith";\n'
         '}',
         Metadata(annotations=[], identification=None, superclass=QualifiedName(names=['ApprovalAnnotation']),
                  about=[QualifiedName(names=['Design'])], body=[
                 MetadataRedefine(name=QualifiedName(names=['approved']), specializations=[], multiplicity=None,
                                  is_ordered=False, is_nonunique=False, is_default=False,
                                  value_type=FeatureValueType.BIND, value=BoolValue(raw='true'), body=[]),
                 MetadataRedefine(name=QualifiedName(names=['approver']), specializations=[], multiplicity=None,
                                  is_ordered=False, is_nonunique=False, is_default=False,
                                  value_type=FeatureValueType.BIND, value=StringValue(raw='"John Smith"'), body=[])])),
        ('metadata ApprovalAnnotation about Design {\n    approved : Type1 = true;\n}',
         Metadata(annotations=[], identification=None, superclass=QualifiedName(names=['ApprovalAnnotation']),
                  about=[QualifiedName(names=['Design'])], body=[
                 MetadataRedefine(name=QualifiedName(names=['approved']),
                                  specializations=[TypingsPart(items=[QualifiedName(names=['Type1'])])],
                                  multiplicity=None, is_ordered=False, is_nonunique=False, is_default=False,
                                  value_type=FeatureValueType.BIND, value=BoolValue(raw='true'), body=[])])),
        ('@ApprovalAnnotation {\n    approved = true;\n    approver = "John Smith";\n}',
         Metadata(annotations=[], identification=None, superclass=QualifiedName(names=['ApprovalAnnotation']), about=[],
                  body=[MetadataRedefine(name=QualifiedName(names=['approved']), specializations=[], multiplicity=None,
                                         is_ordered=False, is_nonunique=False, is_default=False,
                                         value_type=FeatureValueType.BIND, value=BoolValue(raw='true'), body=[]),
                        MetadataRedefine(name=QualifiedName(names=['approver']), specializations=[], multiplicity=None,
                                         is_ordered=False, is_nonunique=False, is_default=False,
                                         value_type=FeatureValueType.BIND, value=StringValue(raw='"John Smith"'),
                                         body=[])])),
        ('@ApprovalAnnotation {\n'
         '    approved = true;\n'
         '    approver;  // not assigned\n'
         '}',
         Metadata(annotations=[], identification=None, superclass=QualifiedName(names=['ApprovalAnnotation']), about=[],
                  body=[MetadataRedefine(name=QualifiedName(names=['approved']), specializations=[], multiplicity=None,
                                         is_ordered=False, is_nonunique=False, is_default=False,
                                         value_type=FeatureValueType.BIND, value=BoolValue(raw='true'), body=[]),
                        MetadataRedefine(name=QualifiedName(names=['approver']), specializations=[], multiplicity=None,
                                         is_ordered=False, is_nonunique=False, is_default=False, value_type=None,
                                         value=None, body=[])])),
    ])
    def test_metadata_feature(self, text, expected):
        parser = _parser_for_rule('metadata_feature')
        if isinstance(expected, type) and issubclass(expected, Exception):
            with pytest.raises(expected):
                _ = parser(text)
        else:
            v, rules = parser(text)
            assert v == expected
            assert 'metadata_feature' in rules

    @pytest.mark.parametrize(['text', 'expected'], [
        ('filter @Annotations::ApprovalAnnotation and\n'
         '        Annotations::ApprovalAnnotation::approved and\n'
         '        Annotations::ApprovalAnnotation::level > 1;',
         ElementFilter(visibility=None, expression=CondBinOp(
             op='and', x=CondBinOp(op='and',
                                   x=ClsTestOp(op='@', x=None,
                                               y=QualifiedName(names=['Annotations', 'ApprovalAnnotation'])),
                                   y=QualifiedName(names=['Annotations', 'ApprovalAnnotation', 'approved'])),
             y=BinOp(op='>', x=QualifiedName(names=['Annotations', 'ApprovalAnnotation', 'level']),
                     y=IntValue(raw='1'))))),
        ('filter x and y and z > 1;',
         ElementFilter(visibility=None, expression=CondBinOp(
             op='and',
             x=CondBinOp(op='and', x=QualifiedName(names=['x']),
                         y=QualifiedName(names=['y'])),
             y=BinOp(op='>', x=QualifiedName(names=['z']),
                     y=IntValue(raw='1'))))),
        ('filter x and y and z and t > 1;',
         ElementFilter(visibility=None, expression=CondBinOp(
             op='and', x=CondBinOp(op='and', x=CondBinOp(op='and', x=QualifiedName(names=['x']),
                                                         y=QualifiedName(names=['y'])),
                                   y=QualifiedName(names=['z'])),
             y=BinOp(op='>', x=QualifiedName(names=['t']), y=IntValue(raw='1'))))),
        ('filter x and y and z and t;',
         ElementFilter(visibility=None, expression=CondBinOp(
             op='and', x=CondBinOp(op='and', x=CondBinOp(op='and', x=QualifiedName(names=['x']),
                                                         y=QualifiedName(names=['y'])),
                                   y=QualifiedName(names=['z'])),
             y=QualifiedName(names=['t'])))),
        ('private filter x and y and z > 1;',
         ElementFilter(visibility=Visibility.PRIVATE, expression=CondBinOp(
             op='and', x=CondBinOp(op='and', x=QualifiedName(names=['x']), y=QualifiedName(names=['y'])),
             y=BinOp(op='>', x=QualifiedName(names=['z']), y=IntValue(raw='1'))))),
        ('private filter x and y and z and t > 1;',
         ElementFilter(visibility=Visibility.PRIVATE, expression=CondBinOp(
             op='and', x=CondBinOp(op='and', x=CondBinOp(
                 op='and', x=QualifiedName(names=['x']), y=QualifiedName(names=['y'])), y=QualifiedName(names=['z'])),
             y=BinOp(op='>', x=QualifiedName(names=['t']), y=IntValue(raw='1'))))),
        ('filter 2 +3 - 4 * 5;',
         ElementFilter(visibility=None,
                       expression=BinOp(op='-', x=BinOp(op='+', x=IntValue(raw='2'), y=IntValue(raw='3')),
                                        y=BinOp(op='*', x=IntValue(raw='4'), y=IntValue(raw='5'))))),
    ])
    def test_element_filter_member(self, text, expected):
        parser = _parser_for_rule('element_filter_member')
        if isinstance(expected, type) and issubclass(expected, Exception):
            with pytest.raises(expected):
                _ = parser(text)
        else:
            v, rules = parser(text)
            assert v == expected
            assert 'element_filter_member' in rules

    @pytest.mark.parametrize(['text', 'expected'], [
        ('package AddressBooks {\n'
         '    datatype Entry {\n'
         '        feature name[1]: String;\n'
         '        feature address[1]: String;\n'
         '    }\n'
         '    struct AddressBook {\n'
         '        composite feature entries[*]: Entry;\n'
         '    }\n'
         '}',
         Package(annotations=[], identification=Identification(short_name=None, name='AddressBooks'), body=[
             NonFeatureMember(visibility=None, element=DataType(is_abstract=False, annotations=[], is_all=False,
                                                                identification=Identification(short_name=None,
                                                                                              name='Entry'),
                                                                multiplicity_bounds=None, conjugation=None,
                                                                superclassing=None, relationships=[], body=[
                     OwnedFeatureMember(visibility=None,
                                        element=Feature(direction=None, is_abstract=False, relationship_type=None,
                                                        is_readonly=False, is_derived=False, is_end=False,
                                                        annotations=[], is_all=False,
                                                        identification=Identification(short_name=None, name='name'),
                                                        specializations=[
                                                            TypingsPart(items=[QualifiedName(names=['String'])])],
                                                        multiplicity=MultiplicityBounds(lower_bound=None,
                                                                                        upper_bound=IntValue(raw='1')),
                                                        is_ordered=False, is_nonunique=False, conjugation=None,
                                                        relationships=[], is_default=False, value_type=None, value=None,
                                                        body=[])), OwnedFeatureMember(visibility=None,
                                                                                      element=Feature(direction=None,
                                                                                                      is_abstract=False,
                                                                                                      relationship_type=None,
                                                                                                      is_readonly=False,
                                                                                                      is_derived=False,
                                                                                                      is_end=False,
                                                                                                      annotations=[],
                                                                                                      is_all=False,
                                                                                                      identification=Identification(
                                                                                                          short_name=None,
                                                                                                          name='address'),
                                                                                                      specializations=[
                                                                                                          TypingsPart(
                                                                                                              items=[
                                                                                                                  QualifiedName(
                                                                                                                      names=[
                                                                                                                          'String'])])],
                                                                                                      multiplicity=MultiplicityBounds(
                                                                                                          lower_bound=None,
                                                                                                          upper_bound=IntValue(
                                                                                                              raw='1')),
                                                                                                      is_ordered=False,
                                                                                                      is_nonunique=False,
                                                                                                      conjugation=None,
                                                                                                      relationships=[],
                                                                                                      is_default=False,
                                                                                                      value_type=None,
                                                                                                      value=None,
                                                                                                      body=[]))])),
             NonFeatureMember(visibility=None, element=Struct(is_abstract=False, annotations=[], is_all=False,
                                                              identification=Identification(short_name=None,
                                                                                            name='AddressBook'),
                                                              multiplicity_bounds=None, conjugation=None,
                                                              superclassing=None, relationships=[], body=[
                     OwnedFeatureMember(visibility=None, element=Feature(direction=None, is_abstract=False,
                                                                         relationship_type=FeatureRelationshipType.COMPOSITE,
                                                                         is_readonly=False, is_derived=False,
                                                                         is_end=False, annotations=[], is_all=False,
                                                                         identification=Identification(short_name=None,
                                                                                                       name='entries'),
                                                                         specializations=[TypingsPart(
                                                                             items=[QualifiedName(names=['Entry'])])],
                                                                         multiplicity=MultiplicityBounds(
                                                                             lower_bound=None, upper_bound=InfValue()),
                                                                         is_ordered=False, is_nonunique=False,
                                                                         conjugation=None, relationships=[],
                                                                         is_default=False, value_type=None, value=None,
                                                                         body=[]))]))])),
        ('package Annotations {\n'
         '    metaclass ApprovalAnnotation {\n'
         '        feature approved[1] : Boolean;\n'
         '        feature approver[1] : String;\n'
         '        feature level[1] : Natural;\n'
         '    }\n'
         '}',
         Package(annotations=[], identification=Identification(short_name=None, name='Annotations'), body=[
             NonFeatureMember(visibility=None, element=Metaclass(is_abstract=False, annotations=[], is_all=False,
                                                                 identification=Identification(short_name=None,
                                                                                               name='ApprovalAnnotation'),
                                                                 multiplicity_bounds=None, conjugation=None,
                                                                 superclassing=None, relationships=[], body=[
                     OwnedFeatureMember(visibility=None,
                                        element=Feature(direction=None, is_abstract=False, relationship_type=None,
                                                        is_readonly=False, is_derived=False, is_end=False,
                                                        annotations=[], is_all=False,
                                                        identification=Identification(short_name=None, name='approved'),
                                                        specializations=[
                                                            TypingsPart(items=[QualifiedName(names=['Boolean'])])],
                                                        multiplicity=MultiplicityBounds(lower_bound=None,
                                                                                        upper_bound=IntValue(raw='1')),
                                                        is_ordered=False, is_nonunique=False, conjugation=None,
                                                        relationships=[], is_default=False, value_type=None, value=None,
                                                        body=[])), OwnedFeatureMember(visibility=None,
                                                                                      element=Feature(direction=None,
                                                                                                      is_abstract=False,
                                                                                                      relationship_type=None,
                                                                                                      is_readonly=False,
                                                                                                      is_derived=False,
                                                                                                      is_end=False,
                                                                                                      annotations=[],
                                                                                                      is_all=False,
                                                                                                      identification=Identification(
                                                                                                          short_name=None,
                                                                                                          name='approver'),
                                                                                                      specializations=[
                                                                                                          TypingsPart(
                                                                                                              items=[
                                                                                                                  QualifiedName(
                                                                                                                      names=[
                                                                                                                          'String'])])],
                                                                                                      multiplicity=MultiplicityBounds(
                                                                                                          lower_bound=None,
                                                                                                          upper_bound=IntValue(
                                                                                                              raw='1')),
                                                                                                      is_ordered=False,
                                                                                                      is_nonunique=False,
                                                                                                      conjugation=None,
                                                                                                      relationships=[],
                                                                                                      is_default=False,
                                                                                                      value_type=None,
                                                                                                      value=None,
                                                                                                      body=[])),
                     OwnedFeatureMember(visibility=None,
                                        element=Feature(direction=None, is_abstract=False, relationship_type=None,
                                                        is_readonly=False, is_derived=False, is_end=False,
                                                        annotations=[], is_all=False,
                                                        identification=Identification(short_name=None, name='level'),
                                                        specializations=[
                                                            TypingsPart(items=[QualifiedName(names=['Natural'])])],
                                                        multiplicity=MultiplicityBounds(lower_bound=None,
                                                                                        upper_bound=IntValue(raw='1')),
                                                        is_ordered=False, is_nonunique=False, conjugation=None,
                                                        relationships=[], is_default=False, value_type=None, value=None,
                                                        body=[]))]))])),
        ('package UpperLevelApprovals {\n'
         '    // This package imports all direct or indirect members\n'
         '    // of the DesignModel package that have been approved\n'
         '    // at a level greater than 1.\n'
         '    import DesignModel::**;\n'
         '    filter @Annotations::ApprovalAnnotation and\n'
         '        Annotations::ApprovalAnnotation::approved and\n'
         '        Annotations::ApprovalAnnotation::level > 1;\n'
         '}',
         Package(annotations=[], identification=Identification(short_name=None, name='UpperLevelApprovals'), body=[
             Import(visibility=None, is_all=False, is_recursive=True, is_namespace=False,
                    name=QualifiedName(names=['DesignModel']), filters=[], body=[]), ElementFilter(visibility=None,
                                                                                                   expression=CondBinOp(
                                                                                                       op='and',
                                                                                                       x=CondBinOp(
                                                                                                           op='and',
                                                                                                           x=ClsTestOp(
                                                                                                               op='@',
                                                                                                               x=None,
                                                                                                               y=QualifiedName(
                                                                                                                   names=[
                                                                                                                       'Annotations',
                                                                                                                       'ApprovalAnnotation'])),
                                                                                                           y=QualifiedName(
                                                                                                               names=[
                                                                                                                   'Annotations',
                                                                                                                   'ApprovalAnnotation',
                                                                                                                   'approved'])),
                                                                                                       y=BinOp(op='>',
                                                                                                               x=QualifiedName(
                                                                                                                   names=[
                                                                                                                       'Annotations',
                                                                                                                       'ApprovalAnnotation',
                                                                                                                       'level']),
                                                                                                               y=IntValue(
                                                                                                                   raw='1'))))])),
        ('package UpperLevelApprovals {\n'
         '    // Recursively import all annotation data types and all\n'
         '    // features of those types.\n'
         '    import Annotations::**;\n'
         '    // The filter condition for this import applies only to\n'
         '    // elements imported from the DesignModel package.\n'
         '    import DesignModel::**[@ApprovalAnnotation and approved and level > 1];\n'
         '}',
         Package(annotations=[], identification=Identification(short_name=None, name='UpperLevelApprovals'), body=[
             Import(visibility=None, is_all=False, is_recursive=True, is_namespace=False,
                    name=QualifiedName(names=['Annotations']), filters=[], body=[]),
             Import(visibility=None, is_all=False, is_recursive=True, is_namespace=False,
                    name=QualifiedName(names=['DesignModel']), filters=[CondBinOp(op='and', x=CondBinOp(op='and',
                                                                                                        x=ClsTestOp(
                                                                                                            op='@',
                                                                                                            x=None,
                                                                                                            y=QualifiedName(
                                                                                                                names=[
                                                                                                                    'ApprovalAnnotation'])),
                                                                                                        y=QualifiedName(
                                                                                                            names=[
                                                                                                                'approved'])),
                                                                                  y=BinOp(op='>', x=QualifiedName(
                                                                                      names=['level']),
                                                                                          y=IntValue(raw='1')))],
                    body=[])])),
        ('package PackageApprovals {\n'
         '    import Annotations::*;\n'
         '    import KerML::*;\n'
         '    // This imports all structures from the DesignModel that have\n'
         '    // at least one owned feature and have been marked as approved.\n'
         '    import DesignModel::**[@Structure and\n'
         '        Structure::ownedFeature != null and\n'
         '        @ApprovalAnnotation and\n'
         '        ApprovalAnnotation::approved];\n'
         '}',
         Package(annotations=[], identification=Identification(short_name=None, name='PackageApprovals'), body=[
             Import(visibility=None, is_all=False, is_recursive=False, is_namespace=True,
                    name=QualifiedName(names=['Annotations']), filters=[], body=[]),
             Import(visibility=None, is_all=False, is_recursive=False, is_namespace=True,
                    name=QualifiedName(names=['KerML']), filters=[], body=[]),
             Import(visibility=None, is_all=False, is_recursive=True, is_namespace=False,
                    name=QualifiedName(names=['DesignModel']), filters=[CondBinOp(op='and', x=CondBinOp(op='and',
                                                                                                        x=CondBinOp(
                                                                                                            op='and',
                                                                                                            x=ClsTestOp(
                                                                                                                op='@',
                                                                                                                x=None,
                                                                                                                y=QualifiedName(
                                                                                                                    names=[
                                                                                                                        'Structure'])),
                                                                                                            y=BinOp(
                                                                                                                op='!=',
                                                                                                                x=QualifiedName(
                                                                                                                    names=[
                                                                                                                        'Structure',
                                                                                                                        'ownedFeature']),
                                                                                                                y=NullValue())),
                                                                                                        y=ClsTestOp(
                                                                                                            op='@',
                                                                                                            x=None,
                                                                                                            y=QualifiedName(
                                                                                                                names=[
                                                                                                                    'ApprovalAnnotation']))),
                                                                                  y=QualifiedName(
                                                                                      names=['ApprovalAnnotation',
                                                                                             'approved']))],
                    body=[])])),
    ])
    def test_package(self, text, expected):
        parser = _parser_for_rule('package')
        if isinstance(expected, type) and issubclass(expected, Exception):
            with pytest.raises(expected):
                _ = parser(text)
        else:
            v, rules = parser(text)
            assert v == expected
            assert 'package' in rules

    @pytest.mark.parametrize(['text', 'expected'], [
        ('library package AddressBooks {\n'
         '    datatype Entry {\n'
         '        feature name[1]: String;\n'
         '        feature address[1]: String;\n'
         '    }\n'
         '    struct AddressBook {\n'
         '        composite feature entries[*]: Entry;\n'
         '    }\n'
         '}',
         LibraryPackage(annotations=[], identification=Identification(short_name=None, name='AddressBooks'), body=[
             NonFeatureMember(visibility=None, element=DataType(is_abstract=False, annotations=[], is_all=False,
                                                                identification=Identification(short_name=None,
                                                                                              name='Entry'),
                                                                multiplicity_bounds=None, conjugation=None,
                                                                superclassing=None, relationships=[], body=[
                     OwnedFeatureMember(visibility=None,
                                        element=Feature(direction=None, is_abstract=False, relationship_type=None,
                                                        is_readonly=False, is_derived=False, is_end=False,
                                                        annotations=[], is_all=False,
                                                        identification=Identification(short_name=None, name='name'),
                                                        specializations=[
                                                            TypingsPart(items=[QualifiedName(names=['String'])])],
                                                        multiplicity=MultiplicityBounds(lower_bound=None,
                                                                                        upper_bound=IntValue(raw='1')),
                                                        is_ordered=False, is_nonunique=False, conjugation=None,
                                                        relationships=[], is_default=False, value_type=None, value=None,
                                                        body=[])), OwnedFeatureMember(visibility=None,
                                                                                      element=Feature(direction=None,
                                                                                                      is_abstract=False,
                                                                                                      relationship_type=None,
                                                                                                      is_readonly=False,
                                                                                                      is_derived=False,
                                                                                                      is_end=False,
                                                                                                      annotations=[],
                                                                                                      is_all=False,
                                                                                                      identification=Identification(
                                                                                                          short_name=None,
                                                                                                          name='address'),
                                                                                                      specializations=[
                                                                                                          TypingsPart(
                                                                                                              items=[
                                                                                                                  QualifiedName(
                                                                                                                      names=[
                                                                                                                          'String'])])],
                                                                                                      multiplicity=MultiplicityBounds(
                                                                                                          lower_bound=None,
                                                                                                          upper_bound=IntValue(
                                                                                                              raw='1')),
                                                                                                      is_ordered=False,
                                                                                                      is_nonunique=False,
                                                                                                      conjugation=None,
                                                                                                      relationships=[],
                                                                                                      is_default=False,
                                                                                                      value_type=None,
                                                                                                      value=None,
                                                                                                      body=[]))])),
             NonFeatureMember(visibility=None, element=Struct(is_abstract=False, annotations=[], is_all=False,
                                                              identification=Identification(short_name=None,
                                                                                            name='AddressBook'),
                                                              multiplicity_bounds=None, conjugation=None,
                                                              superclassing=None, relationships=[], body=[
                     OwnedFeatureMember(visibility=None, element=Feature(direction=None, is_abstract=False,
                                                                         relationship_type=FeatureRelationshipType.COMPOSITE,
                                                                         is_readonly=False, is_derived=False,
                                                                         is_end=False, annotations=[], is_all=False,
                                                                         identification=Identification(short_name=None,
                                                                                                       name='entries'),
                                                                         specializations=[TypingsPart(
                                                                             items=[QualifiedName(names=['Entry'])])],
                                                                         multiplicity=MultiplicityBounds(
                                                                             lower_bound=None, upper_bound=InfValue()),
                                                                         is_ordered=False, is_nonunique=False,
                                                                         conjugation=None, relationships=[],
                                                                         is_default=False, value_type=None, value=None,
                                                                         body=[]))]))], is_standard=False)),
        ('standard library package ScalarValues {\n'
         '    doc\n'
         '    /*\n'
         '     * This package contains a basic set of primitive scalar '
         '(non-collection) data types. \n'
         '     * These include Boolean and String types and a hierarchy of concrete '
         'Number types, from \n'
         '     * the most general type of Complex numbers to the most specific type of '
         'Positive integers.</p>\n'
         '     */\n'
         '\n'
         '    private import Base::DataValue;\n'
         '\n'
         '    abstract datatype ScalarValue specializes DataValue;\n'
         '    datatype Boolean specializes ScalarValue;\n'
         '    datatype String specializes ScalarValue;\n'
         '    abstract datatype NumericalValue specializes ScalarValue;\n'
         '\n'
         '    abstract datatype Number specializes NumericalValue;\n'
         '    datatype Complex specializes Number;\n'
         '    datatype Real specializes Complex;    \n'
         '    datatype Rational specializes Real;\n'
         '    datatype Integer specializes Rational;\n'
         '    datatype Natural specializes Integer;\n'
         '    datatype Positive specializes Natural;    \n'
         '}',
         LibraryPackage(annotations=[], identification=Identification(short_name=None, name='ScalarValues'), body=[
             NonFeatureMember(visibility=None,
                              element=Documentation(identification=Identification(short_name=None, name=None),
                                                    locale=None,
                                                    comment='/*\n     * This package contains a basic set of primitive scalar (non-collection) data types. \n     * These include Boolean and String types and a hierarchy of concrete Number types, from \n     * the most general type of Complex numbers to the most specific type of Positive integers.</p>\n     */')),
             Import(visibility=Visibility.PRIVATE, is_all=False, is_recursive=False, is_namespace=False,
                    name=QualifiedName(names=['Base', 'DataValue']), filters=[], body=[]),
             NonFeatureMember(visibility=None, element=DataType(is_abstract=True, annotations=[], is_all=False,
                                                                identification=Identification(short_name=None,
                                                                                              name='ScalarValue'),
                                                                multiplicity_bounds=None, conjugation=None,
                                                                superclassing=SuperclassingPart(
                                                                    items=[QualifiedName(names=['DataValue'])]),
                                                                relationships=[], body=[])),
             NonFeatureMember(visibility=None, element=DataType(is_abstract=False, annotations=[], is_all=False,
                                                                identification=Identification(short_name=None,
                                                                                              name='Boolean'),
                                                                multiplicity_bounds=None, conjugation=None,
                                                                superclassing=SuperclassingPart(
                                                                    items=[QualifiedName(names=['ScalarValue'])]),
                                                                relationships=[], body=[])),
             NonFeatureMember(visibility=None, element=DataType(is_abstract=False, annotations=[], is_all=False,
                                                                identification=Identification(short_name=None,
                                                                                              name='String'),
                                                                multiplicity_bounds=None, conjugation=None,
                                                                superclassing=SuperclassingPart(
                                                                    items=[QualifiedName(names=['ScalarValue'])]),
                                                                relationships=[], body=[])),
             NonFeatureMember(visibility=None, element=DataType(is_abstract=True, annotations=[], is_all=False,
                                                                identification=Identification(short_name=None,
                                                                                              name='NumericalValue'),
                                                                multiplicity_bounds=None, conjugation=None,
                                                                superclassing=SuperclassingPart(
                                                                    items=[QualifiedName(names=['ScalarValue'])]),
                                                                relationships=[], body=[])),
             NonFeatureMember(visibility=None, element=DataType(is_abstract=True, annotations=[], is_all=False,
                                                                identification=Identification(short_name=None,
                                                                                              name='Number'),
                                                                multiplicity_bounds=None, conjugation=None,
                                                                superclassing=SuperclassingPart(
                                                                    items=[QualifiedName(names=['NumericalValue'])]),
                                                                relationships=[], body=[])),
             NonFeatureMember(visibility=None, element=DataType(is_abstract=False, annotations=[], is_all=False,
                                                                identification=Identification(short_name=None,
                                                                                              name='Complex'),
                                                                multiplicity_bounds=None, conjugation=None,
                                                                superclassing=SuperclassingPart(
                                                                    items=[QualifiedName(names=['Number'])]),
                                                                relationships=[], body=[])),
             NonFeatureMember(visibility=None, element=DataType(is_abstract=False, annotations=[], is_all=False,
                                                                identification=Identification(short_name=None,
                                                                                              name='Real'),
                                                                multiplicity_bounds=None, conjugation=None,
                                                                superclassing=SuperclassingPart(
                                                                    items=[QualifiedName(names=['Complex'])]),
                                                                relationships=[], body=[])),
             NonFeatureMember(visibility=None, element=DataType(is_abstract=False, annotations=[], is_all=False,
                                                                identification=Identification(short_name=None,
                                                                                              name='Rational'),
                                                                multiplicity_bounds=None, conjugation=None,
                                                                superclassing=SuperclassingPart(
                                                                    items=[QualifiedName(names=['Real'])]),
                                                                relationships=[], body=[])),
             NonFeatureMember(visibility=None, element=DataType(is_abstract=False, annotations=[], is_all=False,
                                                                identification=Identification(short_name=None,
                                                                                              name='Integer'),
                                                                multiplicity_bounds=None, conjugation=None,
                                                                superclassing=SuperclassingPart(
                                                                    items=[QualifiedName(names=['Rational'])]),
                                                                relationships=[], body=[])),
             NonFeatureMember(visibility=None, element=DataType(is_abstract=False, annotations=[], is_all=False,
                                                                identification=Identification(short_name=None,
                                                                                              name='Natural'),
                                                                multiplicity_bounds=None, conjugation=None,
                                                                superclassing=SuperclassingPart(
                                                                    items=[QualifiedName(names=['Integer'])]),
                                                                relationships=[], body=[])),
             NonFeatureMember(visibility=None, element=DataType(is_abstract=False, annotations=[], is_all=False,
                                                                identification=Identification(short_name=None,
                                                                                              name='Positive'),
                                                                multiplicity_bounds=None, conjugation=None,
                                                                superclassing=SuperclassingPart(
                                                                    items=[QualifiedName(names=['Natural'])]),
                                                                relationships=[], body=[]))], is_standard=True)),
    ])
    def test_library_package(self, text, expected):
        parser = _parser_for_rule('library_package')
        if isinstance(expected, type) and issubclass(expected, Exception):
            with pytest.raises(expected):
                _ = parser(text)
        else:
            v, rules = parser(text)
            assert v == expected
            assert 'library_package' in rules

    @pytest.mark.parametrize(['text', 'expected'], [
        ("null", None),  # Valid: null expression
        ("()", None),  # Valid: empty parentheses as null
        ("(  )", None),  # Valid: empty parentheses with whitespace
        ("( )", None),  # Valid: parentheses with space
        ("Null", UnexpectedInput),  # Invalid: case sensitive
        ("NULL", UnexpectedInput),  # Invalid: all caps
        ("(null)", UnexpectedInput),  # Invalid: null in parentheses
        ("(,)", UnexpectedInput),  # Invalid: comma in empty parentheses
        ("(())", UnexpectedInput),  # Invalid: nested empty parentheses
    ])
    def test_null_expression(self, text, expected):
        parser = _parser_for_rule('null_expression')
        if isinstance(expected, type) and issubclass(expected, Exception):
            with pytest.raises(expected):
                _ = parser(text)
        else:
            v, rules = parser(text)
            assert isinstance(v, NullValue)
            assert v.value is None
            assert rules == ['null_expression']

    @pytest.mark.parametrize(['text', 'expected'], [
        ("pkg.metadata", ('pkg',)),  # Valid: simple metadata access
        ("very::long::qualified::name.metadata", ('very', 'long', 'qualified', 'name')),  # Valid: long qualified name
        ("'very long'::qualified::name.metadata", ('very long', 'qualified', 'name')),  # Valid: long qualified name
        ("_package.metadata", ('_package',)),  # Valid: underscore in package name
        ("package123.metadata", ('package123',)),  # Valid: numbers in package name
        ("PACKAGE.metadata", ('PACKAGE',)),  # Valid: uppercase package name
        ("pkg::subpackage.metadata", ('pkg', 'subpackage')),  # Valid: qualified name with double colons

        ("package.metadata", GrammarError),  # Valid: reserved word
        ("package.Metadata", UnexpectedInput),  # Invalid: uppercase 'Metadata'
        ("package.meta_data", UnexpectedInput),  # Invalid: underscore in 'metadata'
        (".metadata", UnexpectedInput),  # Invalid: leading dot
        ("package.", UnexpectedInput),  # Invalid: trailing dot
        ("package..metadata", UnexpectedInput),  # Invalid: double dot
        ("package.metadata.extra", UnexpectedInput),  # Invalid: extra after 'metadata'
        ("package.metaData", UnexpectedInput),  # Invalid: camelCase 'metadata'
    ])
    def test_metadata_access_expression(self, text, expected):
        parser = _parser_for_rule('metadata_access_expression')
        if isinstance(expected, type) and issubclass(expected, Exception):
            with pytest.raises(expected):
                _ = parser(text)
        else:
            v, rules = parser(text)
            assert isinstance(v, MetadataAccessExpression)
            assert v.qualified_name == QualifiedName(list(expected))
            assert set(rules) == {'qualified_name', 'metadata_access_expression'}

    @pytest.mark.parametrize(['text', 'expected'], [
        ("myFeature", ("myFeature",)),  # Valid: simple feature reference
        ("pkg::subpackage::feat", ("pkg", "subpackage", "feat")),  # Valid: qualified name
        ("_underscoreFeature", ("_underscoreFeature",)),  # Valid: underscore in name
        ("feature123", ("feature123",)),  # Valid: numbers in name
        ("pkg::feat::subfeature", ("pkg", "feat", "subfeature")),  # Valid: multiple levels
        ("very::long::qualified::feat::name", ("very", "long", "qualified", "feat", "name")),
        # Valid: many levels
        ("double::colon::feat", ("double", "colon", "feat")),  # Valid: double colons
        ("'double with space'::colon::feat", ('double with space', "colon", "feat")),  # Valid: unrestricted colons

        ("123feature", UnexpectedInput),  # Invalid: starts with number
        ("feat-name", UnexpectedInput),  # Invalid: contains hyphen
        ("feat name", UnexpectedInput),  # Invalid: contains space
        ("::leadingColons", UnexpectedInput),  # Invalid: leading colons
        ("trailingColons::", UnexpectedInput),  # Invalid: trailing colons
        ("single:colon", UnexpectedInput),  # Invalid: single colon
        ("package::subpackage::feature", GrammarError),  # Invalid: preserved word
        ("double with space::colon::feat", UnexpectedInput)  # Invalid: invalid spaces
    ])
    def test_feature_reference_expression(self, text, expected):
        parser = _parser_for_rule('feature_reference_expression')
        if isinstance(expected, type) and issubclass(expected, Exception):
            with pytest.raises(expected):
                _ = parser(text)
        else:
            v, rules = parser(text)
            assert isinstance(v, QualifiedName)
            assert tuple(v.names) == expected
            assert set(rules) == {'qualified_name'}

    @pytest.mark.parametrize(['text', 'expected'], [
        (
                "feat()",
                InvocationExpression(name=QualifiedName(names=['feat']), arguments=[])
        ),  # Valid: empty argument list
        (
                "feat(arg1, arg2)",
                InvocationExpression(
                    name=QualifiedName(names=['feat']),
                    arguments=[QualifiedName(names=['arg1']), QualifiedName(names=['arg2'])]
                )
        ),  # Valid: multiple positional arguments
        (
                "feat(1, \"arg2\")",
                InvocationExpression(
                    name=QualifiedName(names=['feat']),
                    arguments=[IntValue(raw='1'), StringValue(raw='"arg2"')]
                )
        ),  # Valid: literal values

        (
                "f()",
                InvocationExpression(name=QualifiedName(names=['f']), arguments=[]),
        ),  # Valid: empty argument list
        (
                "f(arg1, arg2)",
                InvocationExpression(
                    name=QualifiedName(names=['f']),
                    arguments=[QualifiedName(names=['arg1']), QualifiedName(names=['arg2'])]
                )
        ),  # Valid: multiple positional arguments
        (
                "f(1, \"arg2\")",
                InvocationExpression(
                    name=QualifiedName(names=['f']),
                    arguments=[IntValue(raw='1'), StringValue(raw='"arg2"')]
                ),
        ),  # Valid: literal values

        (
                "feat(name1=value1, name2=value2)",
                InvocationExpression(
                    name=QualifiedName(names=['feat']),
                    arguments=[
                        NamedArgument(name=QualifiedName(names=['name1']), value=QualifiedName(names=['value1'])),
                        NamedArgument(name=QualifiedName(names=['name2']), value=QualifiedName(names=['value2']))
                    ]
                )
        ),  # Valid: named arguments
        (
                "feat(name1=1, name2=\"1\")",
                InvocationExpression(
                    name=QualifiedName(names=['feat']),
                    arguments=[
                        NamedArgument(name=QualifiedName(names=['name1']), value=IntValue(raw='1')),
                        NamedArgument(name=QualifiedName(names=['name2']), value=StringValue(raw='"1"'))
                    ]
                )
        ),  # Valid: literal values
        (
                "feat(name1=1, 'name2 x'=\"1\", name3=null)",
                InvocationExpression(
                    name=QualifiedName(names=['feat']),
                    arguments=[
                        NamedArgument(name=QualifiedName(names=['name1']), value=IntValue(raw='1')),
                        NamedArgument(name=QualifiedName(names=['name2 x']), value=StringValue(raw='"1"')),
                        NamedArgument(name=QualifiedName(names=['name3']), value=NullValue()),
                    ]
                ),
        ),  # Valid: named arguments
        # ("feat((nested))", True),  # Valid: nested parentheses TODO: add this back when expression is fixed
        (
                "feat(very::long::qualified::name=value)",
                InvocationExpression(
                    name=QualifiedName(names=['feat']),
                    arguments=[
                        NamedArgument(
                            name=QualifiedName(names=['very', 'long', 'qualified', 'name']),
                            value=QualifiedName(names=['value'])
                        ),
                    ]
                )
        ),  # Valid: qualified name in named argument

        ("feat(,)", UnexpectedInput),  # Invalid: empty argument with comma
        ("feat(arg1,)", UnexpectedInput),  # Invalid: trailing comma
        ("feat(arg1 arg2)", UnexpectedInput),  # Invalid: missing comma
        ("feat(name1:value1)", UnexpectedInput),  # Invalid: colon instead of equals
        ("feat(=value1)", UnexpectedInput),  # Invalid: missing parameter name
        ("feat(arg1, , arg2)", UnexpectedInput),  # Invalid: double comma
        ("feat(arg1, name2=, arg3)", UnexpectedInput),  # Invalid: incomplete named argument
        ("feat(arg1, name2=value2)", UnexpectedInput),  # Valid: mixed positional and named
    ])
    def test_invocation_expression(self, text, expected):
        parser = _parser_for_rule('invocation_expression')
        if isinstance(expected, type) and issubclass(expected, Exception):
            with pytest.raises(expected):
                _ = parser(text)
        else:
            v, rules = parser(text)
            assert v == expected
            assert 'invocation_expression' in rules
