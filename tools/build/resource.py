import os.path


def list_resources():
    from pysysml import __file__ as _pysysml_file

    proj_dir = os.path.abspath(os.path.normpath(os.path.join(_pysysml_file, '..')))
    for root, _, files in os.walk(proj_dir):
        if '__pycache__' in root:
            continue

        for file in files:
            _, ext = os.path.splitext(file)
            if ext != '.py':
                rfile = os.path.abspath(os.path.join(root, file))
                yield rfile


def print_resource_mappings():
    workdir = os.path.abspath('.')
    for rfile in list_resources():
        dst_file = os.path.dirname(os.path.relpath(rfile, workdir))
        t = f'{rfile}{os.pathsep}{dst_file}'
        print(f'--add-data {t!r}')


if __name__ == '__main__':
    print_resource_mappings()
