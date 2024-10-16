from .base import Element, Relationship


class AnnotatingElement(Element):
    pass


class Annotation(Relationship):
    pass


class Comment(AnnotatingElement):
    pass


class Documentation(Comment):
    pass


class TextualRepresentation(AnnotatingElement):
    pass
