import pytest

from pysysml.kerml.cst import list_reserved_words, is_reserved_word, resource_health_check


@pytest.mark.unittest
class TestKermlBase:
    @pytest.mark.parametrize(['rword'], [
        ('about',),
        ('abstract',),
        ('alias',),
        ('all',),
        ('and',),
        ('as',),
        ('assoc',),
        ('behavior',),
        ('binding',),
        ('bool',),
        ('by',),
        ('chains',),
        ('class',),
        ('classifier',),
        ('comment',),
        ('composite',),
        ('conjugate',),
        ('conjugates',),
        ('conjugation',),
        ('connector',),
        ('datatype',),
        ('default',),
        ('dependency',),
        ('derived',),
        ('differences',),
        ('disjoining',),
        ('disjoint',),
        ('doc',),
        ('else',),
        ('end',),
        ('expr',),
        ('false',),
        ('feature',),
        ('featured',),
        ('featuring',),
        ('filter',),
        ('first',),
        ('flow',),
        ('for',),
        ('from',),
        ('function',),
        ('hastype',),
        ('if',),
        ('intersects',),
        ('implies',),
        ('import',),
        ('in',),
        ('inout',),
        ('interaction',),
        ('inv',),
        ('inverse',),
        ('inverting',),
        ('istype',),
        ('language',),
        ('member',),
        ('metaclass',),
        ('metadata',),
        ('multiplicity',),
        ('namespace',),
        ('nonunique',),
        ('not',),
        ('null',),
        ('of',),
        ('or',),
        ('ordered',),
        ('out',),
        ('package',),
        ('portion',),
        ('predicate',),
        ('private',),
        ('protected',),
        ('public',),
        ('readonly',),
        ('redefines',),
        ('redefinition',),
        ('references',),
        ('rep',),
        ('return',),
        ('specialization',),
        ('specializes',),
        ('step',),
        ('struct',),
        ('subclassifier',),
        ('subset',),
        ('subsets',),
        ('subtype',),
        ('succession',),
        ('then',),
        ('to',),
        ('true',),
        ('type',),
        ('typed',),
        ('typing',),
        ('unions',),
        ('xor',)
    ])
    def test_list_reserved_words(self, rword):
        assert rword in list_reserved_words()

    @pytest.mark.parametrize(['rword', 'is_reserved'], [
        ('about', True),
        ('abstract', True),
        ('alias', True),
        ('all', True),
        ('and', True),
        ('as', True),
        ('assoc', True),
        ('behavior', True),
        ('binding', True),
        ('bool', True),
        ('by', True),
        ('chains', True),
        ('class', True),
        ('classifier', True),
        ('comment', True),
        ('composite', True),
        ('conjugate', True),
        ('conjugates', True),
        ('conjugation', True),
        ('connector', True),
        ('datatype', True),
        ('default', True),
        ('dependency', True),
        ('derived', True),
        ('differences', True),
        ('disjoining', True),
        ('disjoint', True),
        ('doc', True),
        ('else', True),
        ('end', True),
        ('expr', True),
        ('false', True),
        ('feature', True),
        ('featured', True),
        ('featuring', True),
        ('filter', True),
        ('first', True),
        ('flow', True),
        ('for', True),
        ('from', True),
        ('function', True),
        ('hastype', True),
        ('if', True),
        ('intersects', True),
        ('implies', True),
        ('import', True),
        ('in', True),
        ('inout', True),
        ('interaction', True),
        ('inv', True),
        ('inverse', True),
        ('inverting', True),
        ('istype', True),
        ('language', True),
        ('member', True),
        ('metaclass', True),
        ('metadata', True),
        ('multiplicity', True),
        ('namespace', True),
        ('nonunique', True),
        ('not', True),
        ('null', True),
        ('of', True),
        ('or', True),
        ('ordered', True),
        ('out', True),
        ('package', True),
        ('portion', True),
        ('predicate', True),
        ('private', True),
        ('protected', True),
        ('public', True),
        ('readonly', True),
        ('redefines', True),
        ('redefinition', True),
        ('references', True),
        ('rep', True),
        ('return', True),
        ('specialization', True),
        ('specializes', True),
        ('step', True),
        ('struct', True),
        ('subclassifier', True),
        ('subset', True),
        ('subsets', True),
        ('subtype', True),
        ('succession', True),
        ('then', True),
        ('to', True),
        ('true', True),
        ('type', True),
        ('typed', True),
        ('typing', True),
        ('unions', True),
        ('xor', True),

        ('variable', False),
        ('functionName', False),
        ('class_name', False),
        ('_private_var', False),
        ('CONSTANT_VALUE', False),
        ('camelCase', False),
        ('snake_case', False),
        ('mixedCase_123', False),
        ('with_number1', False),
        ('_123numericStart', False),
    ])
    def test_is_reserved_word(self, rword, is_reserved):
        assert is_reserved_word(rword) == is_reserved

    def test_resource_health_check(self):
        resource_health_check()
