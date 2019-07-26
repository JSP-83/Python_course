# Conditions

# if
a = 5
if a > 0:
    print("a est grand")
elif a < 0:
    print("negative")
else:
    print("nul")

# tests : <, >, <=, >=, ==, !=, and, or , not(is not for references test)

# while
b = 2
while b < 10:
    print("valeur de b :",b)
    b += 1
    if b == 7:
        print("break at 7")
        break

# for
string = "Hello World"
c = 0
for letter in string:
    if letter in "AEIOUYaeiouy":
        print(letter)
        print("value of c", c)
        continue  # next letter
    c += 1




