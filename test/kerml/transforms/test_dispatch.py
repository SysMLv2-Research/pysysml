import pytest

from pysysml.kerml.models import RootNamespace, NonFeatureMember, LibraryPackage, Identification, DataType, \
    OwnedFeatureMember, QualifiedName, MultiplicityBounds, TypingsPart, IntValue, Feature, Struct, \
    FeatureRelationshipType, Classifier, Documentation, InfValue, Visibility, SuperclassingPart, Import
from .base import _parser_for_rule


@pytest.mark.unittest
class TestKerMLTransformsDispatch:
    @pytest.mark.parametrize(['text', 'expected'], [
        ('library package AddressBooks {\n'
         '    datatype Entry {\n'
         '        feature name[1]: String;\n'
         '        feature address[1]: String;\n'
         '    }\n'
         '    struct AddressBook {\n'
         '        composite feature entries[*]: Entry;\n'
         '    }\n'
         '}\n'
         '\n'
         "classifier <'+'> Plus {\n"
         '    doc /* 1 2 3 */\n'
         '}',
         RootNamespace(body=[NonFeatureMember(visibility=None, element=LibraryPackage(annotations=[],
                                                                                      identification=Identification(
                                                                                          short_name=None,
                                                                                          name='AddressBooks'), body=[
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
                                                                                            upper_bound=IntValue(
                                                                                                raw='1')),
                                                            is_ordered=False, is_nonunique=False, conjugation=None,
                                                            relationships=[], is_default=False, value_type=None,
                                                            value=None, body=[])), OwnedFeatureMember(visibility=None,
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
                                                                             identification=Identification(
                                                                                 short_name=None, name='entries'),
                                                                             specializations=[TypingsPart(items=[
                                                                                 QualifiedName(names=['Entry'])])],
                                                                             multiplicity=MultiplicityBounds(
                                                                                 lower_bound=None,
                                                                                 upper_bound=InfValue()),
                                                                             is_ordered=False, is_nonunique=False,
                                                                             conjugation=None, relationships=[],
                                                                             is_default=False, value_type=None,
                                                                             value=None, body=[]))]))],
                                                                                      is_standard=False)),
                             NonFeatureMember(visibility=None,
                                              element=Classifier(is_abstract=False, annotations=[], is_all=False,
                                                                 identification=Identification(short_name='+',
                                                                                               name='Plus'),
                                                                 multiplicity_bounds=None, conjugation=None,
                                                                 superclassing=None, relationships=[], body=[
                                                      NonFeatureMember(visibility=None, element=Documentation(
                                                          identification=Identification(short_name=None, name=None),
                                                          locale=None, comment='/* 1 2 3 */'))]))])),
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
         RootNamespace(body=[NonFeatureMember(visibility=None, element=LibraryPackage(annotations=[],
                                                                                      identification=Identification(
                                                                                          short_name=None,
                                                                                          name='ScalarValues'), body=[
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
                                                                    superclassing=SuperclassingPart(items=[
                                                                        QualifiedName(names=['NumericalValue'])]),
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
                                                                    relationships=[], body=[]))], is_standard=True))])),
    ])
    def test_root_namespace(self, text, expected):
        parser = _parser_for_rule('root_namespace')
        if isinstance(expected, type) and issubclass(expected, Exception):
            with pytest.raises(expected):
                _ = parser(text)
        else:
            v, rules = parser(text)
            assert v == expected
            assert 'root_namespace' in rules
