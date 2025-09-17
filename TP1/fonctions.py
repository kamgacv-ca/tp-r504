def puissance(a, b):
	if not type(a) is int or not type(b) is int:
		raise TypeError("Only integers are allowed")

	if a == 0 and b < 0:
		raise ValueError("0 à une puissance négative est indéfini")

	result = 1

	for i in range(abs(b)):
		result *= a

	if b < 0:
		return 1 / result
	else:
		return result

	x = "hello"
	if not type(x) is int:
		raise TypeError("Only integers are allowed")

'''

	try:
# Ici tu peux tester ta fonction avec différentes valeurs
		print(puissance(2, 3))  # Devrait afficher 8
		print(puissance(0, -1)) # Va lever ValueError
		print(puissance(2, "a"))# Va lever TypeError
	except TypeError as te:
		print(f"Type error attrapée : {te}")
	except ValueError as ve:
		print(f"Value error attrapée : {ve}")
	except Exception as e:
		print(f"Une autre erreur est survenue : {e}")
	else:
		print("Calcul effectué sans erreur.")
	finally:
		print("Fin de la gestion des exceptions.")

