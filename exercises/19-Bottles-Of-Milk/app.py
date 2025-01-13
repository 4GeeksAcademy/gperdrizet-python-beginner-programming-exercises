def number_of_bottles():

    for i in range(100, 0, -1):
        
        i-=1

        if i > 2:
            print(f'{i} bottles of milk on the wall, {i} bottles of milk.', end='')
            print(f' Take one down and pass it around, {i-1} bottles of milk on the wall.')

        elif i == 2:
            print('2 bottles of milk on the wall, 2 bottles of milk.', end='')
            print(' Take one down and pass it around, 1 bottle of milk on the wall.')

        elif i == 1:
            print('1 bottle of milk on the wall, 1 bottle of milk.', end='')
            print(' Take one down and pass it around, no more bottles of milk on the wall.')

        elif i == 0:
            print('No more bottles of milk on the wall, no more bottles of milk.', end='')
            print(' Go to the store and buy some more, 99 bottles of milk on the wall.')

number_of_bottles()