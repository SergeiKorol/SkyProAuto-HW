def month_to_season(n):
    if n < 3:
        print("Зима")
    else:
        if n < 6:
            print("Весна")
        else:
            if n < 9:
                print("Лето")
            else:
                if n < 12:
                    print("Осень")
                else:
                    print("Зима")
                    
                

n = input("Введите число от 1 до 12 ")
n = int(n)
month_to_season(n)