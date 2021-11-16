# loop.py
value =5
while value > 0 :
	print(value)
	value -=1

lst = [100, "apple", 3.14]
for item in list:
	print(item)

for x in [2,3,4,5,6]:
	print("---{0}단---".format(x))
	for y in [1,2,3,4,5,6,7,8,9]:
		print("{0} * {1} = {2}".format(x,y, x*y))
