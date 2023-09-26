from lib.notebook import *

def test_instantiates_with_contents():
    notebook = Notebook()

    expected = []
    actual = notebook.contents

    assert actual == expected

def test_add_one_note():
    notebook = Notebook()

    notebook.add('entry 1')

    assert notebook.contents[0] == 'entry 1'
    assert 'entry 1' in notebook.contents

def test_add_one_note_with_actual_and_expected():
    # input output
    # setup
    notebook = Notebook()

    # act / action
    notebook.add('entry 1')

    actual = notebook.contents
    expected = ['entry 1']

    # assertion
    assert actual == expected