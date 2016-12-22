c1 = ' bottles of beer on the wall'
c2 = ' bottles of beer,\n Take one down and pass it aroud,'
count = 98
while count != 0:
	print('',(count+1),c1+',','\n',(count+1),c2,'\n',count,c1+'.','\n')
	count=count-1
print('',(count+1),' bottle of beer on the wall,','\n',(count+1),
	' bottle of beer,\n Take one down and pass it aroud,','\n',
	'No more bottles of beer on the wall.')