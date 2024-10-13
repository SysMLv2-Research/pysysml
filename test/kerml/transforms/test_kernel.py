import pytest

from pysysml.kerml.models import Class, Identification, PrefixMetadataAnnotation, QualifiedName, SuperclassingPart, \
    MultiplicityBounds, IntValue, ConjugationPart, DisjoiningPart, UnioningPart, IntersectingPart, DifferencingPart, \
    NonFeatureMember, Documentation, Comment, OwnedFeatureMember, Feature, TypingsPart, DataType, Struct, \
    FeatureRelationshipType, InfValue, Association, AssociationStruct, Connector, ConnectorType, ConnectorEnd, \
    FeatureChain, FeatureValueType, BindingConnector, Succession, Behavior, Step
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
    @pytest.mark.focus
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
    @pytest.mark.focus
    def test_step(self, text, expected):
        parser = _parser_for_rule('step')
        if isinstance(expected, type) and issubclass(expected, Exception):
            with pytest.raises(expected):
                _ = parser(text)
        else:
            v, rules = parser(text)
            assert v == expected
            assert 'step' in rules
