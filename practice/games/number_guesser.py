import random

class NonPositiveValueError(ValueError):
    pass

def main():
    number = round(random.random()*100)

    while True:
        guess = get_input()
        if guess < number:
            print("Too low")
        elif guess > number:
            print("Too large")
        else:
            print("Bingo!")
            break

def get_input():
    while True:
        ip = input("Guess the number: ")
        try:
            guess = int(ip)

            if guess < 0:
                raise NonPositiveValueError
            
            if guess > 100:
                raise ValueError
            
            return guess
        
        except NonPositiveValueError:
            print("Enter a positive value")
        except ValueError:
            print("enter an INTEGER between 0 to 100")


if __name__ == "__main__":
    main()