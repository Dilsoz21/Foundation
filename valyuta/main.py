#1-Method
while True:
    print("Agar dollardan -> so'mga o'tish uchun 1 ni bosing!")
    print("Agar so'mdan -> dollarga o'tish uchun 2 ni bosing!")
    tanlov = input("Son: ")

    if tanlov == "1":
        print("So'm kursini aniqlash!")
        dollar = int(input("Dollar: "))
        print(f"So'm: {dollar * 12450}")

    elif tanlov == "2":
        print("Dollar kursini aniqlash!")
        som = int(input("So'm: "))
        print(f"Dollar: {som // 12450}")

    else:
        print("Noto'g'ri tanlov, iltimos, qayta urinib ko'ring!")
    break




#2-Method
from_convert = float(input("Welcome\n1)USD\n2)SUM\n3)EUR\nChoose: "))
to_convert = float(input("Convert to:\n1)USD\n2)SUM\n3)EUR\nChoose: "))
amount = float(input("Enter the amount: "))


usd = 12.700
eur = 29.000



if from_convert == 1 and to_convert == 2:
    # USD to SUM
    print(f"{amount * usd:.2f} SUM")
elif from_convert == 1 and to_convert == 3:
    # USD to EUR
    print(f"{(amount * usd) / eur:.2f} EUR")
elif from_convert == 2 and to_convert == 1:
    # SUM to USD
    print(f"{amount / usd:.2f} USD")
elif from_convert == 2 and to_convert == 3:
    # SUM to EUR
    print(f"{amount / eur:.2f} EUR")
elif from_convert == 3 and to_convert == 1:
    # EUR to USD
    print(f"{(amount * eur) / usd:.2f} USD")
elif from_convert == 3 and to_convert == 2:
    # EUR to SUM
    print(f"{amount * eur:.2f} SUM")
else:
    print("You chose the wrong type!")