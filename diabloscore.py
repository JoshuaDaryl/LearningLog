games = [
  {"title": "Diablo 1", "score": "0", "endgame": "0"},
  {"title": "Diablo 2", "score": "0", "endgame": "0"},
  {"title": "Diablo 3", "score": "0", "endgame": "0"},
  {"title": "Diablo 4", "score": "0", "endgame": "0"}

]

print("Hi there, here is your input generator for Diablo scores")


cont = input("Do you want to continue y/n?:")


if cont == "y":
             print("Awesome, lets start...")
             
else:
    quit()

print("So im going to be asking you for some Diablo reviews, here are the current results")

#print current score function--------------------------------------------------------------------

def updated_score():
    for game in games:
        game_num = game["title"]
        score = game["score"]
        endgame = game["endgame"]
        message = f"For {game_num}, current score is {score}, and the endgame is rated {endgame}"
        print(message)
#-----------------------------------------------------------------------------------------------

updated_score()

#Below is score adjustment function--------------------------------------------------------------

def user_score (game):
    game = int(game)
    if game in range(1,5):
        
        
        new_score = input(f"Please enter a new score for Diablo {game}:")
        new_endgame = input(f"Please enter a new endgame score for Diablo {game}:")
        if game == 1:
                games[0]["score"] = new_score
                games[0]["endgame"] = new_endgame
        elif game == 2:
                games[1]["score"] = new_score
                games[1]["endgame"] = new_endgame
        elif game == 3:
                games[2]["score"] = new_score
                games[2]["endgame"] = new_endgame
        elif game == 4:
                games[3]["score"] = new_score
                games[3]["endgame"] = new_endgame
    

    

    
    else:
        print("Sorry, that isn't an option")
#------------------------------------------------------------------------------------------------

for i in range(1,100):
    
    cont=input("Quit or update review scores? ('y' to continue & 'n' to finish)")

    if cont == "y":
        which = input("What game do you want to choose? 1, 2, 3, 4?")
        user_score(which)
    else:
        updated_score()
        break


#print(games)


