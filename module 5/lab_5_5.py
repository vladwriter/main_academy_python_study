numb_lst = [i for i in range(1, 6)]


def my_generator(lst):
	for el in lst:
		yield lst.index(el) + 1, el


for i in my_generator(numb_lst):
	print(i)
