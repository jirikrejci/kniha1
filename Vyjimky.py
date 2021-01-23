#test výjimek

while True:
    s = input("Zadejte celé číslo, (konec programu: Q)")
    if s == "Q":
        break
    try:
        i = int(s)
        print("zadáno celé číslo:", i)
    except ValueError as err:
        print(err)

