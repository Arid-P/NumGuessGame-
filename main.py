
from score_handler import ScoreFileHandler

def change_difficulty (difficulty: int) -> int:
    diff_check = input("Do you want to change the difficulty (type 1 for yes) :")
    
    if(diff_check == "1") :
      return input_difficulty()
    
    return difficulty

def try_again(scorefile: ScoreFileHandler, scores) -> bool:
    play_again = input("Do want to try again (type 1 for yes) : ")
  
    if(play_again != "1") :
        scorefile.print_score(scores)
        print("Thanks for playing")
        
        return False
    
    return True

def input_difficulty () -> int :
    """
    Prompts the user to input whatever difficulty they want.
    Theb acckrding to the chossen difficulty, its int is returned.
    EASY: 1
    MEDIUM: 2
    HARD: 3
    EXTREME: 4
    """
    
    while True : 
      diff = input("Enter difficulty (easy, mid, hard, ex) : ")
      
      if (diff == "easy") :
        return 1
      elif (diff == "mid") :
        return 2
      elif (diff == "hard") :
        return 3
      elif (diff == "ex") :
        return 4
      else :
      print("Invalid input")

def starting_instructions() -> None:
    print("INSTRUCTIONS:")
    print("In this program a you need to guess a randomly generated number and minimun tries are 5")
    print()
    
    print("There are 4 difficulties: easy, medium (mid), hard, exterme (ex)")
    print()
    
    print("EASY mode rules :")
    print("In it you have to guess a munber b/w 1 to 100")
    print("If the guessed number it more or less than the selected number by more than 20 then the screen will show too high or too low respectively")
    print("If the guessed number it more or less than the selected number by 20 or less then the screen will show high or low respectively")
    print("And you get maximum of 20 tries")
    print()
    
    print("MEDIUM mode rules :")
    print("In it you have to guess a munber b/w 1 to 150")
    print("If the guessed number it more or less than the selected number by more than 25 then the screen will show too high or too low respectively")
    print("If the guessed number it more or less than the selected number by 25 or less then the screen will show high or low respectively")
    print("And you get maximum of 15 tries")
    print()
    
    print("HARD mode rules :")
    print("In it you have to guess a munber b/w 1 to 200")
    print("If the guessed number it more or less than the selected number by more than 35 then the screen will show too high or too low respectively")
    print("If the guessed number it more or less than the selected number by 35 or less then the screen will show high or low respectively")
    print("And you get maximum of 10 tries")
    print()
    
    print("EXTREME mode rules :")
    print("In it you have to guess a munber b/w 1 to 300")
    print("If the guessed number it more or less than the selected number by more than 45 then the screen will show too high or too low respectively")
    print("If the guessed number it more or less than the selected number by 45 or less then the screen will show high or low respectively")
    print("And you get 5 tries")
    print()

def main():
    """This control the flow of the program along with the variables: score, difficulty"""
    starting_instructions()
    scorefile = ScoreFileHandler()
    scorefile.save_start_time()
    
    scores: list[int] = []
    
    while True: 
        difficulty = input_difficulty()
        
        if (difficulty  == 1) :
            set_gamemode_easy(scores)
        elif (difficulty  == 2) :
            set_gamemode_mid(scores)
        elif (difficulty  == 3) :
            set_gamemode_hard(scores)
        elif (difficulty  == 4) :
            set_gamemode_extreme(scores)
        
        scorefile.save_score_in_file(len(scores), scores[-1])
        
        if try_again(scorefile, scores):
            difficulty = change_difficulty()
    

if __name__ == '__main__':
    main()