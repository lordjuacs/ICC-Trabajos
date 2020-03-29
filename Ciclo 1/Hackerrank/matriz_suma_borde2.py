MA=[]
#leer filas y columnas
(n, m) = input().split(" ")
n = int(n)
m = int(m)
#leer linea por linea y poblar matriz
for i in range(n):
  linea = input().split(" ")
  linea = [int(x) for x in linea]
  MA.append(linea)

#imprimir bordes y suma
suma=0
for i in range(n):
  for j in range(m):
    if i==n//2 and j==m//2:
      print(MA[i][j], end =" ")
      suma += MA[i][j]
    elif not(i>0 and j>0 and i<n-1 and j<n-1):
      print(MA[i][j], end =" ")
      suma += MA[i][j]
    else:
      print(" ", end =" ")
  print()

print(suma)