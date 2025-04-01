import pytest
from string_utils import StringUtils

stroka = StringUtils()

# capitilize

# позитивные проверки замены первой буквы строки на заглавную
@pytest.mark.positive_test
@pytest.mark.capitilize
@pytest.mark.parametrize('str, result', [
    ("skypro", "Skypro"), 
    ("s", "S"), 
    ("Skypro", "Skypro"), 
    ("skypro - the best online school", "Skypro - the best online school"), 
    ("moscow is the capital of Russia", "Moscow is the capital of Russia")
    ])
def test_first_symb_positive(str, result):
    stroka = StringUtils()
    res = stroka.capitilize(str)
    assert res == result

# негативные проверки замены первой буквы на заглавную
@pytest.mark.negative_test
@pytest.mark.capitilize
@pytest.mark.parametrize('str, result', [
    ("123skypro", "123skypro"), 
    (" skypro", " Skypro"),
    ("", "")
    ])
def test_first_symb_negative(str, result):
    stroka = StringUtils()
    res = stroka.capitilize(str)
    assert res == result


@pytest.mark.negative_test
@pytest.mark.capitilize
# stroka = None
def test_string_none():
    stroka = StringUtils()
    with pytest.raises(AttributeError):
        stroka.capitilize(None)

@pytest.mark.negative_test
@pytest.mark.capitilize
# stroka = integer
def test_no_string():
    stroka = StringUtils()
    with pytest.raises(AttributeError):
        stroka.capitilize(123)


# trim

# позитивные проверки удаления пробелов в начале строки
@pytest.mark.trim
@pytest.mark.positive_test
@pytest.mark.parametrize('str, result', [ 
    (" skypro", "skypro"), 
    ("     skypro", "skypro"), 
    ("skypro", "skypro"), 
    ("skypro ", "skypro "), 
    (" Skypro - the best online school", "Skypro - the best online school")
    ])
def test_trim_positive(str, result):
    stroka = StringUtils()
    res = stroka.trim(str)
    assert res == result

# негативные проверки удаления пробелов в начале строки
@pytest.mark.trim
@pytest.mark.negative_test
@pytest.mark.parametrize('str, result', [ 
    (" ", ""), 
    ("      ", "")
    ])
def test_trim_negative(str, result):
    stroka = StringUtils()
    res = stroka.trim(str)
    assert res == result


# stroka = None
@pytest.mark.trim
@pytest.mark.negative_test
def test_trim_string_none():
    stroka = StringUtils()
    with pytest.raises(AttributeError):
        stroka.trim(None)



# to_list


@pytest.mark.positive_test
@pytest.mark.to_list_tests
@pytest.mark.parametrize('str, result',[
    ("a,b,c,d", ["a", "b", "c", "d"]),
    ("1,2,3,4,5", ['1', '2', '3', '4', '5']),
    ("a,,b,cd", ['a', '', 'b', 'cd'])
])
def test_to_list_positive(str, result):
    stroka = StringUtils()
    res = stroka.to_list(str)
    assert res == result

@pytest.mark.positive_test
@pytest.mark.to_list_tests
@pytest.mark.parametrize('str, delimeter, result',[
    ("a/b/c/d", "/", ["a", "b", "c", "d"]),
    ("1*2*3*4*5", "*", ['1', '2', '3', '4', '5']),
    ("a b cd hello", " ", ['a', 'b', 'cd', 'hello']),
    ("a d h,r i l,r h y", ",", ["a d h", "r i l", "r h y"]),
    ("My\tname\tis\tIvan", "\t", ["My", "name", "is", "Ivan"])
])
def test_to_list_del(str, delimeter, result):
    stroka = StringUtils()
    res = stroka.to_list(str, delimeter)
    assert res == result


@pytest.mark.negative_test
@pytest.mark.to_list_tests
def test_to_list_neg():
    stroka = StringUtils()
    res = stroka.to_list("a/b/c/d", "/")
    assert res == ['a', 'b', 'c', 'd']


@pytest.mark.negative_test
@pytest.mark.to_list_tests
def test_to_list_none():
    stroka = StringUtils()
    with pytest.raises(AttributeError):
        stroka.to_list(None, "/")


# contains


@pytest.mark.cont_func
@pytest.mark.positive_test
@pytest.mark.parametrize('str, symb, result', [
    ("SkyPro", "S", True), 
    ("SkyPro", "s", True), 
    ("SkyPro", " ", False), 
    ("SkyPro", "k", True), 
    ("SkyPro", "P", True),
    ("SkyPro", "Sky", True),
    ("SkyPro - the best online school", "skypro", True),
    ("SkyPro - the best online school", "-", True),
    ("SkyPro - the best online school 🤔", "🤔", True),
    ("SkyPro - лучшая онлайн школа", "ш", True)
    ])
def test_contains_positive(str, symb, result):
    stroka = StringUtils()
    res = stroka.contains(str, symb)
    assert res == result

@pytest.mark.cont_func
@pytest.mark.negative_test
@pytest.mark.parametrize('str, symb, result', [
    ("SkyPro", " ", False), 
    ("SkyPro", ".", False), 
    ("", "a", False)
    ])
def test_contains_negative(str, symb, result):
    stroka = StringUtils()
    res = stroka.contains(str, symb)
    assert res == result


@pytest.mark.cont_func
@pytest.mark.negative_test
def test_test_contains_negative_none_str():
    stroka = StringUtils()
    with pytest.raises(AttributeError):
        stroka.contains(None, "")


@pytest.mark.cont_func
@pytest.mark.negative_test
def test_test_contains_negative_none_symb():
    stroka = StringUtils()
    with pytest.raises(TypeError):
        stroka.contains("SkyPro", None)

# delete_symbol

@pytest.mark.delete_func
@pytest.mark.positive_test
@pytest.mark.parametrize('str, symb, result', [
    ("SkyPro", "S", "kyPro"),
    ("SkyPro", "Sky", "Pro"),
    ("SkyPro", "s", "kyPro"),
    ("SkyPro - the best online school", "online", "SkyPro - the best  school"),
    ("SkyPro - the best online school", " ", "SkyPro-thebestonlineschool"),
    ("SkyPro - the best online school", "s", "SkyPro - the bet online chool"),
    ("SkyPro", " ", "SkyPro"),
    ("3,1415926535897932384626433832795028841971", "1", "3,459265358979323846264338327950288497"),
    ("SkyPro - the best online school", "123", "SkyPro - the best online school")
    ])
def test_delete_positive(str, symb, result):
    stroka = StringUtils()
    res = stroka.delete_symbol(str, symb)
    assert res == result

@pytest.mark.delete_func
@pytest.mark.negative_test
@pytest.mark.parametrize('str, symb, result', [
    ("SkyPro - the best online school", "internet", "SkyPro - the best online school"),
    ("SkyPro\n - the\n best\n online\n school", "\n", "SkyPro - the best online school"),
    ("SkyPro 🤔- the best online school🤔", "🤔", "SkyPro - the best online school"),
    ("SkyPro", "SkyPro", "")
    ])
def test_delete_tests_negative(str, symb, result):
    stroka = StringUtils()
    res = stroka.delete_symbol(str, symb)
    assert res == result


@pytest.mark.delete_func
@pytest.mark.negative_test
def test_delete_nums_negative():
    stroka = StringUtils()
    with pytest.raises(AttributeError):
        stroka.delete_symbol(31415926535897932384626433832795028841971, 1)


@pytest.mark.delete_func
@pytest.mark.negative_test
def test_delete_str_num_negative():
    stroka = StringUtils()
    with pytest.raises(TypeError):
        stroka.delete_symbol("31415926535897932384626433832795028841971", 1)

@pytest.mark.delete_func
@pytest.mark.negative_test
def test_delete_str_none():
    stroka = StringUtils()
    with pytest.raises(AttributeError):
        stroka.delete_symbol(None, "a")


@pytest.mark.delete_func
@pytest.mark.negative_test
def test_delete_symb_none():
    stroka = StringUtils()
    with pytest.raises(TypeError):
        stroka.delete_symbol("SkyPro", None)

# starts_with


@pytest.mark.start_with
@pytest.mark.positive_test
@pytest.mark.parametrize('str, symb, result', [
    ("SkyPro", "S", True),
    ("12 SkyPro - the best online school", "1", True),
    (" SkyPro - the best online school", " ", True),
    ("🤔 SkyPro - the best online school", "🤔", True)
    ])
def test_start_positive(str, symb, result):
    stroka = StringUtils()
    res = stroka.starts_with(str, symb)
    assert res == result


@pytest.mark.start_with
@pytest.mark.negative_test
@pytest.mark.parametrize('str, symb, result', [
    ("SkyPro", "F", False),
    ("", "A", False)
    ])
def test_start_negative(str, symb, result):
    stroka = StringUtils()
    res = stroka.starts_with(str, symb)
    assert res == result


@pytest.mark.start_with
@pytest.mark.negative_test
def test_start_num_str_negative():
    stroka = StringUtils()
    with pytest.raises(AttributeError):
        stroka.starts_with(1587463, "1")


@pytest.mark.start_with
@pytest.mark.negative_test
def test_start_nums_negative():
    stroka = StringUtils()
    with pytest.raises(AttributeError):
        stroka.starts_with(9875265, 9)

@pytest.mark.start_with
@pytest.mark.negative_test
def test_start_strs_negative():
    stroka = StringUtils()
    with pytest.raises(TypeError):
        stroka.starts_with("12 SkyPro - the best online school", 1)


@pytest.mark.start_with
@pytest.mark.negative_test
def test_start_none_negative():
    stroka = StringUtils()
    with pytest.raises(TypeError):
        stroka.starts_with("12 SkyPro - the best online school", None)


@pytest.mark.start_with
@pytest.mark.negative_test
def test_start_str_none_negative():
    stroka = StringUtils()
    with pytest.raises(AttributeError):
        stroka.starts_with(None, "a")



# end_with

@pytest.mark.end_with
@pytest.mark.positive_test
@pytest.mark.parametrize('str, symb, result', [
    ("SkyPro", "o", True),
    ("SkyPro - the best online school 125", "125", True),
    ("SkyPro - the best online school ", " ", True),
    ("SkyPro - the best online school!", "!", True),
    ("SkyPro - the best online school 🤔", "🤔", True)
    ])
def test_start_positive(str, symb, result):
    stroka = StringUtils()
    res = stroka.end_with(str, symb)
    assert res == result


@pytest.mark.end_with
@pytest.mark.negative_test
@pytest.mark.parametrize('str, symb, result', [
    ("SkyPro", "F", False),
    ("", "A", False)
    ])
def test_start_negative(str, symb, result):
    stroka = StringUtils()
    res = stroka.end_with(str, symb)
    assert res == result


@pytest.mark.end_with
@pytest.mark.negative_test
def test_start_num_str_negative():
    stroka = StringUtils()
    with pytest.raises(AttributeError):
        stroka.end_with(1587463, "3")


@pytest.mark.end_with
@pytest.mark.negative_test
def test_start_nums_negative():
    stroka = StringUtils()
    with pytest.raises(AttributeError):
        stroka.end_with(9875265, 5)

@pytest.mark.end_with
@pytest.mark.negative_test
def test_start_strs_negative():
    stroka = StringUtils()
    with pytest.raises(TypeError):
        stroka.end_with("SkyPro - the best online school 1", 1)


@pytest.mark.end_with
@pytest.mark.negative_test
def test_start_none_negative():
    stroka = StringUtils()
    with pytest.raises(TypeError):
        stroka.end_with("SkyPro - the best online school", None)


@pytest.mark.end_with
@pytest.mark.negative_test
def test_end_str_none_negative():
    stroka = StringUtils()
    with pytest.raises(AttributeError):
        stroka.end_with(None, "a")



# is_empty

    
@pytest.mark.is_empty
@pytest.mark.positive_test
def test_is_empty():
    stroka = StringUtils()
    res = stroka.is_empty("")
    assert res == True

@pytest.mark.is_empty
@pytest.mark.negative_test
@pytest.mark.parametrize("str, result", [
    ("SkyPro - the best online school", False), 
    (' ', False), ("  ", False), 
    ("!%$", False), 
    ("🤔", False)
    ])
def test_isnt_empty(str, result):
    stroka = StringUtils()
    res = stroka.is_empty(str)
    assert res == result


@pytest.mark.is_empty
@pytest.mark.negative_test
def test_is_empty_nums():
    stroka = StringUtils()
    with pytest.raises(AttributeError):
        stroka.is_empty(123)


@pytest.mark.is_empty
@pytest.mark.negative_test
def test_is_empty_none():
    stroka = StringUtils()
    with pytest.raises(AttributeError):
        stroka.is_empty(None)



# list_to_string



@pytest.mark.list_to_string
@pytest.mark.positive_test
@pytest.mark.parametrize('lst, joiner, result', [
    (["Sky", "Pro"], "-", "Sky-Pro"), 
    ([1,2,3,4], ",",  "1,2,3,4"),
    (["raz", 2, "tri"], "/", "raz/2/tri"),
    ([], "!", ""),
    (["Sky"], "*", "Sky"),
    (["a", "b", "c"], "@", "a@b@c"),
    ([1, "d", True, None], " ! ", "1 ! d ! True ! None")
    ])
def test_list_to_string_positive(lst, joiner, result):
    listtostring = StringUtils()
    res = listtostring.list_to_string(lst, joiner)
    assert res == result


@pytest.mark.list_to_string
@pytest.mark.positive_test
def test_list_to_string_positive_default():
    listtostring = StringUtils()
    res = listtostring.list_to_string([1,2,3,4])
    assert res == "1, 2, 3, 4"