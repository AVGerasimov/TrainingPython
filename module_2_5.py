__author__ = 'Андрей Герасимов'

def get_matrix(n, m, value):
    if n<1 or m<1 :
        return []
    matrix = []
    for i in range(n):
        Addlist = [0]*m
        matrix.append(Addlist)
        for j in range(m):
            matrix [i] [j] = value
    return (matrix)

result1 = get_matrix(2, 2, 10)
result2 = get_matrix(3, 5, 42)
result3 = get_matrix(4, 2, 13)
print(result1)
print(result2)
print(result3)