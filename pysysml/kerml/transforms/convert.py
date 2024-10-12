import json

from lark import v_args, Tree, Token, GrammarError

from .template import KerMLTransTemplate
from ..base import is_reserved_word
from ..models import BoolValue, IntValue, RealValue, StringValue, InfValue, NullValue, QualifiedName, name_unescape, \
    MetadataAccessExpression, NamedArgument, InvocationExpression, Visibility, FeatureChain, PrefixMetadataAnnotation, \
    Identification, Dependency, Comment, Documentation, TextualRepresentation, Namespace, NonFeatureMember, \
    DisjoiningPart, UnioningPart, IntersectingPart, DifferencingPart, MultiplicityBounds, ConjugationPart, \
    SuperclassingPart, Class, Import, SpecializationPart, Type, ChainingPart, InvertingPart, TypeFeaturingPart, \
    TypingsPart, SubsettingsPart, RedefinitionsPart, ReferencesPart, FeatureDirection, FeatureRelationshipType, \
    FeatureValueType, Feature, OwnedFeatureMember, TypeFeatureMember


# noinspection PyPep8Naming
class KerMLTransformer(KerMLTransTemplate):
    @v_args(tree=True)
    def NAME(self, token: Token):
        if not token.value.startswith('\'') and is_reserved_word(token.value):
            raise GrammarError(f'Do not use reserved word {token.value!r} as name in KerML.')
        return token

    @v_args(tree=True)
    def literal_boolean(self, tree: Tree):
        assert len(tree.children) == 1
        token: Token = tree.children[0]
        return BoolValue(token.value)

    @v_args(tree=True)
    def literal_integer(self, tree: Tree):
        assert len(tree.children) == 1
        token: Token = tree.children[0]
        return IntValue(token.value)

    @v_args(tree=True)
    def literal_real(self, tree: Tree):
        assert len(tree.children) == 1
        token: Token = tree.children[0]
        return RealValue(token.value)

    @v_args(tree=True)
    def literal_string(self, tree: Tree):
        assert len(tree.children) == 1
        token: Token = tree.children[0]
        return StringValue(token.value)

    @v_args(tree=True)
    def literal_infinity(self, tree: Tree):
        return InfValue()

    @v_args(tree=True)
    def null_expression(self, tree: Tree):
        return NullValue()

    @v_args(tree=True)
    def qualified_name(self, tree: Tree):
        assert len(tree.children) > 0
        return QualifiedName([name_unescape(item.value) for item in tree.children])

    @v_args(tree=True)
    def metadata_access_expression(self, tree: Tree):
        assert len(tree.children) == 1
        return MetadataAccessExpression(tree.children[0])

    @v_args(tree=True)
    def invocation_expression(self, tree: Tree):
        assert len(tree.children) == 2
        return InvocationExpression(
            name=tree.children[0],
            arguments=tree.children[1],
        )

    @v_args(tree=True)
    def argument_list(self, tree: Tree):
        if tree.children:
            return tree.children[0]
        else:
            return []

    @v_args(tree=True)
    def named_argument(self, tree: Tree):
        assert len(tree.children) == 2
        return NamedArgument(name=tree.children[0], value=tree.children[1])

    @v_args(tree=True)
    def named_argument_list(self, tree: Tree):
        return tree.children

    @v_args(tree=True)
    def positional_argument_list(self, tree: Tree):
        return tree.children

    @v_args(tree=True)
    def visibility_indicator(self, tree: Tree):
        return Visibility.load(tree.children[0])

    @v_args(tree=True)
    def member_prefix(self, tree: Tree):
        if tree.children:
            return tree.children[0]
        else:
            return None

    @v_args(tree=True)
    def feature_chain(self, tree: Tree):
        return FeatureChain(tree.children)

    @v_args(tree=True)
    def prefix_metadata_annotation(self, tree: Tree):
        assert len(tree.children) == 1
        return PrefixMetadataAnnotation(tree.children[0])

    @v_args(tree=True)
    def prefix_metadata_member(self, tree: Tree):
        assert len(tree.children) == 1
        return PrefixMetadataAnnotation(tree.children[0])

    @v_args(tree=True)
    def dependency_list(self, tree: Tree):
        return tree.children

    @v_args(tree=True)
    def dependency_annotation_list(self, tree: Tree):
        return tree.children

    @v_args(tree=True)
    def dependency(self, tree: Tree):
        assert len(tree.children) == 5
        return Dependency(
            annotations=tree.children[0],
            identification=tree.children[1],
            from_list=tree.children[2],
            to_list=tree.children[3],
            body=tree.children[4],
        )

    @v_args(tree=True)
    def identification(self, tree: Tree):
        assert len(tree.children) == 2
        return Identification(
            short_name=name_unescape(tree.children[0].value) if tree.children[0] is not None else None,
            name=name_unescape(tree.children[1].value) if tree.children[1] is not None else None,
        )

    @v_args(tree=True)
    def comment_about_list(self, tree: Tree):
        return tree.children

    @v_args(tree=True)
    def comment_prefix(self, tree: Tree):
        assert len(tree.children) == 2
        identification, about_list = tree.children
        return identification, about_list

    @v_args(tree=True)
    def comment(self, tree: Tree):
        assert len(tree.children) == 3
        if tree.children[0]:
            identification, about_list = tree.children[0]
        else:
            identification, about_list = None, None

        return Comment(
            identification=identification,
            about_list=about_list,
            locale=tree.children[1],
            comment=tree.children[2].value,
        )

    @v_args(tree=True)
    def documentation(self, tree: Tree):
        assert len(tree.children) == 3
        return Documentation(
            identification=tree.children[0],
            locale=tree.children[1],
            comment=tree.children[2].value,
        )

    @v_args(tree=True)
    def locale(self, tree: Tree):
        assert len(tree.children) == 1
        token: Token = tree.children[0]
        return json.loads(token.value)

    @v_args(tree=True)
    def relationship_body(self, tree: Tree):
        return tree.children

    @v_args(tree=True)
    def textual_representation_rep(self, tree: Tree):
        assert len(tree.children) == 1
        return tree.children[0]

    @v_args(tree=True)
    def textual_representation(self, tree: Tree):
        assert len(tree.children) == 3
        return TextualRepresentation(
            identification=tree.children[0],
            language=name_unescape(tree.children[1].value) if tree.children[1] is not None else None,
            comment=tree.children[2].value,
        )

    @v_args(tree=True)
    def namespace_declaration(self, tree: Tree):
        assert len(tree.children) == 1
        return tree.children[0]

    @v_args(tree=True)
    def namespace_body(self, tree: Tree):
        return tree.children

    @v_args(tree=True)
    def namespace(self, tree: Tree):
        assert len(tree.children) >= 2
        return Namespace(
            annotations=tree.children[:-2],
            identification=tree.children[-2],
            body=tree.children[-1],
        )

    @v_args(tree=True)
    def non_feature_member(self, tree: Tree):
        assert len(tree.children) == 2
        return NonFeatureMember(
            visibility=tree.children[0],
            element=tree.children[1],
        )

    @v_args(tree=True)
    def abstract_type_prefix(self, tree: Tree):
        return True, tree.children

    @v_args(tree=True)
    def non_abstract_type_prefix(self, tree: Tree):
        return False, tree.children

    @v_args(tree=True)
    def all_classifier_declaration(self, tree: Tree):
        return True, tree.children[0], tree.children[1], tree.children[2], tree.children[3:]

    @v_args(tree=True)
    def non_all_classifier_declaration(self, tree: Tree):
        return False, tree.children[0], tree.children[1], tree.children[2], tree.children[3:]

    @v_args(tree=True)
    def disjoining_part(self, tree: Tree):
        return DisjoiningPart(items=tree.children)

    @v_args(tree=True)
    def unioning_part(self, tree: Tree):
        return UnioningPart(items=tree.children)

    @v_args(tree=True)
    def intersecting_part(self, tree: Tree):
        return IntersectingPart(items=tree.children)

    @v_args(tree=True)
    def differencing_part(self, tree: Tree):
        return DifferencingPart(items=tree.children)

    @v_args(tree=True)
    def conjugation_part(self, tree: Tree):
        assert len(tree.children) == 2
        assert tree.children[0].type == 'CONJUGATES'
        return ConjugationPart(item=tree.children[1])

    @v_args(tree=True)
    def superclassing_part(self, tree: Tree):
        assert len(tree.children) > 1
        assert tree.children[0].type == 'SPECIALIZES'
        return SuperclassingPart(items=tree.children[1:])

    @v_args(tree=True)
    def specialization_part(self, tree: Tree):
        assert len(tree.children) > 1
        assert tree.children[0].type == 'SPECIALIZES'
        return SpecializationPart(items=tree.children[1:])

    @v_args(tree=True)
    def class_statement(self, tree: Tree):
        assert len(tree.children) == 3
        is_abstract, annotations = tree.children[0]
        is_all, identification, multiplicity_bounds, spx, type_relationship_parts = tree.children[1]
        if spx is None:
            conjugation, superclassing = None, None
        elif isinstance(spx, SuperclassingPart):
            conjugation, superclassing = None, spx
        elif isinstance(spx, ConjugationPart):
            conjugation, superclassing = spx, None
        else:
            assert False, "Should not reach this line"  # pragma: no cover

        return Class(
            is_abstract=is_abstract,
            annotations=annotations,
            is_all=is_all,
            identification=identification,
            multiplicity_bounds=multiplicity_bounds,
            conjugation=conjugation,
            superclassing=superclassing,
            relationships=type_relationship_parts,
            body=tree.children[2],
        )

    @v_args(tree=True)
    def type_body(self, tree: Tree):
        return tree.children

    @v_args(tree=True)
    def multiplicity_bounds(self, tree: Tree):
        assert len(tree.children) == 2
        return MultiplicityBounds(
            lower_bound=tree.children[0],
            upper_bound=tree.children[1],
        )

    @v_args(tree=True)
    def filter_package_list(self, tree: Tree):
        return tree.children

    @v_args(tree=True)
    def non_recursive_membership_import(self, tree: Tree):
        assert len(tree.children) == 1
        return False, False, tree.children[0]

    @v_args(tree=True)
    def recursive_membership_import(self, tree: Tree):
        assert len(tree.children) == 1
        return True, False, tree.children[0]

    @v_args(tree=True)
    def non_recursive_namespace_import(self, tree: Tree):
        assert len(tree.children) == 1
        return False, True, tree.children[0]

    @v_args(tree=True)
    def recursive_namespace_import(self, tree: Tree):
        assert len(tree.children) == 1
        return True, True, tree.children[0]

    @v_args(tree=True)
    def import_declaration(self, tree: Tree):
        return tree.children

    @v_args(tree=True)
    def import_statement(self, tree: Tree):
        assert len(tree.children) == 4
        visibility, is_all, ((is_recursive, is_namespace, import_name), filter_list), body = tree.children
        return Import(
            visibility=visibility,
            is_all=bool(is_all),
            is_recursive=is_recursive,
            is_namespace=is_namespace,
            name=import_name,
            filters=filter_list,
            body=body,
        )

    @v_args(tree=True)
    def type_declaration(self, tree: Tree):
        return bool(tree.children[0]), tree.children[1], tree.children[2], tree.children[3], tree.children[4:]

    @v_args(tree=True)
    def type(self, tree: Tree):
        assert len(tree.children) == 3
        (is_abstract, annotations), (is_all, identification, multiplicity_bounds,
                                     spx, type_relationship_parts), body = tree.children
        if spx is None:
            conjugation, specialization = None, None
        elif isinstance(spx, SpecializationPart):
            conjugation, specialization = None, spx
        elif isinstance(spx, ConjugationPart):
            conjugation, specialization = spx, None
        else:
            assert False, "Should not reach this line"  # pragma: no cover

        return Type(
            is_abstract=is_abstract,
            annotations=annotations,
            is_all=is_all,
            identification=identification,
            multiplicity_bounds=multiplicity_bounds,
            conjugation=conjugation,
            specialization=specialization,
            relationships=type_relationship_parts,
            body=tree.children[2],
        )

    @v_args(tree=True)
    def explicit_identification_plain(self, tree: Tree):
        assert len(tree.children) == 1
        return Identification(
            short_name=None,
            name=name_unescape(tree.children[0].value) if tree.children[0] is not None else None,
        )

    @v_args(tree=True)
    def explicit_identification_with_short(self, tree: Tree):
        assert len(tree.children) == 2
        return Identification(
            short_name=name_unescape(tree.children[0].value),
            name=name_unescape(tree.children[1].value) if tree.children[1] is not None else None,
        )

    @v_args(tree=True)
    def chaining_part(self, tree: Tree):
        assert len(tree.children) == 1
        return ChainingPart(item=tree.children[0])

    @v_args(tree=True)
    def inverting_part(self, tree: Tree):
        assert len(tree.children) == 1
        return InvertingPart(item=tree.children[0])

    @v_args(tree=True)
    def type_featuring_part(self, tree: Tree):
        return TypeFeaturingPart(items=tree.children)

    @v_args(tree=True)
    def feature_declaration_idx(self, tree: Tree):
        assert len(tree.children) == 2
        if isinstance(tree.children[1], ConjugationPart):
            return tree.children[0], None, tree.children[1]
        else:
            return tree.children[0], tree.children[1], None

    @v_args(tree=True)
    def feature_declaration_spc(self, tree: Tree):
        assert len(tree.children) == 1
        return None, tree.children[0], None

    @v_args(tree=True)
    def feature_declaration_coj(self, tree: Tree):
        assert len(tree.children) == 1
        return None, None, tree.children[0]

    @v_args(tree=True)
    def typed_by(self, tree: Tree):
        assert len(tree.children) == 2
        return tree.children[1]

    @v_args(tree=True)
    def typings(self, tree: Tree):
        return TypingsPart(items=tree.children)

    @v_args(tree=True)
    def subsets(self, tree: Tree):
        assert len(tree.children) == 2
        return tree.children[1]

    @v_args(tree=True)
    def subsettings(self, tree: Tree):
        return SubsettingsPart(items=tree.children)

    @v_args(tree=True)
    def references(self, tree: Tree):
        assert len(tree.children) == 2
        return ReferencesPart(item=tree.children[1])

    @v_args(tree=True)
    def redefines(self, tree: Tree):
        assert len(tree.children) == 2
        return tree.children[1]

    @v_args(tree=True)
    def redefinitions(self, tree: Tree):
        return RedefinitionsPart(items=tree.children)

    @v_args(tree=True)
    def multiplicity_part(self, tree: Tree):
        multiplicity = None
        is_ordered, is_nonunique = False, False
        for item in tree.children:
            if isinstance(item, MultiplicityBounds):
                multiplicity = item
            elif item == 'ordered':
                is_ordered = True
            elif item == 'nonunique':
                is_nonunique = True
            else:
                assert False, 'Should not reach this line.'  # pragma: no cover

        return multiplicity, is_ordered, is_nonunique

    @v_args(tree=True)
    def feature_specialization_part(self, tree: Tree):
        items = []
        multiplicity, is_ordered, is_nonunique = None, False, False
        for item in tree.children:
            if isinstance(item, tuple):
                multiplicity, is_ordered, is_nonunique = item
            else:
                items.append(item)

        return items, multiplicity, is_ordered, is_nonunique

    @v_args(tree=True)
    def feature_declaration(self, tree: Tree):
        assert len(tree.children) >= 2
        is_all = bool(tree.children[0])
        identification, spc, conj = tree.children[1]
        specs, multiplicity, is_ordered, is_nonunique = ([], None, False, False) if spc is None else spc
        relationships = tree.children[2:]
        return is_all, identification, specs, (multiplicity, is_ordered, is_nonunique), conj, relationships

    @v_args(tree=True)
    def feature_direction(self, tree: Tree):
        assert len(tree.children) == 1
        return FeatureDirection.load(tree.children[0].type)

    @v_args(tree=True)
    def feature_relationship_type(self, tree: Tree):
        assert len(tree.children) == 1
        return FeatureRelationshipType.load(tree.children[0].type)

    @v_args(tree=True)
    def feature_prefix(self, tree: Tree):
        direction = None
        is_abstract = False
        relationship_type = None
        is_readonly, is_derived, is_end = False, False, False
        annotations = []
        for item in tree.children:
            if isinstance(item, FeatureDirection):
                direction = item
            elif item == 'abstract':
                is_abstract = True
            elif isinstance(item, FeatureRelationshipType):
                relationship_type = item
            elif item == "readonly":
                is_readonly = True
            elif item == "derived":
                is_derived = True
            elif item == "end":
                is_end = True
            elif isinstance(item, PrefixMetadataAnnotation):
                annotations.append(item)
            else:
                assert False, 'Should not reach this line'  # pragma: no cover

        return direction, is_abstract, relationship_type, is_readonly, is_derived, is_end, annotations

    @v_args(tree=True)
    def fv_bind(self, tree: Tree):
        return False, FeatureValueType.BIND

    @v_args(tree=True)
    def fv_initial(self, tree: Tree):
        return False, FeatureValueType.INITIAL

    @v_args(tree=True)
    def fv_default_bind(self, tree: Tree):
        return True, FeatureValueType.BIND

    @v_args(tree=True)
    def fv_default_initial(self, tree: Tree):
        return True, FeatureValueType.INITIAL

    @v_args(tree=True)
    def feature_value(self, tree: Tree):
        assert len(tree.children) == 2
        is_default, value_type = tree.children[0]
        return is_default, value_type, tree.children[1]

    @v_args(tree=True)
    def feature(self, tree: Tree):
        assert len(tree.children) == 4
        prefix, declaration, value, body = tree.children
        direction, is_abstract, relationship_type, is_readonly, is_derived, is_end, annotations = prefix
        is_all, identification, specs, (multiplicity, is_ordered, is_nonunique), conj, relationships = declaration
        if value is not None:
            is_default, value_type, v = value
        else:
            is_default, value_type, v = False, None, None

        return Feature(
            direction=direction,
            is_abstract=is_abstract,
            relationship_type=relationship_type,
            is_readonly=is_readonly,
            is_derived=is_derived,
            is_end=is_end,
            annotations=annotations,

            is_all=is_all,
            identification=identification,
            specializations=specs,
            multiplicity=multiplicity,
            is_ordered=is_ordered,
            is_nonunique=is_nonunique,
            conjugation=conj,
            relationships=relationships,

            is_default=is_default,
            value_type=value_type,
            value=v,

            body=body,
        )

    @v_args(tree=True)
    def owned_feature_member(self, tree: Tree):
        assert len(tree.children) == 2
        return OwnedFeatureMember(
            visibility=tree.children[0],
            element=tree.children[1],
        )

    @v_args(tree=True)
    def type_feature_member(self, tree: Tree):
        assert len(tree.children) == 2
        return TypeFeatureMember(
            visibility=tree.children[0],
            element=tree.children[1],
        )


def tree_to_cst(tree: Tree):
    trans = KerMLTransformer()
    return trans.transform(tree)
