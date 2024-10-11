from lark import v_args, Tree, Token, GrammarError

from .template import KerMLTransTemplate
from ..base import is_reserved_word


# noinspection PyPep8Naming
class KerMLTransformer(KerMLTransTemplate):
    @v_args(tree=True)
    def NAME(self, token: Token):
        if not token.value.startswith('\'') and is_reserved_word(token.value):
            raise GrammarError(f'Do not use reserved word {token.value!r} as name in KerML.')
        return token


def tree_to_cst(tree: Tree):
    trans = KerMLTransformer()
    return trans.transform(tree)
