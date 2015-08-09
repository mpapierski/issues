import os
import subprocess
import tempfile


def call_editor(content):
    '''Calls $EDITOR and returns edited content
    '''
    editor = os.environ['EDITOR']
    with tempfile.NamedTemporaryFile(suffix='.tmp') as f:
        f.write(content)
        f.flush()
        subprocess.call([
            editor,
            f.name
        ])
        with open(f.name) as f2:
            new_content = f2.read()
            if not new_content:
                return None
            return new_content
