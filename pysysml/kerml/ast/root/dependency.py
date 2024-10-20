from typing import Optional, List, Union

from .base import Relationship, ConstraintsError, Element
from ..base import Env, EConn


class Dependency(Relationship):
    def __init__(
            self,
            env: Env,

            is_implied: bool = False,
            alias_ids: Optional[List[str]] = None,
            declared_name: Optional[str] = None,
            declared_short_name: Optional[str] = None,
            is_implied_included: bool = False,

            clients: Optional[List[Union[str, Element]]] = None,
            suppliers: Optional[List[Union[str, Element]]] = None,
            owning_related_element: Optional[Union[str, Element]] = None,
            owned_related_elements: Optional[List[Union[str, Element]]] = None,
            owning_relationship: Optional[Union[str, 'Relationship']] = None,
            owned_relationships: Optional[List[Union[str, 'Relationship']]] = None,
            no_conj_when_init: bool = False,

            element_id: Optional[str] = None
    ):
        Relationship.__init__(
            self,
            env=env,
            is_implied=is_implied,

            alias_ids=alias_ids,
            declared_name=declared_name,
            declared_short_name=declared_short_name,
            is_implied_included=is_implied_included,

            sources=clients,
            targets=suppliers,
            owning_related_element=owning_related_element,
            owned_related_elements=owned_related_elements,
            owning_relationship=owning_relationship,
            owned_relationships=owned_relationships,
            no_conj_when_init=no_conj_when_init,

            element_id=element_id,
        )

    @property
    def clients(self) -> EConn[Element]:
        return self.sources

    @property
    def suppliers(self) -> EConn[Element]:
        return self.targets

    def _check_num_of_clients(self):
        if len(self.clients) < 1:
            raise ConstraintsError('Dependency should have no less than 1 client.')

    def _check_num_of_suppliers(self):
        if len(self.suppliers) < 1:
            raise ConstraintsError('Dependency should have no less than 1 supplier.')

    def check_constraints(self):
        super().check_constraints()
        self._check_num_of_clients()
        self._check_num_of_suppliers()
