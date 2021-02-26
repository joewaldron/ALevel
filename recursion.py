def printnumbers(x):
    if x > 1:
        printnumbers(x-1)
    print(x)

printnumbers(100)

def factorial(n):
    if n == 1:
        return n
    else:
        return n * factorial(n-1)

print(factorial(5))

def fibbi(n):
    if n < 3:
        return 1
    else:
        return fibbi(n-1) + fibbi(n-2)

def inefficientprint(n):
    if n > 0:
        inefficientprint(n-1)
        print(fibbi(n))

inefficientprint(10)

def reverse(s):
    if len(s) == 1:
        return s
    return reverse(s[1:]) + s[0]

print(reverse("hello"))










