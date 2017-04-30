def C_K(c):
    k = c + 273
    return(k)
def C_F(c):
    f = 1.8 * c + 32
    return(f)
def K_F(c):
   f = (((c - 273)*9)/5)+32
   return(f)
def K_C(c):
    x = c - 273
    return(x)
def F_K(c):
    k = (((c - 32)*5)/9)+273
    return(k)
def F_C(c):
    x = (c-32)/1,8
    return(x)

usuario_choice = int(input("Escolha qual escala deseja converter \n 1 - Celsius para Kelvin \n 2 - Celsius para Fahrenheit \n 3 - Kelvin para Fahrenheit \n 4 - Kelvin para Celsius\n 5 - Fahrenheit para Kelvin \n 6 - Fahrenheit para Celsius\n"))
while usuario_choice <= 6:
    c = float(input("Valor a ser convertido: "))
    if usuario_choice == 1:
        k = C_K(c)
        print(k, "K\n")
    elif usuario_choice == 2:
        f = C_F(c)
        print(f, "°F\n")
    elif usuario_choice == 3:
        f = K_F(c)
        print(f, "°F\n")
    elif usuario_choice == 4:
        c = K_C(c)
        print(c, "°C\n")
    elif usuario_choice == 5:
        k = F_K(c)
        print(k, "°K\n")
    elif usuario_choice == 6:
        c = F_C(c)
        print(c, "°C\n")
    usuario_choice = int(input("Escolha qual escala deseja converter \n 1 - Celsius para Kelvin \n 2 - Celsius para Fahrenheit \n 3 - Kelvin para Fahrenheit \n 4 - Kelvin para Celsius\n 5 - Fahrenheit para Kelvin \n 6 - Fahrenheit para Celsius\n"))
        
        
