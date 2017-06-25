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


    	# #take players and randomly sample and assign them to teams

    	equal_division = len(players) // 3

    	shark_players = players[0:equal_division]
    	sharks.extend(shark_players)

    	dragon_players = players[equal_division:equal_division*2]
    	dragons.extend(dragon_players)

    	raptors_players = players[equal_division*2:]
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

    def write_letter(team):
    	practice_time = "July 29th, at 8:00 A.M."
    	practice_location = "Barnes Park"

    	for player in team:
    		get_player_name = player[0]
    		player_first_name = get_player_name.split(' ',1)[0]
    		get_guardian_name = player[2]
    		file_title = get_player_name.replace(' ','_')
    		file_name = file_title.lower()+'.txt'
    	
	    	with open(file_name, "w") as file:
	    		file.write("Dear {},\n\n".format(get_guardian_name))
	    		file.write("I'm coach Hood and I can't wait to meet {} on the field.\n".format(player_first_name))
	    		file.write("Our first practice is at {} on {}.\n".format(practice_location, practice_time))
	    		file.write("I'll see you guys then!\n\n")
	    		file.write("sincerely,\n")
	    		file.write("Coach Hood")

    write_letter(sharks)





  

