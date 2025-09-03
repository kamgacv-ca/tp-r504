#print("Hello, World!")

import fonctions as f

while True:
        a = int(input("Entrez la base (entier) : "))
        b = int(input("Entrez l'exposant (entier) : "))
        res = f.puissance(a, b)
        print(f"{a} élevé à la puissance {b} = {res}")





