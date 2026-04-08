import datetime

from config import SCORE_FILE_PATH
#global variables
score: list[int] = []
difficulty: int = 0 #difficulty like easy, etc with its level number


class ScoreFileHandler ():
    def save_start_time (self) -> None :
      now = datetime.datetime.now()
      formatted_time = now.strftime("%d-%m-%Y %H:%M")
      
      with open(SCORE_FILE_PATH, "a") as scorefile :
        scorefile.write(f"\n\n{formatted_time} \n")
    
    def save_score_in_file (round_: int, score: int) -> None :
        with open(SCORE_FILE_PATH, "a") as scorefile :
            scorefile.write(f"Round {round_} : {score} \n")
    
    def print_score (self, scores: list[int]) -> None :
        totalaccuray = 0
      
        print("Your score of accuray of each round is :")
        for i in range(len(scores)) :
            print(f"Round {i+1} : {scores[i]}") #prints round with its accuray
            totalaccuray += scores[i]
      
        overallaccuray = round(totalaccuray/len(scores), 2)
        self.end_save_on_file(overallaccuray)
      
        print(f"Overall accuray : {overallaccuray}\n")
    
    def end_save_on_file (overallaccuray) -> None :
        with open(SCORE_FILE_PATH, "a") as scorefile :
            scorefile.write(f"Overall accuray : {overallaccuray} \n") 