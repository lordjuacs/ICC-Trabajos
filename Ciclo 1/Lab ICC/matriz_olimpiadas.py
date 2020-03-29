PAISES = 5
MEDALLAS = 3
paises = ["USA", "URSS", "UK", "CHINA", "GERMANY"]
medallas = [[1022, 794, 704], [395, 319, 296], [263, 295, 289], [227, 163, 153], [219, 246, 269]]
print(" COUNTRIES         GOLD          SILVER   BRONCE")
for i in range(PAISES):
    print("%10s" % paises[i], end="  ")
    for j in range(MEDALLAS):
        print("%12.0f" % (medallas[i][j]), end=" ")
    print()
