multitable = [[0] * 11 for i in range(11)]

for i in range(1, 11):
    for j in range(1, 11):
          multitable[i][j] = i * j

for i in range(1, 11):
     for j in range(1, 11):
          print(multitable[i][j], end=', ')
     print()