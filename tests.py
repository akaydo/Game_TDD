from main import *

def test_1():
    try:
        a,q = get_question(1)
        assert a == "приз" and q ==  "сектор в игре <Поле чудес>"
    except:
        print('test error')
    else:
        print('test passed')

test_1()