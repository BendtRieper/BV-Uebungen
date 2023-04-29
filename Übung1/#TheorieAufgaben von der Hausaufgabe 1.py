#
#TheorieAufgaben von der Hausaufgabe 1

import numpy as np 


#1. Wie kann man den vierten bis zehnten Wert einer Liste in einem Befehl setzen?
liste = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
print(liste[3:10])

print("---------------------------")
#2. Welche Möglichkeiten gibt es in einer for-Schleife über eine Liste auch den Index zu bekommen? Nenne zwei Möglichkeiten.

#1. Möglichkeit
for index, element in enumerate(liste):
    print(f"index: {index}  Element: {element}")

print("----------")
#2. Möglichkeit
animals = ["Dog", "cat", "fish", "lion"]
for i in range(len(animals)):
    print(animals.index(animals[i]))
    
print("---------------------------")

#3. Wie kann die Anzahl der Zeilen und Spalten eines zweidimensionalen NumPy-Arrays bestimmt werden?
l = np.array([[2,2], 
             [3,3],
             [4,4]])
zeilen, spalten = l.shape
print(f"Anzhal der Zeilen: {zeilen}, Anzahl der Spalten: {spalten}")

lf = np.full((3, 2), 2-4)
print(lf)


print("---------------------------")

#4. Was unterscheidet die Funktionen numpy.array und numpy.full?

#die np.array Funktion erstellt einen NumPyArray aus einer gegebenen Liste oder einem Tupel
#die np.full Funktion hingegen erstellt einen neuen NumPyArray mit einer bestimmten Form und füllt ihn mit einem 
#angegebenen Wert oder einer angegebenen Liste von Werten., welche an jeder Stelle die selben Werte hat 