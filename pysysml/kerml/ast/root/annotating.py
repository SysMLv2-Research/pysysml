from typing import Optional, List, Union

from .base import Element, Relationship
from ..base import Env, EConn


class AnnotatingElement(Element):
    def __init__(
            self,
            env: Env,

            alias_ids: Optional[List[str]] = None,
            declared_name: Optional[str] = None,
            declared_short_name: Optional[str] = None,
            is_implied_included: bool = False,

            annotations: Optional[List[Union[str, 'Annotation']]] = None,
            owning_relationship: Optional[Union[str, 'Relationship']] = None,
            owned_relationships: Optional[List[Union[str, 'Relationship']]] = None,
            no_conj_when_init: bool = False,

            element_id: Optional[str] = None,
    ):
        Element.__init__(
            self,
            env=env,
            alias_ids=alias_ids,
            declared_name=declared_name,
            declared_short_name=declared_short_name,
            is_implied_included=is_implied_included,
            owning_relationship=owning_relationship,
            owned_relationships=owned_relationships,
            no_conj_when_init=no_conj_when_init,
            element_id=element_id,
        )

        self._annotations = EConn(
            env=self.env, type_=Annotation,
            fn_add_conj=self._fn_add_to_annotations,
            fn_remove_conj=self._fn_remove_from_annotations,
        )
        self._annotations.update(annotations or [])

    def _fn_add_to_annotations(self, annotation: 'Annotation'):
        pass

    def _fn_remove_from_annotations(self, annotation: 'Annotation'):
        pass

    @property
    def annotations(self) -> EConn['Annotation']:
        return self._annotations

    @property
    def annotated_elements(self) -> List[Element]:
        if self.annotations:
            return [
                annotation.annotated_element
                for annotation in self.annotations
                if annotation.annotated_element
            ]

        else:
            if self.owning_namespace:
                return [self.owning_namespace]
            else:
                return []

    @property
    def owned_annotating_relationship(self) -> List['Annotation']:
        return [
            r for r in self.owned_relationships
            if isinstance(r, Annotation) and r.annotated_element == self
        ]


class Annotation(Relationship):
    def __init__(
            self,
            env: Env,

            is_implied: bool = False,
            alias_ids: Optional[List[str]] = None,
            declared_name: Optional[str] = None,
            declared_short_name: Optional[str] = None,
            is_implied_included: bool = False,

            annotating_elements: Optional[List[Union[str, Element]]] = None,
            annotated_elements: Optional[List[Union[str, Element]]] = None,
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

            sources=annotating_elements,  # only 1
            targets=annotated_elements,  # only 1
            owning_related_element=owning_related_element,
            owned_related_elements=owned_related_elements,
            owning_relationship=owning_relationship,
            owned_relationships=owned_relationships,
            no_conj_when_init=no_conj_when_init,

            element_id=element_id,
        )

    @property
    def annotating_element(self) -> Optional[Element]:
        return self.sources.first()

    @annotating_element.setter
    def annotating_element(self, value):
        if value is not None:
            self.sources.set_to(value)
        else:
            self.sources.clear()

    @property
    def annotated_element(self) -> Optional[Element]:
        return self.targets.first()

    @annotated_element.setter
    def annotated_element(self, value):
        if value is not None:
            self.targets.set_to(value)
        else:
            self.targets.clear()

    @property
    def owning_annotated_element(self) -> Optional[Element]:
        annotated_element = self.annotated_element
        if annotated_element and annotated_element in self.owning_related_element:
            return annotated_element
        else:
            return None

    @property
    def owning_annotating_element(self) -> Optional[Element]:
        annotating_element = self.annotating_element
        if annotating_element and annotating_element in self.owning_related_element:
            return annotating_element
        else:
            return None


class Comment(AnnotatingElement):
    pass


class Documentation(Comment):
    pass


class TextualRepresentation(AnnotatingElement):
    pass
