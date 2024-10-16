import uuid
from typing import List, Optional

from ..base import Env, IElementID, ConstraintsError


class Element(IElementID):
    def __init__(self,
                 env: Env,
                 alias_ids: List[str],
                 declared_name: Optional[str],
                 declared_short_name: Optional[str],
                 is_implied_included: bool,
                 element_id: Optional[str] = None):
        super().__init__(env, element_id)

        # Various alternative identifiers for this Element. Generally, these will be set by tools.
        self.alias_ids: List[str] = alias_ids

        # The declared name of this Element.
        self.declared_name: Optional[str] = declared_name

        # An optional alternative name for the Element that is intended to be shorter or more succinct.
        self.declared_short_name: Optional[str] = declared_short_name

        # Whether all necessary implied Relationships have been included in the ownedRelationships of this Element.
        self.is_implied_included: bool = is_implied_included

        # The Relationship for which this Element is an ownedRelatedElement, if any.
        self._owning_relationship_id: Optional[str] = None

    @property
    def documentation(self) -> List["Documentation"]:
        return self._get_documentation()

    def _get_documentation(self) -> List["Documentation"]:
        # TODO: Implement method to return Documentation owned by this Element.
        # This should return a list of Documentation objects that are owned elements and annotating elements of this Element.
        # The list should be ordered.
        raise NotImplementedError()

    @property
    def is_library_element(self) -> bool:
        return self._get_is_library_element()

    def _get_is_library_element(self) -> bool:
        # TODO: Implement method to determine if this Element is contained in the ownership tree of a library model.
        raise NotImplementedError()

    @property
    def name(self) -> Optional[str]:
        return self.effective_name()

    @property
    def owned_annotation(self) -> List["Annotation"]:
        return self._get_owned_annotation()

    def _get_owned_annotation(self) -> List["Annotation"]:
        # TODO: Implement method to return ownedRelationships of this Element that are Annotations,
        # for which this Element is the annotatedElement. This should be a subset of ownedRelationship and annotation,
        # and should be ordered.
        raise NotImplementedError()

    @property
    def owned_element(self) -> List["Element"]:
        return [self._env[element_id] for element_id in self._owned_element_ids]

    @property
    def owner(self) -> Optional["Element"]:
        return self._get_owner()

    def _get_owner(self) -> Optional["Element"]:
        # TODO: Implement method to return the owner of this Element, derived as the owningRelatedElement
        # of the owningRelationship of this Element, if any.
        raise NotImplementedError()

    @property
    def owning_membership(self) -> Optional["OwningMembership"]:
        return self._get_owning_membership()

    def _get_owning_membership(self) -> Optional["OwningMembership"]:
        # TODO: Implement method to return the owningRelationship of this Element,
        # if that Relationship is a Membership. This should be a subset of owningRelationship and membership.
        raise NotImplementedError()

    @property
    def owning_namespace(self) -> Optional["Namespace"]:
        return self._get_owning_namespace()

    def _get_owning_namespace(self) -> Optional["Namespace"]:
        # TODO: Implement method to return the Namespace that owns this Element,
        # which is the membershipOwningNamespace of the owningMembership of this Element, if any.
        # This should be a subset of namespace.
        raise NotImplementedError()

    @property
    def owning_relationship(self) -> Optional["Relationship"]:
        owning_relationship_id = self._get_owning_relationship_id()
        return self._env[owning_relationship_id] if self._owning_relationship_id else None

    def _get_owning_relationship_id(self) -> Optional[str]:
        raise NotImplementedError

    @property
    def owned_relationship(self) -> List["Relationship"]:
        return [
            self._env[id_]
            for id_ in self._get_owned_relationship_ids()
        ]

    def _get_owned_relationship_ids(self) -> List[str]:
        raise NotImplementedError

    @property
    def qualified_name(self) -> Optional[str]:
        return self._get_qualified_name()

    def _get_qualified_name(self) -> Optional[str]:
        # TODO: Implement method to return the full ownership-qualified name of this Element.
        # This should be represented in a form that is valid according to the KerML textual concrete syntax for qualified names.
        # Return null if this Element has no owningNamespace or if there is not a complete ownership chain of named Namespaces.
        raise NotImplementedError()

    @property
    def short_name(self) -> Optional[str]:
        return self.effective_short_name()

    @property
    def textual_representation(self) -> List["TextualRepresentation"]:
        return self._get_textual_representation()

    def _get_textual_representation(self) -> List["TextualRepresentation"]:
        # TODO: Implement method to return TextualRepresentations that annotate this Element.
        # This should be a subset of ownedElement and annotatingElement, and should be ordered.
        raise NotImplementedError()

    def effective_name(self) -> Optional[str]:
        return self.declared_name

    def effective_short_name(self) -> Optional[str]:
        return self.declared_short_name

    def escaped_name(self) -> Optional[str]:
        name = self.name or self.short_name
        if name is None:
            return None
        if self._is_basic_name(name):
            return name
        return repr(name.replace('\'', '\\\''))

    def _is_basic_name(self, name: str) -> bool:
        # TODO: Implement method to check if the name has the form of a basic name
        raise NotImplementedError()

    def library_namespace(self) -> Optional["Namespace"]:
        if self.owning_relationship:
            return self.owning_relationship.library_namespace()
        return None

    def check_constraints(self):
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

    def _check_derive_element_documentation(self):
        """
        Constraint: The documentation of an Element is its ownedElements that are Documentation.
        """
        from .annotating import Documentation

        expected_documentation = [elem for elem in self.owned_element if isinstance(elem, Documentation)]
        if self.documentation != expected_documentation:
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
            rel for rel in self.owned_relationship
            if isinstance(rel, Annotation) and rel.annotated_element == self
        ]
        if self.owned_annotation != expected_owned_annotation:
            raise ConstraintsError("OwnedAnnotation constraint violated")

    def _check_derive_element_owned_element(self):
        """
        Constraint: The ownedElements of an Element are the ownedRelatedElements of its ownedRelationships.
        """
        expected_owned_element = [
            elem for rel in self.owned_relationship
            for elem in rel.owned_related_element
        ]
        if self.owned_element != expected_owned_element:
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
        expected_textual_representation = [elem for elem in self.owned_element if
                                           isinstance(elem, TextualRepresentation)]
        if self.textual_representation != expected_textual_representation:
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
        if any(rel.is_implied for rel in self.owned_relationship) and not self.is_implied_included:
            raise ConstraintsError("IsImpliedIncluded constraint violated")


class Relationship(Element):
    def __init__(self,
                 env: Env,
                 is_implied: bool,
                 source_element_ids: List[str],
                 target_element_ids: List[str],
                 element_id: Optional[str] = None):
        self._env = env
        self._is_implied = is_implied
        self._source = source_element_ids
        self._target = target_element_ids
        self._element_id = element_id if element_id is not None else str(uuid.uuid4())
        self._env[self._element_id] = self

    @property
    def element_id(self) -> str:
        return self._element_id

    @property
    def is_implied(self) -> bool:
        return self._is_implied

    @property
    def source(self) -> List[Element]:
        return [self._env[s] for s in self._source]

    @property
    def target(self) -> List[Element]:
        return [self._env[t] for t in self._target]

    @property
    def related_element(self) -> List[Element]:
        return self._get_related_element()

    def _get_related_element(self) -> List[Element]:
        # This should be a list of ElementProxy objects, ordered with source elements followed by target elements.
        # The list may contain non-unique elements.
        return [*self.source, *self.target]

    @property
    def owned_related_element(self) -> List[Element]:
        return self._get_owned_related_element()

    def _get_owned_related_element(self) -> List[Element]:
        # TODO: Implement this method to return the owned related elements.
        # This should be a list of ElementProxy objects that are owned by this Relationship.
        # These elements are a subset of relatedElement and should be ordered.
        raise NotImplementedError()

    @property
    def owning_related_element(self) -> Optional[Element]:
        return self._get_owning_related_element()

    def _get_owning_related_element(self) -> Optional[Element]:
        # TODO: Implement this method to return the owning related element.
        # This should return an ElementProxy object that owns this Relationship, if any.
        # It is a subset of relatedElement.
        raise NotImplementedError()

    def library_namespace(self) -> Optional['Namespace']:
        # Implement the libraryNamespace operation
        owning_related_element = self.owning_related_element
        if owning_related_element is not None:
            return owning_related_element.get().library_namespace()
        owning_relationship = self._get_owning_relationship()
        if owning_relationship is not None:
            return owning_relationship.library_namespace()
        return None

    def _get_owning_relationship(self) -> Optional['Relationship']:
        # TODO: Implement this method to return the owning relationship.
        # This should return an ElementProxy object that represents the owning relationship, if any.
        raise NotImplementedError()

    def check_constraints(self):
        """
        Check all constraints for the Relationship.
        Raises ConstraintsError if any constraint is not satisfied.
        """
        self._check_derive_relationship_related_element()

    def _check_derive_relationship_related_element(self):
        """
        Constraint: deriveRelationshipRelatedElement
        The relatedElements of a Relationship consist of all of its source Elements followed by all of its target Elements.
        relatedElement = source->union(target)
        """
        expected_related_elements = self.source + self.target
        if self.related_element != expected_related_elements:
            raise ConstraintsError(
                "The relatedElement property must be the union of source and target elements, in that order.")
