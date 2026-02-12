#python-pagrindai-su-pavyzdziais.md

# 1️⃣ KINTAMIEJI IR TIPAI

name = "Milda"      # string
age = 30            # integer
salary = 1700.50    # float
is_active = True    # boolean
print(type(name))
print(type(age))

# 2️⃣ MATEMATINIAI VEIKSMAI

a = 10
b = 3

print(a + b)  # sudėtis
print(a - b)  # atimtis
print(a * b)  # daugyba
print(a / b)  # dalyba
print(a % b)  # liekana

# 3️⃣ SĄLYGOS (IF / ELSE)
age = 20

if age >= 18:
    print("Suaugęs")
else:
    print("Nepilnametis")

score = 85

if score >= 90:
    print("A")
elif score >= 80:
    print("B")
else:
    print("C")

# 4️⃣ CIKLAI

    #For ciklas
for i in range(5):
    print(i)

    #For su sąrašu
names = ["Milda", "Jonas", "Asta"]
for name in names:
    print(name)

    #While ciklas
x = 0
while x < 5:
    print(x)
    x += 1

# 5️⃣ SĄRAŠAI (LISTS)

numbers = [10, 20, 30]

numbers.append(40)
print(len(numbers))
print(numbers[0])

    # List Comprehension
squares = [x**2 for x in range(5)]
print(squares)

# 6️⃣ ŽODYNAS (DICTIONARY)
person = {
    "name": "Milda",
    "age": 30
}
print(person["name"])

# 7️⃣ FUNKCIJOS
# Paprasta funkcija
def calculate_bonus(sales):
    return sales * 0.1

print(calculate_bonus(10000))

# Su numatytąja reikšme

def greet(name="Guest"):
    print(f"Hello {name}")

#8️⃣ PRAKTINĖS UŽDUOTYS

# Užduotis 1 – Išspausdinti lyginius skaičius

numbers = range(1, 11)
for n in numbers:
    if n % 2 == 0:
        print(n)

# Užduotis 2 – Rasti kainų vidurkį
prices = [100, 200, 300, 400]

avg = sum(prices) / len(prices)
print(avg)

# Užduotis 3 – 10% bonus funkcija

def bonus(sales):
    return sales * 0.10

print(bonus(5000))




