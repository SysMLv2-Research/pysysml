from typing import Optional, Union

import pytest

from pysysml.kerml.ast import IElementID, EConn, Env


class TreeNode(IElementID):
    def __init__(self, env: Env, element_id: Optional[str] = None):
        super().__init__(env, element_id)
        self._parents: EConn[TreeNode] = EConn(
            env=self.env, type_=TreeNode,
            fn_add_conj=self._fn_add_to_parents,
            fn_remove_conj=self._fn_remove_from_parents,
        )
        self._children: EConn[TreeNode] = EConn(
            env=self.env, type_=TreeNode,
            fn_add_conj=self._fn_add_to_children,
            fn_remove_conj=self._fn_remove_from_children,
        )

    def _fn_add_to_parents(self, parent: 'TreeNode'):
        parent.children.add(self)

    def _fn_remove_from_parents(self, parent: 'TreeNode'):
        parent.children.remove(self)

    @property
    def parent(self) -> Optional['TreeNode']:
        return self._parents.first()

    @parent.setter
    def parent(self, value: Optional[Union[str, 'TreeNode']]):
        if value is not None:
            self._parents.set_to(value)
        else:
            self._parents.clear()

    def _fn_add_to_children(self, child: 'TreeNode'):
        child.parent = self

    def _fn_remove_from_children(self, child: 'TreeNode'):
        child.parent = None

    @property
    def children(self) -> EConn['TreeNode']:
        return self._children


@pytest.fixture()
def env():
    return Env()


@pytest.mark.unittest
class TestKerMLAstEConnRelations:
    def test_simple(self, env):
        p = TreeNode(env)
        c1 = TreeNode(env)
        c2 = TreeNode(env)
        assert p.parent is None
        assert p.children == []
        assert c1.parent is None
        assert c1.children == []
        assert c2.parent is None
        assert c2.children == []

        p.children.add(c1)
        assert p.parent is None
        assert p.children == [c1]
        assert c1.parent is p
        assert c1.children == []
        assert c2.parent is None
        assert c2.children == []

        c2.parent = p
        assert p.parent is None
        assert p.children == [c1, c2]
        assert c1.parent is p
        assert c1.children == []
        assert c2.parent is p
        assert c2.children == []

        c1.parent = None
        assert p.parent is None
        assert p.children == [c2]
        assert c1.parent is None
        assert c2.children == []
        assert c2.parent is p
        assert c2.children == []

        p.children.remove(c2)
        assert p.parent is None
        assert p.children == []
        assert c1.parent is None
        assert c1.children == []
        assert c2.parent is None
        assert c2.children == []

    def test_recursive_1(self, env):
        p = TreeNode(env)
        assert p.parent is None
        assert p.children == []

        p.children.add(p)
        assert p.parent is p
        assert p.children == [p]

        p.parent = p
        assert p.parent is p
        assert p.children == [p]

        p.parent = None
        assert p.parent is None
        assert p.children == []

    def test_recursive_2(self, env):
        p = TreeNode(env)
        assert p.parent is None
        assert p.children == []

        p.parent = p
        assert p.parent is p
        assert p.children == [p]

        p.children.add(p)
        assert p.parent is p
        assert p.children == [p]

        p.children.remove(p)
        assert p.parent is None
        assert p.children == []

    def test_simple_2(self, env):
        p1 = TreeNode(env)
        p2 = TreeNode(env)
        c = TreeNode(env)
        assert p1.parent is None
        assert p1.children == []
        assert p2.parent is None
        assert p2.children == []
        assert c.parent is None
        assert c.children == []

        c.parent = p1
        assert p1.parent is None
        assert p1.children == [c]
        assert p2.parent is None
        assert p2.children == []
        assert c.parent is p1
        assert c.children == []

        c.parent = p2
        assert p1.parent is None
        assert p1.children == []
        assert p2.parent is None
        assert p2.children == [c]
        assert c.parent is p2
        assert c.children == []

        c.parent = None
        assert p1.parent is None
        assert p1.children == []
        assert p2.parent is None
        assert p2.children == []
        assert c.parent is None
        assert c.children == []
