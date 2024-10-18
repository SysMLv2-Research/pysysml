from typing import Optional, List, Union

from .base import Relationship, Element, ConstraintsError
from ..base import Env


class Dependency(Relationship):
    def __init__(
            self,
            env: Env,

            client: Optional[List[Union[str, 'Relationship']]] = None,
            supplier: Optional[List[Union[str, 'Relationship']]] = None,
            is_implied: bool = False,
            owning_related_elements: Optional[List[Union[str, Element]]] = None,
            owned_related_element: Optional[Union[str, Element]] = None,

            alias_ids: Optional[List[str]] = None,
            declared_name: Optional[str] = None,
            declared_short_name: Optional[str] = None,
            owning_relationship: Optional[Union[str, 'Relationship']] = None,
            owned_relationships: Optional[List[Union[str, 'Relationship']]] = None,
            is_implied_included: bool = False,

            element_id: Optional[str] = None
    ):
        Relationship.__init__(
            self,
            env=env,
            is_implied=is_implied,
            source=client,
            target=supplier,
            owning_related_elements=owning_related_elements,
            owned_related_element=owned_related_element,

            alias_ids=alias_ids,
            declared_name=declared_name,
            declared_short_name=declared_short_name,
            owning_relationship=owning_relationship,
            owned_relationships=owned_relationships,
            is_implied_included=is_implied_included,

            element_id=element_id,
        )

    @property
    def clients(self):
        return self.sources

    @property
    def suppliers(self):
        return self.targets

    def _check_number_of_clients(self):
        if len(self.clients) < 1:
            raise ConstraintsError('Dependency should have no less than 1 client.')

    def _check_number_of_suppliers(self):
        if len(self.suppliers) < 1:
            raise ConstraintsError('Dependency should have no less than 1 supplier.')

    def check_constraints(self):
        super().check_constraints()
        self._check_number_of_clients()
        self._check_number_of_suppliers()
