import os.path


def list_file_resources():
    from pysysml import __file__ as _pysysml_file

    workdir = os.path.abspath('.')
    proj_dir = os.path.abspath(os.path.normpath(os.path.join(_pysysml_file, '..')))

    for root, _, files in os.walk(proj_dir):
        for file in files:
            _, ext = os.path.splitext(file)
            if ext in {'.txt', '.lark'}:
                rfile = os.path.abspath(os.path.join(root, file))
                dst_file = os.path.dirname(os.path.relpath(rfile, workdir))
                t = f'{rfile}{os.pathsep}{dst_file}'
                print(f'--add-data {t!r}')


if __name__ == '__main__':
    list_file_resources()
