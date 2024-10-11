import json

from lark import v_args, Tree, Token, GrammarError

from .template import KerMLTransTemplate
from ..base import is_reserved_word
from ..models import BoolValue, IntValue, RealValue, StringValue, InfValue, NullValue, QualifiedName, name_unescape, \
    MetadataAccessExpression, NamedArgument, InvocationExpression, Visibility, FeatureChain, PrefixMetadataAnnotation, \
    Identification, Dependency, Comment, Documentation, TextualRepresentation, Namespace


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


def tree_to_cst(tree: Tree):
    trans = KerMLTransformer()
    return trans.transform(tree)
