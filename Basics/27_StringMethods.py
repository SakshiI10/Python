score='19.67'
score2='20'
# 1) isdecimal()
print(score.isdecimal())
print(score2.isdecimal())

# 2) isdigit()
print(score.isdigit())
print(score2.isdigit())

# 3) isnumeric()
print("1234".isnumeric())

str="largest is larger than larger"
# 4) count()
print(str.count("lar"))
print(str.count('lar',10))
print(str.count('lar', 10, 20))

# 5) startswith()

c="INDIAN"
# 6) endswith()
print(c.endswith('N'))
print(c.endswith('n'))

a="27Feb2024"
b="27 Feb 2024"
# 7) isalnum()
print(a.isalnum())
print(b.isalnum())
print("!@#$%".isalnum())

month='February'
# 8) isaplha()
print(month.isalpha())

# 9) isupper()
print('SAKSHI'.isupper())

# 10) islower()
print('sakshi'.islower())

# 11) upper()


# 12) lower()
print("Sakshi".lower())

I="python in OOP language"
# 13) capitalize()
print(I.capitalize())

# 14) casefold()
print(I.casefold())

t="Good Day"
t2="Good day"
t3="good day"
# 15) istitle()
print(t.istitle())
print(t2.istitle())
print(t3.istitle())

# 16) title()

# 17) center()
print(I.center(24,'-'))

# 18) isprintable()
print("".isprintable())
print("Good Day".isprintable())
print("Good \t Day".isprintable())

s="\n"
s2="\n  \r  \t"
s3="a\nb"
# 19) isspace()
print(s.isspace())
print(s2.isspace())
print(s3.isspace())

a='aa\tbb\tcc'
# 20) expandtabs()
print(a.expandtabs())

# 21) isidentifier()
print("rollno".isidentifier())
print("roll no".isidentifier())