import re
from typing import List, Optional, Union

from ..base import Env, IElementID, ConstraintsError, EConn


def _is_basic_name(name: str) -> bool:
    return bool(re.fullmatch(r'^[a-zA-Z_][a-zA-Z\d_]*$', name))


# noinspection PyUnresolvedReferences
class Element(IElementID):
    def __init__(
            self,
            env: Env,

            alias_ids: Optional[List[str]] = None,
            declared_name: Optional[str] = None,
            declared_short_name: Optional[str] = None,
            is_implied_included: bool = False,

            owning_relationship: Optional[Union[str, 'Relationship']] = None,
            owned_relationships: Optional[List[Union[str, 'Relationship']]] = None,
            no_conj_when_init: bool = False,

            element_id: Optional[str] = None,
    ):
        super().__init__(env, element_id)

        # Various alternative identifiers for this Element. Generally, these will be set by tools.
        self.alias_ids: List[str] = list(alias_ids or [])

        # The declared name of this Element.
        self.declared_name: Optional[str] = declared_name

        # An optional alternative name for the Element that is intended to be shorter or more succinct.
        self.declared_short_name: Optional[str] = declared_short_name

        # Whether all necessary implied Relationships have been included in the ownedRelationships of this Element.
        self.is_implied_included: bool = is_implied_included

        self._owning_relationships: EConn['Relationship'] = EConn(
            env=self.env, type_=Relationship,
            fn_add_conj=self._fn_add_to_owning_relationship,
            fn_remove_conj=self._fn_remove_from_owning_relationship,
        )
        self._owned_relationships: EConn['Relationship'] = EConn(
            env=self.env, type_=Relationship,
            fn_add_conj=self._fn_add_to_owned_relationship,
            fn_remove_conj=self._fn_remove_from_owned_relationship,
        )
        if owning_relationship:
            self._owning_relationships.set_to(owning_relationship, no_conj=no_conj_when_init)
        self._owned_relationships.update(owned_relationships or [], no_conj=no_conj_when_init)

    @property
    def documentations(self) -> List["Documentation"]:
        from .annotating import Documentation
        return [item for item in self.owned_elements if isinstance(item, Documentation)]

    @property
    def is_library_element(self) -> bool:
        return bool(self.library_namespace())

    @property
    def name(self) -> Optional[str]:
        return self._get_name()

    def _get_name(self):
        return self.effective_name()

    @property
    def owned_annotations(self) -> List["Annotation"]:
        from .annotating import Annotation
        return [item for item in self.owned_relationships if isinstance(item, Annotation)]

    @property
    def owned_elements(self) -> List["Element"]:
        retval = []
        for relationship in self.owned_relationships:
            retval.extend(relationship.owned_related_elements)
        return retval

    @property
    def owner(self) -> Optional["Element"]:
        if self.owning_relationship:
            return self.owning_relationship.owning_related_element
        else:
            return None

    @property
    def owning_membership(self) -> Optional["OwningMembership"]:
        from .namespace import OwningMembership
        owning_relationship = self.owning_relationship
        if owning_relationship and isinstance(owning_relationship, OwningMembership):
            return owning_relationship
        else:
            return None

    @property
    def owning_namespace(self) -> Optional["Namespace"]:
        from .namespace import Namespace
        owning_membership: Optional[Namespace] = self.owning_membership
        if owning_membership:
            return owning_membership.membership_owning_namespace
        else:
            return None

    def _fn_add_to_owned_relationship(self, relationship: 'Relationship'):
        relationship.owning_related_element = self

    def _fn_remove_from_owned_relationship(self, relationship: 'Relationship'):
        relationship.owning_related_element = None

    @property
    def owned_relationships(self) -> EConn['Relationship']:
        return self._owned_relationships

    def _fn_add_to_owning_relationship(self, relationship: 'Relationship'):
        relationship.owned_related_elements.add(self)

    def _fn_remove_from_owning_relationship(self, relationship: 'Relationship'):
        relationship.owned_related_elements.remove(self)

    @property
    def owning_relationship(self) -> Optional["Relationship"]:
        return self._owning_relationships.first()

    @owning_relationship.setter
    def owning_relationship(self, value: Optional[Union[str, 'Relationship']]):
        if value is not None:
            self._owning_relationships.set_to(value)
        else:
            self._owning_relationships.clear()

    @property
    def qualified_name(self) -> Optional[str]:
        from .namespace import Namespace
        return self._compute_qualified_name()

    @property
    def short_name(self) -> Optional[str]:
        return self._get_short_name()

    def _get_short_name(self):
        return self.effective_short_name()

    @property
    def textual_representations(self) -> List["TextualRepresentation"]:
        from .annotating import TextualRepresentation
        return [item for item in self.owned_elements if isinstance(item, TextualRepresentation)]

    def effective_name(self) -> Optional[str]:
        return self.declared_name

    def effective_short_name(self) -> Optional[str]:
        return self.declared_short_name

    def escaped_name(self) -> Optional[str]:
        name = self.name or self.short_name
        if name is None:
            return None
        if _is_basic_name(name):
            return name
        else:
            return repr(name)

    def library_namespace(self) -> Optional["Namespace"]:
        if self.owning_relationship:
            return self.owning_relationship.library_namespace()
        return None

    def check_constraints(self):
        self._check_num_owning_relationships()
        self._check_derive_element_documentation()
        self._check_derive_element_is_library_element()
        self._check_derive_element_name()
        self._check_derive_element_owned_annotation()
        self._check_derive_element_owned_element()
        self._check_derive_element_owner()
        self._check_derive_element_qualified_name()
        self._check_derive_element_short_name()
        self._check_derive_element_textual_representation()
        self._check_derive_owning_namespace()
        self._check_validate_element_is_implied_included()

    def _check_num_owning_relationships(self):
        if len(self._owning_relationships) > 1:
            raise ConstraintsError(
                f'Owning relationships should not exceed 1 not {self._owning_relationships!r} found.')

    def _check_derive_element_documentation(self):
        """
        Constraint: The documentation of an Element is its ownedElements that are Documentation.
        """
        from .annotating import Documentation

        expected_documentation = [elem for elem in self.owned_elements if isinstance(elem, Documentation)]
        if self.documentations != expected_documentation:
            raise ConstraintsError("Documentation constraint violated")

    def _check_derive_element_is_library_element(self):
        """
        Constraint: An Element isLibraryElement if libraryNamespace() is not null.
        """
        expected_is_library_element = self.library_namespace() is not None
        if self.is_library_element != expected_is_library_element:
            raise ConstraintsError("IsLibraryElement constraint violated")

    def _check_derive_element_name(self):
        """
        Constraint: The name of an Element is given by the result of the effectiveName() operation.
        """
        if self.name != self.effective_name():
            raise ConstraintsError("Name constraint violated")

    def _check_derive_element_owned_annotation(self):
        """
        Constraint: The ownedAnnotations of an Element are its ownedRelationships that are Annotations,
        for which the Element is the annotatedElement.
        """
        from .annotating import Annotation

        expected_owned_annotation = [
            rel for rel in self.owned_relationships
            if isinstance(rel, Annotation) and rel.annotated_element == self
        ]
        if self.owned_annotations != expected_owned_annotation:
            raise ConstraintsError("OwnedAnnotation constraint violated")

    def _check_derive_element_owned_element(self):
        """
        Constraint: The ownedElements of an Element are the ownedRelatedElements of its ownedRelationships.
        """
        expected_owned_element = [
            elem for rel in self.owned_relationships
            for elem in rel.owned_related_elements
        ]
        if self.owned_elements != expected_owned_element:
            raise ConstraintsError("OwnedElement constraint violated")

    def _check_derive_element_owner(self):
        """
        Constraint: The owner of an Element is the owningRelatedElement of its owningRelationship.
        """
        expected_owner = self.owning_relationship.owning_related_element if self.owning_relationship else None
        if self.owner != expected_owner:
            raise ConstraintsError("Owner constraint violated")

    def _check_derive_element_qualified_name(self):
        """
        Constraint: The qualifiedName is derived based on the owningNamespace and the escaped name of the Element.
        """
        expected_qualified_name = self._compute_qualified_name()
        if self.qualified_name != expected_qualified_name:
            raise ConstraintsError("QualifiedName constraint violated")

    def _compute_qualified_name(self) -> Optional[str]:
        if not self.owning_namespace:
            return None
        if self.owning_namespace.owner is None:
            return self.escaped_name()
        if self.owning_namespace.qualified_name is None or self.escaped_name() is None:
            return None
        return f"{self.owning_namespace.qualified_name}::{self.escaped_name()}"

    def _check_derive_element_short_name(self):
        """
        Constraint: The shortName of an Element is given by the result of the effectiveShortName() operation.
        """
        if self.short_name != self.effective_short_name():
            raise ConstraintsError("ShortName constraint violated")

    def _check_derive_element_textual_representation(self):
        """
        Constraint: The textualRepresentations of an Element are its ownedElements that are TextualRepresentations.
        """
        from .annotating import TextualRepresentation
        expected_textual_representation = [elem for elem in self.owned_elements if
                                           isinstance(elem, TextualRepresentation)]
        if self.textual_representations != expected_textual_representation:
            raise ConstraintsError("TextualRepresentation constraint violated")

    def _check_derive_owning_namespace(self):
        """
        Constraint: The owningNamespace of an Element is the membershipOwningNamspace of its owningMembership (if any).
        """
        expected_owning_namespace = self.owning_membership.membership_owning_namespace if self.owning_membership else None
        if self.owning_namespace != expected_owning_namespace:
            raise ConstraintsError("OwningNamespace constraint violated")

    def _check_validate_element_is_implied_included(self):
        """
        Constraint: If an Element has any ownedRelationships for which isImplied = true,
        then the Element must also have isImpliedIncluded = true.
        """
        if any(rel.is_implied for rel in self.owned_relationships) and not self.is_implied_included:
            raise ConstraintsError("IsImpliedIncluded constraint violated")


class Relationship(Element):
    def __init__(
            self,
            env: Env,

            is_implied: bool = False,
            alias_ids: Optional[List[str]] = None,
            declared_name: Optional[str] = None,
            declared_short_name: Optional[str] = None,
            is_implied_included: bool = False,

            sources: Optional[List[Union[str, Element]]] = None,
            targets: Optional[List[Union[str, Element]]] = None,
            owning_related_element: Optional[Union[str, Element]] = None,
            owned_related_elements: Optional[List[Union[str, Element]]] = None,
            owning_relationship: Optional[Union[str, 'Relationship']] = None,
            owned_relationships: Optional[List[Union[str, 'Relationship']]] = None,
            no_conj_when_init: bool = False,

            element_id: Optional[str] = None
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
        self._is_implied = is_implied

        self._sources: EConn[Element] = EConn(
            env=self.env, type_=Element,
            no_conj_when_init=no_conj_when_init,
            initial=list(sources or []),
        )
        self._targets: EConn[Element] = EConn(
            env=self.env, type_=Element,
            no_conj_when_init=no_conj_when_init,
            initial=list(targets or []),
        )

        self._owned_related_elements: EConn[Element] = EConn(
            env=self.env, type_=Element,
            fn_add_conj=self._fn_add_to_owned_related_element,
            fn_remove_conj=self._fn_remove_from_owned_related_element,
        )
        self._owning_related_elements: EConn[Element] = EConn(
            env=self.env, type_=Element,
            fn_add_conj=self._fn_add_to_owning_related_element,
            fn_remove_conj=self._fn_remove_from_owning_related_element,
        )
        self._owned_related_elements.update(owned_related_elements or [], no_conj=no_conj_when_init)
        if owning_related_element:
            self._owning_related_elements.set_to(owning_related_element, no_conj=no_conj_when_init)

    @property
    def is_implied(self) -> bool:
        return self._is_implied

    @property
    def sources(self) -> EConn[Element]:
        return self._sources

    @property
    def targets(self) -> EConn[Element]:
        return self._targets

    @property
    def related_elements(self) -> List[Element]:
        return [*self._sources, *self.targets]

    def _fn_add_to_owned_related_element(self, element: Element):
        element.owning_relationship = self

    def _fn_remove_from_owned_related_element(self, element: Element):
        element.owning_relationship = None

    @property
    def owned_related_elements(self) -> EConn[Element]:
        return self._owned_related_elements

    def _fn_add_to_owning_related_element(self, element: Element):
        element.owned_relationships.add(self)

    def _fn_remove_from_owning_related_element(self, element: Element):
        element.owned_relationships.remove(self)

    @property
    def owning_related_element(self) -> Optional[Element]:
        return self._owning_related_elements.first()

    @owning_related_element.setter
    def owning_related_element(self, value: Optional[Union[str, Element]]):
        if value is not None:
            self._owning_related_elements.set_to(value)
        else:
            self._owning_related_elements.clear()

    def library_namespace(self) -> Optional['Namespace']:
        # Implement the libraryNamespace operation
        owning_related_element = self.owning_related_element
        if owning_related_element is not None:
            return owning_related_element.library_namespace()
        owning_relationship = self.owning_relationship
        if owning_relationship is not None:
            return owning_relationship.library_namespace()
        return None

    def check_constraints(self):
        """
        Check all constraints for the Relationship.
        Raises ConstraintsError if any constraint is not satisfied.
        """
        Element.check_constraints(self)
        self._check_num_owning_related_element()
        self._check_derive_relationship_related_element()
        self._check_consistence_of_owned_related_element()
        self._check_consistence_of_owning_related_element()

    def _check_num_owning_related_element(self):
        if len(self._owning_related_elements) > 1:
            raise ConstraintsError(
                f'Owning relationships should not exceed 1 not {self._owning_related_elements!r} found.')

    def _check_derive_relationship_related_element(self):
        """
        Constraint: deriveRelationshipRelatedElement
        The relatedElements of a Relationship consist of all of its source Elements followed by all of its target Elements.
        relatedElement = source->union(target)
        """
        expected_related_elements = [*self.sources, *self.targets]
        if self.related_elements != expected_related_elements:
            raise ConstraintsError(
                "The relatedElement property must be the union of source and target elements, in that order.")

    def _check_consistence_of_owned_related_element(self):
        for item in self.owned_related_elements:
            if item not in self.related_elements:
                raise ConstraintsError(
                    f"The item {item!r} in owned_related_elements not in the related_elements.")

    def _check_consistence_of_owning_related_element(self):
        item = self.owning_related_element
        if item is not None and item not in self.related_elements:
            raise ConstraintsError(
                f"The item {item!r} of owning_related_elements not in the related_elements.")
