from src.mat_operations import add,sub,div

def test_add():
    assert add(2,3)==5
    assert add(-1,1)==0
    
def test_sub():
    assert sub(5,3)==2
    assert sub(4,3)==1
    assert sub(3,3)==0
    assert sub(2,3)==-1

def test_div():
    assert div(6,3)==2
    assert div(10,2)==5
    assert div(7,2)==3