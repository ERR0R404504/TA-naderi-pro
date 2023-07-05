from re import X
from turtle import distance


def floyd_warshall(matrix):
    n = len(matrix)
    """
    این تابع  الگوریتم فلوید وارشال را برای محاسبه کوتاه ترین مسیرها بین تمام جفت ریوس در نموداری که با یک ماتریس مجاور  نمایش داده میشود پیاده سازی میکند.
    """
    distance = [[matrix[i][j] for j in range(n)] for i in range(n)]

    #محاسبه کوتاه ترین راه با استفاده از با الگوریتک وارشال
    for k in range(n):
        for i in range(n):
            for j in range(n):
                distance[i][j] = distance[i][j] or (distance[i][k] and distance[k][j])
    return distance

#.......................................................................................................

def symmetric_closure(matrix):
    n = len(matrix)

    # محاسبه بستار متقارن ماتریکس با استفاده ار الگوریتم وارشال
    distance = floyd_warshall(matrix)
    for i in range (n):
        for j in range(n):
            if distance[i][j] or distance[j][i]:
                matrix[i][j] = 1
                matrix[j][i] = 1
    return matrix


#.......................................................................................................

def reflexive_closure(matrix):
    n = len(matrix)
    #محاسبه بستار انعکاسی با استفاده از  الگوریتم وارشال 
    distance = floyd_warshall(matrix)
    for i in range (n):
        if not distance[i][i]:
            matrix[i][i] = 1
        return matrix
    

#........................................................................................................

def transetive_closure(matrix):
    n = len(matrix)                       

#محاسبه بستار متعدی با استفاده از الگوریتم وارشال



    distance = floyd_warshall(matrix)
    for i in range(n):
        for j in range(n):
            if distance[i][j]:
                matrix[i][j] = 1
    return matrix



matrix = [
    [0,1,0,0],
    [1,0,1,0],
    [0,0,0,1],
    [0,0,0,0]
]

print("input matrix: ")
for row in matrix:
    print (" ".join(str(x) for x in row))


print("symmetric closure: ")
symmetric = symmetric_closure(matrix)
for row in symmetric:
    print(" ".join(str(x) for x in row))





print("reflexive closure: ")
reflexive = reflexive_closure(matrix)
for row in reflexive :
    print(" ".join(str(x)for x in row))



print("transetive closure: ")
transetive = transetive_closure(matrix)
for row in transetive :
    print(" ".join(str(x)for x in row))















