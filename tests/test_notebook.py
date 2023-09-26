from lib.notebook import *

def test_instantiates_with_contents():
    notebook = Notebook()

    expected = []
    actual = notebook.contents

    assert actual == expected