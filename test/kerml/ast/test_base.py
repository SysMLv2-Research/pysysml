import uuid

import pytest

from pysysml.kerml.ast import Env, IElementID, ElementNotFoundError, ConstraintsError
from pysysml.kerml.ast.base import EConn


@pytest.fixture
def mock_uuid(monkeypatch):
    mock_id = "mock-uuid"
    monkeypatch.setattr(uuid, "uuid4", lambda: mock_id)
    return mock_id


@pytest.fixture
def env():
    return Env()


class MockElement(IElementID):
    pass


class AnotherTypeElement(IElementID):
    pass


@pytest.fixture
def mock_element(env):
    return MockElement(env)


@pytest.mark.unittest
class TestEnvAndElementID:
    def test_env_init(self, env):
        assert len(env) == 0
        assert repr(env) == f"<Env {hex(id(env))}, 0 items>"

    def test_env_add_and_get(self, env, mock_element):
        env.add(mock_element)
        assert len(env) == 1
        assert env[mock_element.element_id] == mock_element
        assert mock_element in env

    def test_env_set_and_del(self, env, mock_element):
        env["test_key"] = mock_element
        assert "test_key" in env
        assert env["test_key"] == mock_element
        del env["test_key"]
        assert "test_key" not in env

    def test_env_set_and_del_obj(self, env, mock_element):
        env.add(mock_element)
        assert env[mock_element.element_id] == mock_element
        assert env[mock_element] == mock_element
        del env[mock_element]
        assert mock_element.element_id not in env
        assert mock_element not in env

    def test_env_errors(self, env, mock_element):
        with pytest.raises(ElementNotFoundError) as exc_info:
            env["non_existent"]
        assert exc_info.value.env == env
        assert exc_info.value.key == "non_existent"

        with pytest.raises(TypeError):
            env["invalid"] = "not an IElementID"

    def test_element_id_init(self, env, mock_uuid):
        element = IElementID(env)
        assert element.element_id == mock_uuid
        assert element.env == env

    def test_element_id_custom_id(self, env):
        custom_id = "custom-id"
        element = IElementID(env, element_id=custom_id)
        assert element.element_id == custom_id
        assert element.env == env


@pytest.mark.unittest
class TestExceptions:
    def test_element_not_found_error(self, env):
        with pytest.raises(ElementNotFoundError) as exc_info:
            _ = env["non_existent"]

        assert exc_info.value.args[0] == f"Element 'non_existent' not found in env {env!r}."
        assert exc_info.value.env == env
        assert exc_info.value.key == "non_existent"

    def test_constraints_error(self):
        with pytest.raises(ConstraintsError):
            raise ConstraintsError("Test constraints error")


@pytest.mark.unittest
class TestEConn:
    def test_econn(self, env):
        conn = EConn(env)
        assert conn.env is env
        assert len(conn) == 0
        assert list(conn) == []
        assert conn.first() is None

        assert conn == []
        assert not conn
        assert repr(conn) == 'EConn()'

    def test_elements(self, env, mock_element):
        e1 = MockElement(env)
        e2 = MockElement(env)
        conn = EConn(env, initial=[e1, e2])
        assert len(conn) == 2
        assert e1 in conn
        assert e1.element_id in conn
        assert e2 in conn
        assert e2.element_id in conn
        assert conn.first() == e1

        assert conn == [e1, e2]
        assert conn

        e3 = MockElement(env)
        assert e3 not in conn
        assert e3.element_id not in conn
        assert list(conn) == [e1, e2]

        with pytest.raises(ElementNotFoundError):
            conn.add('xxxx')

        conn.remove(e1)
        assert len(conn) == 1
        assert list(conn) == [e2]
        assert e1 not in conn
        assert e1.element_id not in conn
        assert e2 in conn
        assert e2.element_id in conn
        assert conn.first() == e2
        assert conn == [e2]
        assert conn
        assert repr(conn) == f'EConn({e2!r})'

        conn.remove(e1)
        assert len(conn) == 1
        assert list(conn) == [e2]
        assert e1 not in conn
        assert e1.element_id not in conn
        assert e2 in conn
        assert e2.element_id in conn
        assert conn.first() == e2
        assert conn == [e2]
        assert conn
        assert repr(conn) == f'EConn({e2!r})'

        conn.remove(e2)
        assert len(conn) == 0
        assert list(conn) == []
        assert e1 not in conn
        assert e1.element_id not in conn
        assert e2 not in conn
        assert e2.element_id not in conn
        assert conn.first() is None
        assert conn == []
        assert not conn

    def test_type_check(self, env):
        e1 = MockElement(env)
        e2 = MockElement(env)
        conn = EConn(env, type_=MockElement, initial=[e1, e2])
        assert len(conn) == 2
        assert list(conn) == [e1, e2]
        assert e1 in conn
        assert e1.element_id in conn
        assert e2 in conn
        assert e2.element_id in conn

        e3 = MockElement(env)
        conn.add(e3)
        assert len(conn) == 3
        assert list(conn) == [e1, e2, e3]
        assert e1 in conn
        assert e1.element_id in conn
        assert e2 in conn
        assert e2.element_id in conn
        assert e3 in conn
        assert e3.element_id in conn

        e4 = AnotherTypeElement(env)
        with pytest.raises(TypeError):
            conn.add(e4)

    def test_update(self, env):
        conn = EConn(env)
        assert len(conn) == 0
        assert list(conn) == []

        e1 = MockElement(env)
        e2 = MockElement(env)
        assert conn.update([e1, e2]) is conn
        assert len(conn) == 2
        assert list(conn) == [e1, e2]
        assert e1 in conn
        assert e1.element_id in conn
        assert e2 in conn
        assert e2.element_id in conn

    def test_clear(self, env):
        e1 = MockElement(env)
        e2 = MockElement(env)
        conn = EConn(env, type_=MockElement, initial=[e1, e2])
        assert len(conn) == 2
        assert list(conn) == [e1, e2]
        assert e1 in conn
        assert e1.element_id in conn
        assert e2 in conn
        assert e2.element_id in conn

        assert conn.clear() is conn
        assert len(conn) == 0
        assert list(conn) == []
        assert e1 not in conn
        assert e1.element_id not in conn
        assert e2 not in conn
        assert e2.element_id not in conn

    def test_add_conj(self, env):
        add_count = 0
        addings = []

        def _fn_add(e):
            nonlocal add_count
            add_count += 1
            addings.append(e)

        e1 = MockElement(env)
        e2 = MockElement(env)
        conn = EConn(env, type_=MockElement, initial=[e1, e2], fn_add_conj=_fn_add)
        assert len(conn) == 2
        assert list(conn) == [e1, e2]
        assert e1 in conn
        assert e1.element_id in conn
        assert e2 in conn
        assert e2.element_id in conn
        assert add_count == 2
        assert addings == [e1, e2]

        e3 = MockElement(env)
        conn.add(e3)
        assert len(conn) == 3
        assert list(conn) == [e1, e2, e3]
        assert e1 in conn
        assert e1.element_id in conn
        assert e2 in conn
        assert e2.element_id in conn
        assert e3 in conn
        assert e3.element_id in conn
        assert add_count == 3
        assert addings == [e1, e2, e3]

        e4 = AnotherTypeElement(env)
        with pytest.raises(TypeError):
            conn.add(e4)
        assert len(conn) == 3
        assert list(conn) == [e1, e2, e3]
        assert e1 in conn
        assert e1.element_id in conn
        assert e2 in conn
        assert e2.element_id in conn
        assert e3 in conn
        assert e3.element_id in conn
        assert add_count == 3
        assert addings == [e1, e2, e3]

    def test_remove_conj(self, env):
        remove_count = 0
        removings = []

        def _fn_remove(e):
            nonlocal remove_count
            remove_count += 1
            removings.append(e)

        e1 = MockElement(env)
        e2 = MockElement(env)
        e3 = MockElement(env)
        conn = EConn(env, type_=MockElement, initial=[e1, e2, e3], fn_remove_conj=_fn_remove)
        assert len(conn) == 3
        assert list(conn) == [e1, e2, e3]
        assert e1 in conn
        assert e1.element_id in conn
        assert e2 in conn
        assert e2.element_id in conn
        assert e3 in conn
        assert e3.element_id in conn
        assert remove_count == 0
        assert removings == []

        conn.remove(e2)
        assert len(conn) == 2
        assert list(conn) == [e1, e3]
        assert e1 in conn
        assert e1.element_id in conn
        assert e2 not in conn
        assert e2.element_id not in conn
        assert e3 in conn
        assert e3.element_id in conn
        assert remove_count == 1
        assert removings == [e2]

        conn.clear()
        assert len(conn) == 0
        assert list(conn) == []
        assert e1 not in conn
        assert e1.element_id not in conn
        assert e2 not in conn
        assert e2.element_id not in conn
        assert e3 not in conn
        assert e3.element_id not in conn
        assert remove_count == 3
        assert removings == [e2, e1, e3]

    def test_set_to(self, env):
        add_count = 0
        addings = []

        def _fn_add(e):
            nonlocal add_count
            add_count += 1
            addings.append(e)

        remove_count = 0
        removings = []

        def _fn_remove(e):
            nonlocal remove_count
            remove_count += 1
            removings.append(e)

        e1 = MockElement(env)
        e2 = MockElement(env)
        conn = EConn(env, type_=MockElement, initial=[e1, e2], fn_add_conj=_fn_add, fn_remove_conj=_fn_remove)
        assert len(conn) == 2
        assert list(conn) == [e1, e2]
        assert e1 in conn
        assert e1.element_id in conn
        assert e2 in conn
        assert e2.element_id in conn
        assert add_count == 2
        assert addings == [e1, e2]
        assert remove_count == 0
        assert removings == []

        e3 = MockElement(env)
        conn.set_to(e3)
        assert len(conn) == 1
        assert list(conn) == [e3]
        assert e1 not in conn
        assert e1.element_id not in conn
        assert e2 not in conn
        assert e2.element_id not in conn
        assert e3 in conn
        assert e3.element_id in conn
        assert add_count == 3
        assert addings == [e1, e2, e3]
        assert remove_count == 2
        assert removings == [e1, e2]

        e4 = MockElement(env)
        conn.set_to(e4)
        assert len(conn) == 1
        assert list(conn) == [e4]
        assert e1 not in conn
        assert e1.element_id not in conn
        assert e2 not in conn
        assert e2.element_id not in conn
        assert e3 not in conn
        assert e3.element_id not in conn
        assert e4 in conn
        assert e4.element_id in conn
        assert add_count == 4
        assert addings == [e1, e2, e3, e4]
        assert remove_count == 3
        assert removings == [e1, e2, e3]

        conn.clear()
        assert len(conn) == 0
        assert list(conn) == []
        assert e1 not in conn
        assert e1.element_id not in conn
        assert e2 not in conn
        assert e2.element_id not in conn
        assert e3 not in conn
        assert e3.element_id not in conn
        assert e4 not in conn
        assert e4.element_id not in conn
        assert add_count == 4
        assert addings == [e1, e2, e3, e4]
        assert remove_count == 4
        assert removings == [e1, e2, e3, e4]

        e5 = MockElement(env)
        conn.set_to(e5)
        assert len(conn) == 1
        assert list(conn) == [e5]
        assert e1 not in conn
        assert e1.element_id not in conn
        assert e2 not in conn
        assert e2.element_id not in conn
        assert e3 not in conn
        assert e3.element_id not in conn
        assert e4 not in conn
        assert e4.element_id not in conn
        assert e5 in conn
        assert e5.element_id in conn
        assert add_count == 5
        assert addings == [e1, e2, e3, e4, e5]
        assert remove_count == 4
        assert removings == [e1, e2, e3, e4]

        conn.set_to(e5)
        assert len(conn) == 1
        assert list(conn) == [e5]
        assert e1 not in conn
        assert e1.element_id not in conn
        assert e2 not in conn
        assert e2.element_id not in conn
        assert e3 not in conn
        assert e3.element_id not in conn
        assert e4 not in conn
        assert e4.element_id not in conn
        assert e5 in conn
        assert e5.element_id in conn
        assert add_count == 5
        assert addings == [e1, e2, e3, e4, e5]
        assert remove_count == 4
        assert removings == [e1, e2, e3, e4]
