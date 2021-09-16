def sum_of_squares(a):
	sum = 0
	for i in a:
		sum += i*i
	return sum

def test_one():
    assert sum_of_squares([1,2,3]) == 14
if(sum_of_squares([1,2,3]) == 14):
	print(True)

def test_two():
    assert sum_of_squares([2,5,4]) == 45
if(sum_of_squares([2,5,4]) == 45):
	print(True)
