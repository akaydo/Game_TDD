from main import *

def test_1():
    try:
        a,q = get_question(1)
        assert a == "стаж" and q == "Общая продолжительность трудовой деятельности"
    except:
        print('test error')
    else:
        print('test passed')

def test_2():
    try:
        t = encrypt('well')
        assert t == ['*','*','*','*']
    except:
        print('test error')
    else:
        print('test passed')

def test_3_1():
    try:
        t = guess_letter('word', ['*','*','*','*'], 'o')
        assert t == ['*','o','*','*']
    except:
        print('test error')
    else:
        print('test passed')

def test_3_2():
    try:
        t = guess_letter('word', ['*','*','*','*'], 'к')
        assert t == ['*','*','*','*']
    except:
        print('test error')
    else:
        print('test passed')

def test_3_3():
    try:
        t = guess_letter('слово', ['*','*','*','*','*'], 'о')
        assert t == ['*','*','о','*','о']
    except:
        print('test error')
    else:
        print('test passed')

def test_4_1():
    try:
        assert guess_word("слово", "слово")
    except:
        print('test error')
    else:
        print('test passed')

def test_4_2():
    try:
        t = guess_word("слово", "слова")
        assert t != True
    except:
        print('test error')
    else:
        print('test passed')

test_1()
test_2()
test_3_1()
test_3_2()
test_3_3()
test_4_1()
test_4_2()
