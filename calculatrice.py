#Projet de calculatrice simple
#En date du 7 octobre 2024

def addition(a,b):
    '''
    (float,float) -> (float)
    Cette fonction détermine la somme de deux nombres.
    '''
    somme = a + b #Résultat des deux nombres
    return somme

def soustraction(a,b):
    '''
    (float,float) -> (float)
    Cette fonction détermine la différence de deux nombres.
    '''
    difference = a - b
    return difference

def multiplication(a,b):
    '''
    (float,float) -> (float)
    Cette fonction détermine le produit de deux nombres.
    '''
    produit = a * b
    return produit

def division(a,b):
    '''
    (float,float) -> (float)
    Cette fonction détermine le quotient de deux nombres.
    Le deuxième nombre ne peut toutefois par être égale à zéro.
    '''
    quotient = a / b
    return quotient

def calculatrice():
    #Fonction qui fait fonctionner la calculatrice simple.
    print("Welcome to the simple calculator!",'\n')
    print("You'll be able to solve simple and basic operations.")
    print("Choose between the four following operations:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division",'\n')
    choice = input("Which operation do you want? (Between 1 to 4):   ")
     
    if choice == "1":
        print("You chose Addition!",'\n')
        a = float(input("What's your first number?   "))
        b = float(input("What's your second number?   "))
        print(addition(a,b))
    elif choice == "2":
        print("You chose Subtraction!",'\n')
        a = float(input("What's your first number?   "))
        b = float(input("What's your second number?   "))
        print(soustraction(a,b))
    elif choice == "3":
        print("You chose Multiplication!",'\n')
        a = float(input("What's your first number?   "))
        b = float(input("What's your second number?   "))
        print(multiplication(a,b))
    elif choice == "4":
        print("You chose Division!",'\n')
        a = float(input("What's your first number?"  ))
        b = float(input("What's your second number?"   ))
        if b == 0: 
            print()
            print("Error! This operation is not defined. Try again!")
            print()
            calculatrice()
        else:
            print(division(a,b))

def main():
    #Définition du système
    while True:
        calculatrice()

        play_again = input("Do you want to use the calculator again? (yes/no): " )

        if play_again != "yes":
            print("Thank you for using the Simple Caculator! See you again!")
            break

if __name__ == "__main__":
    main()
