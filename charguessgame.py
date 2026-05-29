import random
def guessgame():
    attempt=0
    char=random.choice("ABCDEFGHIKLMNOPQRSTUVWXYZ")
    print("I choosed a random character")

    while True:
        try:
            Guess=input("Enter a Characeter A-Z:")
            attempt=attempt+1
            if attempt==4:
                print("Attempt over")
                break
            elif Guess>char:
                print("Too High")
            elif Guess<char:
                print("Too Low")
            else:
                print(f"You are right in the Attempt {attempt} and the Value is {char}")
                attempt=0
        except ValueError:
            print("Enter a Valid Character")
guessgame()