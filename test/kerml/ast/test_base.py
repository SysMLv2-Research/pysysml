import uuid

import pytest

from pysysml.kerml.ast import Env, IElementID, ConstraintsError, EList, EFrozenList


@pytest.fixture
def env():
    return Env()


@pytest.fixture
def mock_element(env):
    class MockElement(IElementID):
        pass

    return lambda: MockElement(env)


@pytest.mark.unittest
class TestEnvAndElementID:
    def test_env_init(self, env):
        assert len(env) == 0

    def test_env_add_element(self, env, mock_element):
        element = mock_element()
        env.add(element)
        assert len(env) == 1
        assert element.element_id in env

    def test_env_getitem(self, env, mock_element):
        element = mock_element()
        env.add(element)
        assert env[element.element_id] == element
        assert env[element] == element

    def test_env_setitem(self, env, mock_element):
        element = mock_element()
        env[element.element_id] = element
        assert len(env) == 1
        assert element.element_id in env

    def test_env_delitem(self, env, mock_element):
        element = mock_element()
        env.add(element)
        del env[element.element_id]
        assert len(env) == 0
        assert element.element_id not in env

    def test_env_contains(self, env, mock_element):
        element = mock_element()
        env.add(element)
        assert element.element_id in env
        assert element in env

    def test_env_len(self, env, mock_element):
        env.add(mock_element())
        env.add(mock_element())
        print(env)
        assert len(env) == 2

    def test_env_repr(self, env, mock_element):
        env.add(mock_element())
        assert repr(env).startswith("<Env ")
        assert "1 item" in repr(env)

    def test_element_id_init(self, env):
        element = IElementID(env)
        assert element.env == env
        assert isinstance(element.element_id, str)

    def test_element_id_custom_id(self, env):
        custom_id = str(uuid.uuid4())
        element = IElementID(env, element_id=custom_id)
        assert element.element_id == custom_id

    def test_constraints_error(self):
        with pytest.raises(ConstraintsError):
            raise ConstraintsError


@pytest.mark.unittest
class TestEList:
    def test_elist_init(self, env, mock_element):
        elements = [mock_element() for _ in range(3)]
        elist = EList(env, elements)
        assert len(elist) == 3
        assert all(isinstance(e, IElementID) for e in elist)

    def test_elist_getitem(self, env, mock_element):
        elements = [mock_element() for _ in range(3)]
        elist = EList(env, elements)
        assert elist[0] == elements[0]
        assert isinstance(elist[1:], EList)

    def test_elist_setitem(self, env, mock_element):
        elist = EList(env, [mock_element() for _ in range(3)])
        new_element = mock_element()
        elist[1] = new_element
        assert elist[1] == new_element

    def test_elist_insert(self, env, mock_element):
        elist = EList(env, [mock_element() for _ in range(2)])
        new_element = mock_element()
        elist.insert(1, new_element)
        assert elist[1] == new_element
        assert len(elist) == 3

    def test_elist_append(self, env, mock_element):
        elist = EList(env, [mock_element() for _ in range(2)])
        new_element = mock_element()
        elist.append(new_element)
        assert elist[-1] == new_element
        assert len(elist) == 3

    def test_elist_extend(self, env, mock_element):
        elist = EList(env, [mock_element() for _ in range(2)])
        new_elements = [mock_element() for _ in range(2)]
        elist.extend(new_elements)
        assert len(elist) == 4
        assert elist[-2:] == new_elements

    def test_elist_contains(self, env, mock_element):
        elements = [mock_element() for _ in range(3)]
        elist = EList(env, elements)
        assert elements[1] in elist
        assert elements[1].element_id in elist

    def test_elist_index(self, env, mock_element):
        elements = [mock_element() for _ in range(3)]
        elist = EList(env, elements)
        assert elist.index(elements[1]) == 1
        assert elist.index(elements[1].element_id) == 1

    def test_elist_count(self, env, mock_element):
        elements = [mock_element() for _ in range(3)]
        elist = EList(env, elements + [elements[0]])
        assert elist.count(elements[0]) == 2
        assert elist.count(elements[0].element_id) == 2

    def test_elist_repr(self, env, mock_element):
        elements = [mock_element() for _ in range(3)]
        elist = EList(env, elements)
        assert repr(elist).startswith("EList([")


@pytest.mark.unittest
class TestEFrozenList:
    def test_efrozenlist_init(self, env, mock_element):
        elements = [mock_element() for _ in range(3)]
        efrozenlist = EFrozenList(env, elements)
        assert len(efrozenlist) == 3
        assert all(isinstance(e, IElementID) for e in efrozenlist)

    def test_efrozenlist_getitem(self, env, mock_element):
        elements = [mock_element() for _ in range(3)]
        efrozenlist = EFrozenList(env, elements)
        assert efrozenlist[0] == elements[0]
        assert isinstance(efrozenlist[1:], EFrozenList)

    def test_efrozenlist_immutable(self, env, mock_element):
        elements = [mock_element() for _ in range(3)]
        efrozenlist = EFrozenList(env, elements)
        with pytest.raises(TypeError):
            efrozenlist[0] = mock_element()
        with pytest.raises(AttributeError):
            efrozenlist.append(mock_element())
