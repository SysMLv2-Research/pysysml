import re

import pytest

from pysysml.kerml.ast import Env, Element, Relationship, ConstraintsError

uuid4_pattern = re.compile(r'^[a-f0-9]{8}-[a-f0-9]{4}-4[a-f0-9]{3}-[89ab][a-f0-9]{3}-[a-f0-9]{12}$')


def is_valid_uuid4(string):
    return bool(uuid4_pattern.match(string))


@pytest.fixture()
def env():
    return Env()


@pytest.fixture()
def element1(env):
    return Element(
        env=env,
        declared_name='this_is_name',
        declared_short_name='+-*/\'',
    )


@pytest.fixture()
def element2(env):
    return Element(
        env=env,
        declared_name=None,
        declared_short_name='+',
        element_id='element_2',
        is_implied_included=True,
    )


@pytest.fixture()
def element3(env):
    return Element(env=env)


@pytest.mark.unittest
class TestKerMLAstRootBaseElement:
    def test_simple_element1(self, element1, env):
        assert element1.env is env
        assert element1.element_id is not None
        assert is_valid_uuid4(element1.element_id)
        assert element1.name == 'this_is_name'
        assert element1.declared_name == 'this_is_name'
        assert element1.short_name == '+-*/\''
        assert element1.declared_short_name == '+-*/\''
        assert element1.escaped_name() == 'this_is_name'
        assert not element1.is_implied_included
        element1.check_constraints()

    def test_simple_element2(self, element2, env):
        assert element2.env is env
        assert element2.element_id == 'element_2'
        assert element2.name is None
        assert element2.declared_name is None
        assert element2.short_name == '+'
        assert element2.declared_short_name == '+'
        assert element2.escaped_name() == '\'+\''
        assert element2.is_implied_included
        element2.check_constraints()

    def test_simple_element3(self, element3, env):
        assert element3.env is env
        assert element3.element_id is not None
        assert is_valid_uuid4(element3.element_id)
        assert element3.name is None
        assert element3.declared_name is None
        assert element3.short_name is None
        assert element3.declared_short_name is None
        assert element3.escaped_name() is None
        assert not element3.is_implied_included
        element3.check_constraints()


@pytest.fixture()
def e1(env):
    return Element(env)


@pytest.fixture()
def e2(env):
    return Element(env)


@pytest.fixture()
def e3(env):
    return Element(env)


@pytest.fixture()
def r1(e1, e2, env):
    return Relationship(env, sources=[e1], targets=[e2])


@pytest.fixture()
def r2(e1, e2, env):
    return Relationship(
        env,
        sources=[e1],
        targets=[e2],
        owning_related_element=e1,
    )


@pytest.mark.unittest
class TestKerMLAstRootBaseRelationship:
    def test_precondition(self, e1, e2, env):
        assert e1.env is env
        assert e1.owning_relationship is None
        assert e1.owned_relationships == []
        e1.check_constraints()
        assert e2.env is env
        assert e2.owning_relationship is None
        assert e2.owned_relationships == []
        e2.check_constraints()

    def test_simple_r1(self, e1, e2, r1, env):
        assert e1.env is env
        assert e1.owning_relationship is None
        assert e1.owned_relationships == []
        e1.check_constraints()
        assert e2.env is env
        assert e2.owning_relationship is None
        assert e2.owned_relationships == []
        e2.check_constraints()

        assert r1.sources == [e1]
        assert r1.targets == [e2]
        assert r1.related_elements == [e1, e2]
        assert r1.owning_related_element is None
        assert r1.owned_related_elements == []
        assert not r1.is_implied_included
        assert not r1.is_implied
        r1.check_constraints()

    def test_simple_r2(self, e1, e2, r2, env, e3):
        assert e1.env is env
        assert e1.owning_relationship is None
        assert e1.owned_relationships == [r2]
        e1.check_constraints()
        assert e2.env is env
        assert e2.owning_relationship is None
        assert e2.owned_relationships == []
        e2.check_constraints()
        assert e3.env is env
        assert e3.owning_relationship is None
        assert e3.owned_relationships == []
        e3.check_constraints()

        assert r2.sources == [e1]
        assert r2.targets == [e2]
        assert r2.related_elements == [e1, e2]
        assert r2.owning_related_element == e1
        assert r2.owned_related_elements == []
        assert not r2.is_implied_included
        assert not r2.is_implied
        r2.check_constraints()

        r2.owned_related_elements.add(e3)
        assert r2.sources == [e1]
        assert r2.targets == [e2]
        assert r2.related_elements == [e1, e2]
        assert r2.owning_related_element == e1
        assert r2.owned_related_elements == [e3]
        with pytest.raises(ConstraintsError):
            r2.check_constraints()
        assert e3.owning_relationship is r2
        assert e3.owned_relationships == []
        e3.check_constraints()

        r2.targets.add(e3)
        r2.check_constraints()
        assert r2.sources == [e1]
        assert r2.targets == [e2, e3]
        assert r2.related_elements == [e1, e2, e3]
        assert r2.owning_related_element == e1
        assert r2.owned_related_elements == [e3]
        assert e3.owning_relationship is r2
        assert e3.owned_relationships == []
        e3.check_constraints()

        e1.owned_relationships.clear()
        assert e1.owning_relationship is None
        assert e1.owned_relationships == []
        e1.check_constraints()
        assert r2.sources == [e1]
        assert r2.targets == [e2, e3]
        assert r2.related_elements == [e1, e2, e3]
        assert r2.owning_related_element is None
        assert r2.owned_related_elements == [e3]
        r2.check_constraints()

        r2.owned_related_elements.clear()
        assert e3.owning_relationship is None
        assert e3.owned_relationships == []
        e3.check_constraints()
        assert r2.sources == [e1]
        assert r2.targets == [e2, e3]
        assert r2.related_elements == [e1, e2, e3]
        assert r2.owning_related_element is None
        assert r2.owned_related_elements == []
