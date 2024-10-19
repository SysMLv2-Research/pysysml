from typing import Optional

import pytest

from pysysml.kerml.ast import IElementID, EConn, Env


class Person(IElementID):
    def __init__(self, env: Env, element_id: Optional[str] = None):
        super().__init__(env, element_id)
        self._friends: EConn[Person] = EConn(
            env=env, type_=Person,
            fn_add_conj=self._fn_add_to_friends,
            fn_remove_conj=self._fn_remove_from_friends,
        )

    def _fn_add_to_friends(self, friend: 'Person'):
        friend.friends.add(self)

    def _fn_remove_from_friends(self, friend: 'Person'):
        friend.friends.remove(self)

    @property
    def friends(self) -> EConn['Person']:
        return self._friends


@pytest.fixture()
def env():
    return Env()


@pytest.mark.unittest
class TestKerMLAstEConnFriends:
    def test_simple(self, env):
        p1 = Person(env)
        p2 = Person(env)
        assert p1.friends == []
        assert p2.friends == []

        p1.friends.add(p2)
        assert p1.friends == [p2]
        assert p2.friends == [p1]

        p2.friends.remove(p1)
        assert p1.friends == []
        assert p2.friends == []

    def test_self(self, env):
        p1 = Person(env)
        assert p1.friends == []

        p1.friends.add(p1)
        assert p1.friends == [p1]

        p1.friends.remove(p1)
        assert p1.friends == []

    def test_3_person(self, env):
        p1 = Person(env)
        p2 = Person(env)
        p3 = Person(env)
        assert p1.friends == []
        assert p2.friends == []
        assert p3.friends == []

        p1.friends.add(p2)
        assert p1.friends == [p2]
        assert p2.friends == [p1]
        assert p3.friends == []

        p3.friends.update([p1, p2])
        assert p1.friends == [p2, p3]
        assert p2.friends == [p1, p3]
        assert p3.friends == [p1, p2]

        p1.friends.clear()
        assert p1.friends == []
        assert p2.friends == [p3]
        assert p3.friends == [p2]

        p3.friends.set_to(p1)
        assert p1.friends == [p3]
        assert p2.friends == []
        assert p3.friends == [p1]
