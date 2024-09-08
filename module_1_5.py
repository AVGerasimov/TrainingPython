__author__ = 'Андрей'

immutable_var=tuple([12, "High_load", True, 23.467])
print(immutable_var)
#immutable_var[0]=2
#print(immutable_var)
#'tuple' object does not support item assignment
mutable_list = tuple([[12,34,56], ["High_load",12], True, 23.467])
print(mutable_list)
mutable_list[0][1] = 333
mutable_list[0][2] = 444
mutable_list[1][0] = "Low load"
print(mutable_list)