import random

# STATEMENTS
"""
The if statement evaluates a condition (an expression that results in True or False).
If the condition is true, the code block inside the if statement is executed.
If the condition is false, the code block is skipped.
"""

a = 33
b = 200
if b > a:
    print("b is greater than a")

# INDENTATION
number = 15
if number > 0:
    print("The number is positive")

# MULTIPLE STATEMENTS IN IF BLOCK
age = 20
if age >= 18:
  print("You are an adult,", end=" ")
  print("you can vote now!")
  print("You have full legal rights!")

# VARIABLE CONDITIONS
is_logged_in = True
if is_logged_in:
   print("Welcome back!")

# ELIF STATEMENT 
c = 33
d = 33
if d > c:
   print("d is greater than c")
elif c == d:
   print("c and d are equal")

#  MULTIPLE ELIF STATEMENTS
score = 75

if score >= 90:
   print("Grade: A")
elif score >= 80:
   print("Grade: B")
elif score >= 70:
   print("Grade: C")
elif score >= 60:
   print("Grade: D")

# ELSE STATEMENT
e = 200
f = 33
if f > e:
  print("f is greater than e")
elif e == f:
  print("e and f are equal")
else:
  print("e is greater than f")

# WITHOUT ELIF
g = 200
h = 33
if h > g:
  print("h is greater than g")
else:
  print("h is not greater than g")

number = 7

if number % 2 == 0:
  print("The number is even")
else:
  print("The number is odd")

# COMPLETE IF-ELIF-ELSE CHAIN
temperature = 22

if temperature > 30:
  print("It's hot outside!")
elif temperature > 20:
  print("It's warm outside")
elif temperature > 10:
  print("It's cool outside")
else:
  print("It's cold outside!")

# ELSE AS FALLBACK
username = "Monreal"

if len(username) > 0:
  print(f"Welcome, {username}!")
else:
  print("Error: Username cannot be empty")

# SHORTHAND IF
i = 5
j = 2
if i > j:
  print("i is greater than j")

# SHORTHAND IF ELSE
ai = 5
aj = 2
print("AI") if ai > aj else print("AJ")

# MULTIPLE CONDITIONS ON ONE LINE
k = 330
l = 330 
print("K") if k > l else print("Equal Numbers") if k == l else print("L")

m = 15
n = 20
max_value = m if m > n else n
print("Maximum value:", max_value)

username = ""
display_name = username if username else "Guest"
print("Welcome", display_name)

# LOGICAL OPERATORS
o = 200
p = 33
q = 500

if o > p and q > o:
  print("Both conditions are True")

# OR OPERATOR
if o > p or o > q:
  print("At least one of the conditions is True")

# NOT OPERATOR
r = 33
s = 200

if not r > s:
  print("r is not greater than s")

# MULTIPLE OPERATORS
age = 25
is_student =  False
has_discount_code = True

if (age < 18 or age > 65) and not is_student or has_discount_code:
  print("Discount applies!")

# USING PARENTHESES FOR CLARITY
temperature = 25
isRaining =  False
isWeekend = True

if (temperature > 20 and not isRaining) or isWeekend:
  print("Great day for outdoor activities")

username = "Tobias"
password = "secret123"
is_verified = True

if username and password and is_verified:
  print("Login successful")
else:
  print("Login failed")

# NESTED IF
t = random.randrange(0, 30)

if t > 10:
  print(t, "is above 10,", end="")
  if t > 20:
    print("and also above 20!")
  elif t == 20:
    print("and also equal to 20!")
  else:
    print("but is below 20")
elif t == 10:
  print(t,"is equal to 10")
else:
  print(t,"is below 10")

# NESTED IF VS LOGICAL OPERATORS
temp = 25
isSunny = True

if temp > 20:
  if isSunny:
    print("Perfect beach weather!")
# OR
if temp > 20 and isSunny:
  print("Perfect beach weather!")

username = "Emil"
password = "python123"
is_active = True

if username:
  if password:
    if is_active:
      print("Login successful")
    else:
      print("Account is not active")
  else:
    print("Password required")
else:
  print("Username required")


score = 92
extra_credit = 5

if score >= 90:
  if extra_credit > 0:
    print("A+ grade")
  else:
    print("A grade")
elif score >= 80:
  print("B grade")
else:
  print("C grade or below")

# PASS STATEMENT
u = 33
v = 200

if v > u:
  pass

age = 20

if age < 18:
  pass # TODO: Add underage logic later
else:
  print("Access granted")

score = 85

if score > 90:
  pass # This is excellent
print("Score processed")

# MULTIPLE CONDITIONS
value = 50

if value < 0:
  print("Negative value")
elif value == 0:
  pass # Zero case - no action needed
else:
  print("Positive value")


def calculate_discount(price):
  pass # TODO: Implement discount logic

# Function exists but doesn't do anything yet


age = random.randrange(7, 25)

if age < 13:
  print("Child")
elif age < 18:
  print("Teenager")
else:
  print("Adult")

# MATCH STATEMENT 
day = random.randrange(1, 7)
month = random.randrange(1, 12)
match day:
  case 1:
    print("Monday")
  case 2:
    print("Tuesday")
  case 3:
    print("Wednesday")
  case 4:
    print("Thursday")
  case 5:
    print("Friday")
  case 6:
    print("Saturday")
  case 7:
    print("Sunday")

match month:
  case 1:
    print("January")
  case 2:
    print("February")
  case 3:
    print("March")
  case 4:
    print("April")
  case 5:
    print("May")
  case 6:
    print("June")
  case 7:
    print("July")
  case 8:
    print("August")
  case 9:
    print("September")
  case 10:
    print("October")
  case 11:
    print("November")
  case 12:
    print("December")

day = 3
match day:
  case 3:
    print("Wednesday")
  case _:
    print("Other day")