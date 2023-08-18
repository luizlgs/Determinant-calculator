def det(pmatrix):
    if len(pmatrix) > 2:
        result = 0
        matrixwitoutlastline = []
        for e in range(0, len(pmatrix)-1):
            matrixwitoutlastline.append(pmatrix[e])
        newdet1 = []
        columnnewdet1 = []
        for c in range(0, len(matrixwitoutlastline[0])):
            for d in range(0, len(matrixwitoutlastline)):
                columnnewdet1.append(matrixwitoutlastline[d][c])
            newdet1.append(columnnewdet1)
            columnnewdet1 = []
        newdet = []

        for c in range (0, len(pmatrix)):
            for d in range(0, len(newdet1)):
                if d == c:
                    continue
                else:
                    newdet.append(newdet1[d])
           
            result += ((-1)**(len(pmatrix) + c+1)) * pmatrix[len(pmatrix)-1][c] * det(newdet)
            newdet = []
        return result
    else:
        return (pmatrix[0][0] * pmatrix[1][1]) - (pmatrix[0][1] * pmatrix[1][0])


tam = int(input("Dimensão da matriz: "))
matrix = []
column = []
for c in range (tam):
    for d in range (tam):
        column.append(int(input("")))
    matrix.append(column)
    column = []
    
print(f"Determinante = {det(matrix)}")
