from src.math_operation import add,sub

def test_add():
    assert add(2,3)==5
    assert add(0,2)==2


def test_sub():
    assert sub(5,8)==-3
    assert sub(9,10)==1
    