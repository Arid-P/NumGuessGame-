from random import randint

def trys_input (upper_bound)  -> int:
    print("Enter the number tries you will need :", end=" ")
    
    while True :
        tries_str = input()
        
        if not tries_str.strip() :
            print("Enter a valid number")
            continue
        
        tries = int(tries_str) 
        if 5 <= tries <= upper_bound:     # checks if tries is in correct bound
            break
        
        print("Enter a valid number")

    return tries

def valid_int (self, ask_user="Enter a number (integer): "):
        while True:
            n = input(ask_user)
            
            try: 
                n = int(n)
                return n 
            except TypeError:
                print("Invalid literal! Integer  are numbers like 0, 1, 2, -1, -2, etc")
                ask_user = "Again enter a valid integer: "


class Gamemode ():
    def __init__ (self):
        self.guess = GuessLogic()
    
    def set_ex (self, scores) -> None : 
        tries = 5 
        n = int(randint(1,300)) #n is our generated number
        near_range = 45
        
        score = self.guess.guessing(tries, n, near_range)
        scores.append(score)
    
    def set_hard (self, scores) -> None:
        tries = trys_input(10)
        n = int(randint(1,200)) #n is our generated number
        near_range = 35
        
        score = self.guess.guessing(tries, n, near_range)
        scores.append(score)
    
    def set_mid (self, scores) -> None :
        tries = trys_input(15)
        n = int(randint(1,150)) #n is our generated number
        near_range = 25
        
        score = self.guess.guessing(tries, n, near_range)
        scores.append(score)
    
    def set_easy (self, scores) -> None :
        tries = trys_input(20)
        n = int(randint(1,100)) #n is our generated number
        near_range = 20
        
        score = self.guess.guessing(tries, n, near_range)
        scores.append(score)

class GuessLogic ():
    def calcu_accuracy (self, triestaken, tries) -> int :
        accuracy = (100 - ( ((triestaken - 1) / tries) * 100))
        return accuracy
    
    
    def guessing (self, tries: int, n: int, near_range: int) -> int :
        triestaken = 1
        
        print("\nLets start guessing then!\n")
        for i in range(tries) : 
            guessed_num = valid_int("Enter your guess: ")
            
            if(n == guessed_num) :
                print(f"You won, it took you : {triestaken} tries")
                break
            
            elif((n - guessed_num) > 0) : #if the guessed_num is smaller
                triestaken += 1
                
                if((n - guessed_num) > near_range) :
                    print("too low")
                else:
                    print("little low")
                
            else : #if guessed_num is greater
                triestaken += 1
                if((guessed_num - n) > near_range):
                    print("too high")
                else: 
                    print("little high")
            
        else :
            print(f"You lost, the number was {n}")
        
        print()
        return self.calcu_accuracy(triestaken, tries)