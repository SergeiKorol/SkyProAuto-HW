def is_year_leap(a):
    if (a % 4) > 0:
        print('Год ', a, ': ', 'False')
    else: print('Год ', a, ': ', 'True')

a = input('Введите год=')
a = int(a)
is_year_leap(a)
