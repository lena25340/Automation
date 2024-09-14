import pytest
from lesson_4.string_utils import StringUtils

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
def test_positive_capitalize(input_str, expected_result):
    res = utils.capitilize(input_str)
    assert res == expected_result


@pytest.mark.parametrize("input_str, expected_result", [
     {"", ""},
     {"🤗🤗🤗", "🤗🤗🤗"},
     {"لائكتي", "لائكتي"}
])
def test_Negatives_capitalize(input_str, expected_result):
    res = utils.capitilize(input_str)
    assert res == expected_result

@pytest.mark.positive_test
def test_positive_trim ():


    assert utils.trim (" дом") == "дом"
    assert utils.trim ("  введите слово ") == "введите слово "
    assert utils.trim (" 675") == "675"
    
@pytest.mark.Negatives_test
def test_Negatives_trim():
    
    assert utils.trim ("") == ""
    assert utils.capitilize("🤗🤗🤗") == "🤗🤗🤗"
    assert utils.capitilize("ملائكتي") == "ملائكتي"

@pytest.mark.xfail() 
def test_trim_with_numbers_input ():
    assert utils.trim ("675") =="675"


@pytest.mark.parametrize ('string, delimeter, result', [

    ("one,two,three", ",", ["one", "two", "three"]),
    ("1,2,3,4,5", None, ["1", "2", "3", "4", "5"]),
    ("@^%^&^!^*", "^", ["@", "%", "&", "!", "*"]),
    #NEGATIVE:
    ("", None, []),
    ("1,2,3,4 5", None, ["1", "2", "3", "4 5"]),
    ])

def test_to_list(string, delimeter, result):
    if delimeter is None:
        res = utils.to_list(string)
    else:
        res = utils.to_list(string, delimeter)
    assert res == result

@pytest.mark.parametrize ('string, symbol, result', [
    #POSITIVE:
    ("oksana", "o", True),
    (" test", "t", True),
    ("space  ", "e", True),
    ("who-who", "-", True),
    ("123", "1", True),
    ("", "", True),
    #NEGATIVE:
    ("City", "c", False),
    ("parameter", "P", False),
    ("hello", "x", False),  
    ("12345", "!", False),  
    ("", "x", False),  
    # (("hello", "", False))
])

def test_contains(string, symbol, result):
    res = utils.contains (string, symbol)
    assert res == result


@pytest.mark.parametrize('string, symbol, result', [
    #POSITIVE:
    ("test", "t", True),
    ("", "", True),
    (" Учеба", "", True),
    ("Forewer  ", "F", True),
    ("123", "1", True),
    #NEGATIVE:
    ("Summer", "s", False),
    ("fall", "F", False),
    ("", "v", False),
    ("winter", "e", False),
    
])
def test_starts_with(string, symbol, result):
    res = utils.starts_with(string, symbol)
    assert res == result

@pytest.mark.parametrize('string, symbol, result', [
    #Позитивные проверки:
    ("coffee", "e", True),
    ("teA", "A", True),
    ("", "", True),
    ("one ", "", True),
    ("123", "3", True),
    ("why-why", "y", True),
    ("test ", "", True),
    #Негативные проверки:
    ("one", "P", False),
    ("two", "e", False),
    ("Three", "E", False),
    ("", "n", False)
])
def test_end_with(string, symbol, result):
    res = utils.end_with(string, symbol)
    assert res == result

@pytest.mark.parametrize('string, result', [
    #POSITIVE:
    ("", True),
    (" ", True),
    ("  ", True),
    #NEGATIVE:
    ("tree", False),
    (" one", False),
    ("123", False),
    ("town ", False)   
])
def test_is_empty(string, result):
    res = utils.is_empty(string)
    assert res == result

@pytest.mark.parametrize('lst, joiner, result', [
    #POSITIVE:
    (["a", "b", "c"], ",", "a,b,c"),
    ([1,2,3,4,5], None, "1, 2, 3, 4, 5"),
    (["a", "b", "c"], "", "abc"),
    (["Юго", "Западный"], "-", "Юго-Западный"),
    (["Юго", "ветер"], "Западный", "ЮгоЗападныйветер"),
    #NEGATIVE:
    ([], None, ""),
    ([], "*", "")
])
def test_list_to_string(lst, joiner, result):
    if joiner == None:
        res = utils.list_to_string(lst)
    else:
        res = utils.list_to_string(lst, joiner)
    assert res == result