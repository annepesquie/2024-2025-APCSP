import main

def test_1(): 
  assert main.problem_1() == "102030","problem_1() didn't return the str 102030"

def test_2():
  assert main.problem_2() == 60,"problem_2() didn't return the int 60"

def test_3():
  assert int(main.problem_3()) == 151015,"problem_3() didn't return the int 151015"

def test_4():
  assert int(main.problem_4()) == 26,"problem_4() didn't return the int 26"

def test_5():
  assert int(main.problem_5()) == 37,"problem_5() didn't return the int 37"

def test_6():
  assert int(main.problem_6()) == 90210,"problem_6() didn't return the int 90210"

test_1()
test_2()
test_3()
test_4()
test_5()
test_6()