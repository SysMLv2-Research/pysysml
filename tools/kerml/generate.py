import os.path
import pathlib

from pysysml.utils import list_rules_from_grammar


def _get_all_starts():
    from pysysml.kerml import __grammar_file__
    grammar_code = pathlib.Path(__grammar_file__).read_text()
    return list_rules_from_grammar(grammar_code=grammar_code)


def main():
    all_starts = _get_all_starts()
    from pysysml.kerml.transforms import __file__ as _template_file

    template_file = os.path.normpath(os.path.join(_template_file, '..', 'template.py'))
    with open(template_file, 'w') as f:
        print(f'from lark import Transformer, v_args, Tree', file=f)
        print(f'', file=f)
        print(f'', file=f)
        print(f'class KerMLTransTemplate(Transformer):', file=f)
        for s in all_starts:
            print(f'    @v_args(tree=True)', file=f)
            print(f'    def {s}(self, tree: Tree):', file=f)
            print(f'        return tree', file=f)
            print(f'', file=f)

    recorder_file = os.path.normpath(os.path.join(_template_file, '..', 'recorder.py'))
    with open(recorder_file, 'w') as f:
        print(f'from lark import v_args, Tree', file=f)
        print(f'', file=f)
        print(f'from .template import KerMLTransTemplate', file=f)
        print(f'', file=f)
        print(f'', file=f)
        print(f'class KerMLTransRecorder(KerMLTransTemplate):', file=f)
        print(f'    def __init__(self, visit_tokens: bool = True):', file=f)
        print(f'        KerMLTransTemplate.__init__(self, visit_tokens=visit_tokens)', file=f)
        print(f'        self._rules_set = set()', file=f)
        print(f'        self.rules = []', file=f)
        print(f'', file=f)
        for s in all_starts:
            print(f'    @v_args(tree=True)', file=f)
            print(f'    def {s}(self, tree: Tree):', file=f)
            print(f'        if {s!r} not in self._rules_set:', file=f)
            print(f'            self._rules_set.add({s!r})', file=f)
            print(f'            self.rules.append({s!r})', file=f)
            print(f'        return KerMLTransTemplate.{s}(self, tree)', file=f)
            print(f'', file=f)


if __name__ == '__main__':
    main()
