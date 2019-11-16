a = int(input('The first group has ... students: '))
b = int(input('The second group has ... students: '))
c = int(input('The third group has ... students: '))

def desks(a, b, c):
    print('\nThere are ' + str(-(-a // 2)) + ' desks in the first group.')
    print('\nThere are ' + str(-(-b // 2)) + ' desks in the second group.')
    print('\nThere are ' + str(-(-c // 2)) + ' desks in the third group.')
    print('\nThere are ' + str((-(-a // 2)) + (-(-b // 2)) + (-(-c // 2))) + ' desks in all classes.')

desks(a, b, c)

