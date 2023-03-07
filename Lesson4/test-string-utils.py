import pytest
from string_utils import StringUtils

@pytest.mark.parametrize('num1, result', [("hello", "Hello"),("Hello", "Hello"),('привет', 'Привет'),(' Hi', 'Hi')])
def test_Up_first(num1, result):
    test = StringUtils()
    res = test.capitilize(num1)
    assert res == result

@pytest.mark.parametrize('num1, result', [("   hello", "hello"),("H ello  ", "H ello  ")])
def Spaces_first(num1, result):
    test = StringUtils()
    res = test.trim(num1)
    assert res == result

@pytest.mark.parametrize('val, delim, result', [("1,2,3", ",",['1','2','3']),(" , , ,", ",",[' ',' ',' '])])
def Delim_count(val, delim, result):
    test = StringUtils()
    res = test.to_list(val, delim)
    assert res == result

@pytest.mark.parametrize('val, sumbol, result', [("1,2,3", "1",True),(" , , ,", " ",True),('abcdef','g',False)])
def Contain_sumbol(val, sumbol, result):
    test = StringUtils()
    res = test.contains(val, sumbol)
    assert res == result

@pytest.mark.parametrize('val, sumbol, result', [("1,2,3,1,2,3", "1",",2,3,,2,3"),("111111", "1",''),("aaaa","b","aaaa")])
def Sumbol_del(val, sumbol, result):
    test = StringUtils()
    res = test.delete_symbol(val, sumbol)
    assert res == result

@pytest.mark.parametrize('val, sumbol, result', [("1,2,3,1,2,3", "1",True),("111111", "2",False),("","",True)])
def Start_check(val, sumbol, result):
    test = StringUtils()
    res = test.starts_with(val, sumbol)
    assert res == result

@pytest.mark.parametrize('val, sumbol, result', [("1,2,3,1,2,3", "3",True),("111111", "2",False),("","",True)])
def End_check(val, sumbol, result):
    test = StringUtils()
    res = test.end_with(val, sumbol)
    assert res == result

@pytest.mark.parametrize('val, result', [("1,2,3,1,2,3", False),("      ",False),("",True)])
def Str_check(val, result):
    test = StringUtils()
    res = test.is_empty(val)
    assert res == result

@pytest.mark.parametrize('val, delim, result', [([1,2,3,1,2,3], '*', "1*2*3*1*2*3"),([1,2,3], '', "123"),([], '*', "")])
def Str_delim(val, delim, result):
    test = StringUtils()
    res = test.list_to_string(val,delim)
    assert res == result