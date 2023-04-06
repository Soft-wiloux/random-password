import random #In cmd: pip install random

while True: 
    print("------------")
    print("")
    print("    Use: 1    ")
    print("")
    print("------------")
    
    user = input("Generate a random password: ")
    
    if user == "1":
        print("")
        print(f"Number generate: {random.random()}")
    
    