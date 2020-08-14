numero = 100
letra = "A"

print(f"{numero}{letra}")
print("{1}{0}".format(numero, letra))

# %s - String (or any object with a string representation, like numbers)
# %d - Integers
# %f - Floating point numbers
# %.<number of digits>f - Floating point numbers with a fixed amount of digits to the right of the dot.
# %x/%X - Integers in hex representation (lowercase/uppercase)

print("%s%s" % (numero, letra))
