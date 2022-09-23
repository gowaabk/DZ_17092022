""" Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных. """


""" def rle_fun(data):
    res = []
    r = 0
    for d in data:
        if d != r:
            res.append(d)
            res.append(str(1))
            print(res)
            r = d
        else:
            res[-1] = str(int(res[-1]) + 1)
            print(res)
    return res  
       """
my_str='aaabbbbcccccdddddd'                                
#print("".join(rle_fun(my_str)))
for i in my_str:
    if i == 'b':
        print (i)


#my_str2=list(my_str)
#print (my_str2)
