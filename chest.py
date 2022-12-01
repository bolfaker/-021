kol = 0
vsego = 10
 
otv = input("Производная от sin(x)")
if otv == "cos(x)" or "cosx":
    print("Верно")
    kol = kol + 1
else:
    print("Не верно")
     
otv = input("Производная от cos(x)")
if otv.lower() == "-sin(x)" or "-sinx":
    print("Верно")
    kol = kol + 1
else:
    print("Не верно")
 
otv = input("Производная от ln(x)")
if otv.lower() == "1/x" or "1:x":
    print("Верно")
    kol = kol + 1
else:
    print("Не верно")

otv = input("Производная от x")
if otv.lower() == "1" or " 1" or "  1":
    print("Верно")
    kol = kol + 1
else:
    print("Не верно")

otv = input("Производная от cos(2x)")
if otv.lower() == "-2sin(2x)" or "-2*sin(2x)" or "-2sin2x" or "-2*sin2x":
    print("Верно")
    kol = kol + 1
else:
    print("Не верно")

otv = input("Производная от a^x")
if otv.lower() == "a^x*ln(a)" or "a^xln(a)":
    print("Верно")
    kol = kol + 1
else:
    print("Не верно")

otv = input("Производная x^n")
if otv.lower() == "nx^(n-1)" or "n*x^(n-1)" or "nx^n-1" or "n*x^n-1":
    print("Верно")
    kol = kol + 1
else:
    print("Не верно")

otv = input("Производная tg(x)")
if otv.lower() == "1/cos(x)^2" or "1/cos^2(x)":
    print("Верно")
    kol = kol + 1
else:
    print("Не верно")

otv = input("Производная от ctg(x)")
if otv.lower() == "-1/sin(x)^2" or "-1/sin^2(x)":
    print("Верно")
    kol = kol + 1
else:
    print("Не верно")

otv = input("Производная от sin(3x)")
if otv.lower() == "3cos(3x)" or "3*cos(3x)" or "3cos3x" or "3*cos3x":
    print("Верно")
    kol = kol + 1
else:
        print("Не верно") 
 
print(kol," верных ответов из ", vsego)
