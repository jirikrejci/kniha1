print('Ahoj Jirko')

retezec = 'Tak teď zase pro změnu zkouším python'

print(retezec[6] + retezec[-10])
print(5 + 5)

a = int(32) + 5
print(a)

a = str(233)
print(a + " to je výsledek")

x = "modrá"
y = 'zelená'

x = y
print(x)

a = ['jedna', 2, ' tři', 'four']

print(a)

print(a[2])
print(len(a))

a.append("pjať")
print(a)

list.append(a, "6")
print(a)

a.insert(1, "jedna a půl")
print(a)

a[1] = "jedna a třičtvrtě"
print(a)

zvirata = "kočka, žába, žirafa"

print()
print(zvirata)
print("kočka je v seznamu:", "kočka" in zvirata)
print("pes je v seznamu:", "pes" in zvirata)

# logické operátory
five = 5
two = 2
zero = 0

print(five and two)

a = "krokodýl2"

if a == "panda":
    res = "savec"
elif a == "krokodýl":
    res = "obojživelník"
elif a == "pstruh":
    res = "ryba"
else:
    res = "... fakt nevím, co to je :-)"

print(a, "je", res)

print("Ahoj z Github")

print("Ahoj z Macka")