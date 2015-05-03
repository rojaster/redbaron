from redbaron import RedBaron


def test_import_modules():
    red = RedBaron("import a, b.c, d.e as f")
    assert red[0].modules() == ['a', 'b.c', 'd.e']


def test_import_names():
    red = RedBaron("import a, b.c, d.e as f")
    assert red[0].names() == ['a', 'b.c', 'f']


def test_from_import_names():
    red = RedBaron("from qsd import a, c, e as f")
    assert red[0].names() == ['a', 'c', 'f']


def test_from_import_modules():
    red = RedBaron("from qsd import a, c, e as f")
    assert red[0].modules() == ['a', 'c', 'e']


def test_from_import_full_path_names():
    red = RedBaron("from qsd import a, c, e as f")
    assert red[0].full_path_names() == ['qsd.a', 'qsd.c', 'qsd.f']


def test_from_import_full_path_modules():
    red = RedBaron("from qsd import a, c, e as f")
    assert red[0].full_path_modules() == ['qsd.a', 'qsd.c', 'qsd.e']


def test_to_python_int_node():
    red = RedBaron("1")
    assert red[0].value == "1"
    assert red[0].to_python() == 1


def test_to_python_float_node():
    red = RedBaron("1.1")
    assert red[0].value == "1.1"
    assert red[0].to_python() == 1.1


def test_to_python_octa_node():
    red = RedBaron("0011")
    assert red[0].value == "0011"
    assert red[0].to_python() == 9


def test_to_python_hexa_node():
    red = RedBaron("0xFF")
    assert red[0].value == "0xFF"
    assert red[0].to_python() == 255


def test_to_python_long_node():
    red = RedBaron("10L")
    assert red[0].value == "10L"
    assert red[0].to_python() == 10L


def test_to_python_binary_node():
    red = RedBaron("0b101010101")
    assert red[0].value == "0b101010101"
    assert red[0].to_python() == 341


def test_to_python_float_exponant_node():
    red = RedBaron("1.1e1")
    assert red[0].value == "1.1e1"
    assert red[0].to_python() == 11.0


def test_to_python_string_node():
    red = RedBaron("'pouet'")
    assert red[0].value == "'pouet'"
    assert red[0].to_python() == 'pouet'


# TODO to_python for "strings, tuples, lists, dicts, booleans, and None"
