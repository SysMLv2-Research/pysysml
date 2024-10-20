import pytest

from pysysml.kerml.ast import Element, Dependency, ConstraintsError, Env


@pytest.fixture()
def env():
    return Env()


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
def d1(e1, e2, env):
    return Dependency(
        env,
        clients=[e1],
        suppliers=[e2],
        owning_related_element=e1,
    )


@pytest.fixture()
def d2(e1, e2, env):
    return Dependency(
        env,
        clients=[],
        suppliers=[],
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

    def test_simple_d1(self, e1, e2, d1, env, e3):
        assert e1.env is env
        assert e1.owning_relationship is None
        assert e1.owned_relationships == [d1]
        e1.check_constraints()
        assert e2.env is env
        assert e2.owning_relationship is None
        assert e2.owned_relationships == []
        e2.check_constraints()
        assert e3.env is env
        assert e3.owning_relationship is None
        assert e3.owned_relationships == []
        e3.check_constraints()

        assert d1.sources == d1.clients == [e1]
        assert d1.targets == d1.suppliers == [e2]
        assert d1.related_elements == [e1, e2]
        assert d1.owning_related_element == e1
        assert d1.owned_related_elements == []
        assert not d1.is_implied_included
        assert not d1.is_implied
        d1.check_constraints()

        d1.owned_related_elements.add(e3)
        assert d1.sources == d1.clients == [e1]
        assert d1.targets == d1.suppliers == [e2]
        assert d1.related_elements == [e1, e2]
        assert d1.owning_related_element == e1
        assert d1.owned_related_elements == [e3]
        with pytest.raises(ConstraintsError):
            d1.check_constraints()
        assert e3.owning_relationship is d1
        assert e3.owned_relationships == []
        e3.check_constraints()

        d1.targets.add(e3)
        d1.check_constraints()
        assert d1.sources == d1.clients == [e1]
        assert d1.targets == d1.suppliers == [e2, e3]
        assert d1.related_elements == [e1, e2, e3]
        assert d1.owning_related_element == e1
        assert d1.owned_related_elements == [e3]
        assert e3.owning_relationship is d1
        assert e3.owned_relationships == []
        e3.check_constraints()

        e1.owned_relationships.clear()
        assert e1.owning_relationship is None
        assert e1.owned_relationships == []
        e1.check_constraints()
        assert d1.sources == d1.clients == [e1]
        assert d1.targets == d1.suppliers == [e2, e3]
        assert d1.related_elements == [e1, e2, e3]
        assert d1.owning_related_element is None
        assert d1.owned_related_elements == [e3]
        d1.check_constraints()

        d1.owned_related_elements.clear()
        assert e3.owning_relationship is None
        assert e3.owned_relationships == []
        e3.check_constraints()
        assert d1.sources == d1.clients == [e1]
        assert d1.targets == d1.suppliers == [e2, e3]
        assert d1.related_elements == [e1, e2, e3]
        assert d1.owning_related_element is None
        assert d1.owned_related_elements == []

    def test_simple_d2(self, e1, e2, d2, env):
        assert d2.sources == d2.clients == []
        assert d2.targets == d2.suppliers == []
        assert d2.related_elements == []
        assert d2.owning_related_element is None
        assert d2.owned_related_elements == []
        with pytest.raises(ConstraintsError):
            d2.check_constraints()

        d2.clients.add(e2)
        assert d2.sources == d2.clients == [e2]
        assert d2.targets == d2.suppliers == []
        assert d2.related_elements == [e2]
        assert d2.owning_related_element is None
        assert d2.owned_related_elements == []
        with pytest.raises(ConstraintsError):
            d2.check_constraints()

        d2.suppliers.add(e1)
        assert d2.sources == d2.clients == [e2]
        assert d2.targets == d2.suppliers == [e1]
        assert d2.related_elements == [e2, e1]
        assert d2.owning_related_element is None
        assert d2.owned_related_elements == []
        d2.check_constraints()
