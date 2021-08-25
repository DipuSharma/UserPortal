from django.test import TestCase

# Create your tests here.
x = [1, 2, 3, 4, 5, 6, 7]
y = [6,4]

for i in y:
    for j in x:
        if i == j:
            print(j)
