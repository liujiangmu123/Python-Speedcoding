'''
Project: SimpleMathKi
Author: Ari24
Youtube: https://youtu.be/YgYZo_v-fDw
GitHub: https://github.com/Ari24-cb24/Python-Speedcoding/edit/master/simpleMathKi.py
'''

from sklearn.linear_model import LinearRegression

# Hier erstellen wir unsere kleine KI Klasse, mit der wir dann KI's erzeugen können

class Prediction_NN:
    def __init__(self, x, y):
        self.x = x
        self.y = y

        self.model = LinearRegression()
        self.__fit()

    def predict(self, prediction):
        return self.model.predict(prediction)

    def __fit(self):
        self.model.fit(self.x, self.y)

# Simple Multiplikation
# In das Array x kommt die Rechnung
# In das Array y kommen die Ergebnisse

# Wir haben nur 5 Trainingsdaten, unser Ergebnis wird also nicht so genau sein. 

x = [[7, 8], [4, 4], [5, 5], [1, 4], [10, 1], [3, 3], [7, 1], [3, 7], [2, 7], [4, 6], [10, 3]]
y = [56, 16, 25, 4, 10, 9, 7, 28, 21, 24, 30]

# Hier wird unsere Ki erstellt
# Unsere Trainingsdaten werden mitgeliefert

model = Prediction_NN(x, y)

# Nun wollen wir eine Rechnung erstellen, auf die unsere KI eine Antwort geben soll
# Hier werden wir einen Benutzerinput benutzen

first_number = input("Erste Zahl: ")
second_number = input("Zweite Zahl: ")

# Hier fragen wir noch ab, ob unser Benutzer denn Zahlen eingegeben hat

if first_number.isnumeric():
    if second_number.isnumeric():
        # Wichtig ist, dass die Zahlen zu einem Integer umgewandelt werden. Wir haben unsere KI ja nur auf Integer trainiert, nicht auf Strings
        first_number = int(first_number)
        second_number = int(second_number)
        
        calculation = [[first_number, second_number]]

# Die Ki soll jetzt uns sagen, was sie mit dieser Rechnung anfängt

print(model.predict(calculation)[0])
print("\n")







