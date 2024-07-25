import pytest
from string_utils import StringUtils

utils = StringUtils()

def test_capitalize():
    #"""Positive"""
    assert utils.capitilize("skypro") == "Skypro"
    assert utils.capitilize("hello world") == "Hello world"
    assert utils.capitilize("123") == "123"
   # """Negative"""
    assert utils.capitilize("") == ""
    assert utils.capitilize("  ") == "  "
    assert utils.capitilize("12345тест") == "12345тест"\
    
#"""trim"""


def test_trim():
    #"""Positive"""
    assert utils.trim("    skypro") == "skypro"
    assert utils.trim("    hello world    ") == "hello world    "
    assert utils.trim("   SKY   ") == "SKY   "
   # """Negative"""
    assert utils.trim("") == ""


#"""to_list"""


@pytest.mark.parametrize('string, delimeter, result', [
#"""Pozitive"""
    ('яблоко,банан,апельсин', ",", ["яблоко", "банан", "апельсин"]),
    ("1,2,3,4,5", ",", ["1", "2", "3", "4", "5"]),
    ("*@$@%@&", "@", ["*", "$","%", "&"]),
#"""Negative"""
    ("", None, []),
    ("1,2,3,4 5", None, ['1', '2', '3', '4 5']),
])
def test_to_list(string, delimeter, result):
    if delimeter is None:
        res = utils.to_list(string)
    else:
        res = utils.to_list(string, delimeter)
    assert res == result


# """Contains"""
@pytest.mark.parametrize("string, symbol, result", [
    #positive
    ("банан", "б", True),
    (" гвоздь", "д", True),
    ("мир  ", "р",True),
    ("диван-кровать", "-", True),
    ("145", "1", True),
    ("", "", True),
    #negative
    ("Москва", "м", False),
    ("привет", "з", False),
    ("кот", "%", False),
    ("", "3", False),
    ("12345", "h", False),
])
def test_contains(string, symbol, result):
    res = utils.contains(string, symbol)
    assert res == result

#"""Delete_symbol"""
    
@pytest.mark.parametrize("string, symbol, result", [
     #positive
        ("корень", "к", "орень"),
        ("Женя", "н", "Жея"),
        ("Море", "М", "оре"),
        ("123", "1", "23"),
        ("Красная Площадь", " ", "КраснаяПлощадь"),
    #negative
        ("ножик", "з", "ножик"),
        ("", "", ""),
        ("", "С", ""),
        ("кофе", "", "кофе"),
        ("зелень ", " ", "зелень")
 ])
def test_delete_symbol(string, symbol, result):
    res = utils.delete_symbol(string, symbol)
    assert res == result


# """Starts_with"""

@pytest.mark.parametrize("string, symbol, result", [
        #positive
        ("светофор", "с", True),
        ("", "", True),
        ("Москва", "М", True),
        ("Film", "F", True),
        ("Мира-Зина", "М", True),
        ("123", "1", True),
        #negative
        ("Ваня", "а", False),
        ("мир", "М", False),
        ("", "0", False),
        ("плащь", "ж", False),
        ("зверь", "н", False)
    ])
def test_starts_with(string, symbol, result):
    res = utils.starts_with(string, symbol)
    assert res == result

# """end_with"""


@pytest.mark.parametrize("string, symbol, result", [
    #positive
    ("Мария", "я", True),
    ("ТОРТИК", "К", True),
    ("", "", True),
    ("собака ", " ", True),
    ("67", "7", True),
    ("ONE-TWo", "o", True),
    ("Петр1", "1", True),
    ("БаобаБ", "Б", True),
    #negative
    ("природа", "л", False),
    ("тигр", "с", False),
    ("дверь", "Ь", False),
    ("", "*", False)
])
def test_end_with(string, symbol, result):
    res = utils.end_with(string, symbol)
    assert res == result


    """is_empty"""

@pytest.mark.parametrize("string, result", [
    #positive
    ("", True),
    (" ", True),
    ("  ", True),
    #negative
    ("не пусто", False),
    (" не пусто с пробелом ", False),
    ("345", False),
])

def test_is_empty(string, result):
    res = utils.is_empty(string)
    assert res == result


"""list_to_string"""

@pytest.mark.parametrize("lst, joiner, result", [
    #positive
    (['s', 'o', 's'], ",", "s,o,s"),
    (["1,2,3,4,5"], None, "1,2,3,4,5"),
    (["Первый", "Второй"], "-", "Первый-Второй"),
    (["Первый", "Второй"], "Середина", "ПервыйСерединаВторой"),
    (["в", "у", "з"], "", "вуз"),
    #negative
    ([], None, ""),
    ([], ",", ""),
    ([], "кот", "")
])
def test_list_to_string(lst, joiner, result):
    if joiner == None:
        res = utils.list_to_string(lst)
    else:
        res = utils.list_to_string(lst, joiner)
    assert res == result

