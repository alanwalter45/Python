a = 'i'
b = 'i'
print(a is b)

a = 'i n d i a'
b = 'i n d i a'
print(a is b)

a,b = 5000,5000
print(a is b)
print(id(a),id(b))

a = [999,50]
b = [999,50]
print(a is b)