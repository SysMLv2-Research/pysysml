from typing import Optional, List

from .base import Relationship, ConstraintsError
from ..base import Env


class Dependency(Relationship):
    def __init__(
            self,
            env: Env,

            is_implied: bool = False,
            alias_ids: Optional[List[str]] = None,
            declared_name: Optional[str] = None,
            declared_short_name: Optional[str] = None,
            is_implied_included: bool = False,

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
