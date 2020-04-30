"""
PAVARD Hugo
Encodeur/décodeur base 64
Avril 2020 
"""

# Permettre à l'utilisateur d'entrer une chaîne
# de caractères après avoir lancé le programme
# en boucle infinie.
def main():
	# Les étapes de l'algorithme Base 64
	while True:
		pass
		user_input = input()

		# 1. Conversion de la chaîne en liste
		elements_list = list(user_input)
		print(elements_list) 

		# 2. Conversion de chaque élément de la liste en entier
		int_list = []
		for ele in elements_list:
			int_list.extend(ord(num) for num in ele)
		print(int_list)

		# 3. Conversion de chaque entier de la liste en 8 bits
		binary_list = list(map(lambda x: format(x,'08b'),int_list))
		print(binary_list)

		# 4. Conversion de la liste en chaîne
		binary_string = ''.join(binary_list)
		print(binary_string)

		# 5. Conversion de la chaîne en une liste d'éléments de longueur six cadrés à droite
		new_int_list = [int(binary_string[i:i+6], 2) for i in range(0, len(binary_string), 6)] 
		new_binary_list = list(map(lambda x: format(x,'06b'),new_int_list))
		print(new_binary_list)

		# 6. Conversion des éléments en entier
		print(new_int_list)

		# 7. Conversion des entiers dans leur représentation dans la base 64

		"""
		new_elements_list = []
		for ele2 in new_int_list:
			new_elements_list.extend(corresp = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4, "F": 5, "G": 6, "H": 7, 
			"I": 8, "J": 9, "K": 10, "L": 11, "M": 12, "N": 13, "O": 14, "P": 15,
			"Q": 16, "R": 17, "S": 18, "T": 19, "U": 20, "V": 21, "W": 22, "X": 23,
			"Y": 24, "Z": 25,

			"a": 26, "b": 27, "c": 28, "d": 29, "e": 30, "f": 31, "g": 32, "h": 33, 
			"i": 34, "j": 35, "k": 36, "l": 37, "m": 38, "n": 39, "o": 40, "p": 41,
			"q": 42, "r": 43, "s": 44, "t": 45, "u": 46, "v": 47, "w": 48, "x": 49,
			"y": 50, "z": 51,

			"0": 52, "1": 53, "2": 54, "3": 55, "4": 56,
			"5": 57, "6": 58, "7": 59, "8": 60, "9": 61,

			"+": 62, "/": 63})

		print(new_elements_list)

		"""







		





if __name__ == '__main__':
    main()