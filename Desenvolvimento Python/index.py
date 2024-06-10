Python 3.12.2 (tags/v3.12.2:6abddd9, Feb  6 2024, 21:26:36) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> print("hello" + "world")
helloworld
>>> name = "mateus"
>>> idade = 18
>>> peso = 78.6
>>> print(name+idade+peso)
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    print(name+idade+peso)
TypeError: can only concatenate str (not "int") to str
>>> name = "mateus"
>>> idade = "18"
>>> peso = "78.6"
>>> print(name+idade+peso)
mateus1878.6
>>> name = "mateus"
>>> year = 18
>>> peso = 78.6
>>> print(name, year, peso)
mateus 18 78.6
>>> print("olá" + 5)
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    print("olá" + 5)
TypeError: can only concatenate str (not "int") to str
