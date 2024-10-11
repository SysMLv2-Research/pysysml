from lark import v_args, Tree, Token, GrammarError

from .template import KerMLTransTemplate
from ..base import is_reserved_word
from ..models import BoolValue, IntValue, RealValue, StringValue, InfValue, NullValue, QualifiedName, name_unescape, \
    MetadataAccessExpression, NamedArgument, InvocationExpression


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


def tree_to_cst(tree: Tree):
    trans = KerMLTransformer()
    return trans.transform(tree)
