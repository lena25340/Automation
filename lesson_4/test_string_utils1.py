import pytest
from lesson_4.string_utils1 import StringUtils

utils = StringUtils()


@pytest.mark.positive_test
def test_positive_capitilize():


    assert utils.capitilize("Butterfly") == "Butterfly"
    assert utils.capitilize("%?№;") == "%?№;"
    assert utils.capitilize("0") == "0"


@pytest.mark.Negatives_test
def test_Negatives_capitilize():


    assert utils.capitilize("") == ""
    assert utils.capitilize("🤗🤗🤗") == "🤗🤗🤗"
    assert utils.capitilize("ملائكتي") == "ملائكتي"


@pytest.mark.parametrize("input_str, expected_result", [
     {"Butterfly", "Butterfly"},
     {"%?№;", "%?№;"},
     {"0", "0"}
])
def test_positive_capitalize(string, symbol, result):
    res = utils.capitilize(string)
    assert res == result


@pytest.mark.parametrize("input_str, expected_result", [
     {"", ""},
     {"🤗🤗🤗", "🤗🤗🤗"},
     {"لائكتي", "لائكتي"}
])
def test_Negatives_capitalize(string, symbol, result):
    res = utils.capitilize(string)
    assert res == result
