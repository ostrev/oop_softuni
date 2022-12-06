# test animal
import unittest

from project.animal import Animal
from project.dog import Dog


d = Dog()
res = d.bark()
print(res)
print(d.__class__.__bases__[0].__name__)