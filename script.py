'''
Выводит место исходя из количества баллов, если одинаковое кол-во баллов, то одинаковые места. by Ruzill
'''
a = [
'141,76',
'134,44',
'130',
'125,61',
'95',
'61,39',
'57,22',
'45',
'39,45',
'37,22',
'36,66', 
'36,17',
'33,42',
'33,34',
'32,34',
'29,67',
'29,45',
'28,88',
'28,16',
'28,16',
'26,66',
'23,33',
'20',
'20',
'20',
'18,33',
'17,23',
'13',
'12,22',
'6,33',
'1,67',
'0',
'0',
'0',
'0',
'0',
'0',
'0',
'0'
]

p=1
j=''
for i in a:
    print(p)
    if i == j:
        j = i
        continue
    j=i
    p+=1
# для правильного вывода. Со второго элемента вычитать 1, починить последнее место