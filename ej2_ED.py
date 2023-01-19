def ej2(a, b):
    a = [1, 2, 3]
    b = [-1, 0, 2]
    producto = 0
    for i in range(len(a)):
        producto = a[i-1]*b[i-1]
    print("El producto de vectores" + str(a) + "y" + str(b) + "es" + str(producto))
ej2([1, 2, 3], [-1, 0, 2])



