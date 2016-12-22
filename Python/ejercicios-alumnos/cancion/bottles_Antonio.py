
for i in range(99,0,-1):
    dif=i-1
    if dif < 1 :
        print(i, 'bottle of beer on the wall,\n',i, 'bottles of beer,\n','Take one down and pass it arraund,\n','No more bottles of beer on the wall.\n\n')
    else:
        print(i, 'bottles of beer on the wall,\n',i, 'bottles of beer,\n','Take one down and pass it arraund,\n',i-1, 'bottles of beer on the wall.\n\n')
    print()
