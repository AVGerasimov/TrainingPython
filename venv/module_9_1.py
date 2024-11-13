__author__ = 'Андрей Герасимов'

def apply_all_func(int_list, *functions):
# если в переданном списке есть значения, не принадлежащие целым числам или вещественным, то им присваивается значение 0
    step = 0
    for j in int_list:
        if isinstance(j, int)== False and isinstance(j, float) == False:
            int_list[step] = 0
        step+=1


    result = dict()
    for i in functions:
            result[i.__name__] = i(int_list)
    return result



print(apply_all_func([6, 20, 15, 9], max, min))
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))

