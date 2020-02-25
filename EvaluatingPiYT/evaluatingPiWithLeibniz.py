'''
Evaluating Pi with Leibniz Method
Github: https://github.com/Ari24-cb24/Python-Speedcoding/edit/master/EvaluatingPiYT/evaluatingPiWithLeibniz.py
Youtube: https://youtu.be/y0hKsoaMrMg
Wikipedia: https://de.wikipedia.org/wiki/Leibniz-Reihe

Creator: Ari24
'''

# Import Time damit wir wissen, wie lange die Operation gedauert hat
import time

pi = None # Unsere Variable PI
counter = 3
current = 1
add = False

run = True
before = time.time()
while run:
    if not add:
        current -= 1 / counter
    else:
        current += 1 / counter

    add = not add # Hier wird add auf True/False gesetzt
    counter += 2

    pi = current * 4

    print(pi)

    if str(pi).startswith("3.141592"):
        run = False

after = time.time()
print(f"\nPi ist ca.: {pi}\nDies dauerte {after - before} Sekunden!")






