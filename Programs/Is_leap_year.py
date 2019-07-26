# Is input year leap ?

# input
s_year = input("Give a year : ")
print("you chose",s_year)

# conversion
i_year = int(s_year)

# leap ?
rest = i_year % 4
if rest == 0:
    print("leap year")
else:
    print("no leap year")


