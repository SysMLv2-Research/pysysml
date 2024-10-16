from enum import Enum, unique

from .base import Element, Relationship


class Namespace(Element):
    pass


class Membership(Relationship):
    pass


class OwningMembership(Membership):
    pass


class Import(Relationship):
    pass


class NamespaceImport(Import):
    pass


class MembershipImport(Import):
    pass


@unique
class VisibilityKind(Enum):
    pass
