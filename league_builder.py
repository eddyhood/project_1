import csv
import random

#=========================  REQUIREMENTS  ====================================#
#Make sure script doesn't execute when imported. Keep all code within __name__ == '__main__'

#Create variables and programming logic to divide the 18 players into three teams
#Sharks, Dragons and Raptors. Make sure the teams have the same number of 
#players on them, and that the experience players are divided equally across the three teams.

#Create a text file named teams.txt that includes the name of a team, 
#followed by the players on that team. List all three teams and their players.

#In the list of teams, include the team name on one line, followed by a separate 
#line for each player. Include the player's name, whether the player has experience 
#playing soccer, and the player's guardian names. Separate each bit of player information by a comma.


if __name__ == '__main__':

    #open soccer_players.csv with the ability to read and parse data. 
    #Create logic that seperates the experiences players from the new players

    sharks = []
    dragons = []
    raptors = []

    def sort_players():
    	experienced_players = []
    	new_players = []

    	with open("soccer_players.csv", newline = '') as csvfile:
    		reader = csv.DictReader(csvfile, delimiter = ',')
    		for row in reader:
    			if row['Soccer Experience'] == 'YES':
    				player_record = (row['Name'], row['Soccer Experience'], row['Guardian Name(s)'])
    				experienced_players.append(player_record) 			
    			else:
    				player_record = (row['Name'], row['Soccer Experience'], row['Guardian Name(s)'])
    				new_players.append(player_record)
    		return experienced_players, new_players

    x,y = sort_players()   

   
    
    # Evenly assign players to teams according to skillset

    def player_picker(players):
    	#take players and randomly sample and assign them to teams
    	equal_division = len(players) // 3

    	shark_players = random.sample(players, equal_division)
    	sharks.extend(shark_players)

    	dragon_players = random.sample(players, equal_division)
    	dragons.extend(dragon_players)

    	raptors_players = random.sample(players, equal_division)
    	raptors.extend(raptors_players)

    player_picker(x)
    player_picker(y)


    #Format output of players
    def format_players(team):
    	players = []
    	for p in team:
    		player_record = ', '.join(p)
    		players.append(player_record)
    	final_roster = '\n'.join(players)
    	return final_roster


    #Write the final roster to the text file
    def write_file():
    	with open("teams.txt", "w") as file:

    		sharks_header = ('\n\nThe Sharks\n==============================\n')
    		get_sharks = format_players(sharks)

    		dragons_header = ('\n\nThe Dragons\n==============================\n')
    		get_dragons = format_players(dragons)

    		raptors_header = ('\n\nThe Raptors\n==============================\n')
    		get_raptors = format_players(raptors)


    		file.write(sharks_header)
    		file.write(str(get_sharks))
    		file.write(dragons_header)
    		file.write(str(get_dragons))
    		file.write(raptors_header)
    		file.write(str(get_raptors))
    write_file()

    
else:
	pass





  

