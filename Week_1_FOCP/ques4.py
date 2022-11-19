no_of_inning=float(input("Enter Number of Innings: "))
no_of_not_out_inning=float(input("Enter Number of not out Innings: "))
no_of_success_inning=no_of_inning-no_of_not_out_inning
runs_scored=float(input("Enter Total Runs Scored: "))
batting_average=runs_scored/no_of_success_inning
print("Batting Average", batting_average)