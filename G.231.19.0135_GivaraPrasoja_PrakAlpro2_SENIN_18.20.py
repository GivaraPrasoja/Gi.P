Python 3.8.2 (tags/v3.8.2:7b3ab59, Feb 25 2020, 22:45:29) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a = 12
>>> print (a)
12
>>> b = "Saya"
>>> print (b)
Saya
>>> c = (4j)
>>> print (c)
4j
>>> a,b,c = c,b,a
>>> print (c)
12
>>> print (b)
Saya
>>> print (a)
4j
>>> print (c,b,a)
12 Saya 4j
>>> print (a,b,c)
4j Saya 12
>>> 
>>> 
>>> x = 23
>>> y = 10
>>> print (x)
23
>>> print (y)
10
>>> x,y = y,x
>>> print (x)
10
>>> print (y)
23
>>> print (x,y)
10 23
>>> print (y,x)
23 10
>>> 