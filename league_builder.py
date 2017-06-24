import csv
import random
#Make sure script doesn't execute when imported. Keep all code within name == main

#Create variables and programming logic to divide the 18 players into three teams:
#Sharks, Dragons and Raptors. Make sure the teams have the same number of 
#players on them, and that the experience players are divided equally across the three teams.

#Create a text file named teams.txt that includes the name of a team, 
#followed by the players on that team. List all three teams and their players.

#In the list of teams, include the team name on one line, followed by a separate 
#line for each player. Include the player's name, whether the player has experience 
#playing soccer, and the player's guardian names. Separate each bit of player information by a comma.


if __name__ == '__main__':

    #open soccer_players.csv with the ability to read and parse data. 

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
    				new_players.append(row)
    		return experienced_players, new_players

    x,y = sort_players()   

   
    #Create logic that seperates the experiences players from the new players
    # def create_roster(Experience):

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

    print('Sharks are: {}'.format(sharks))
    print('Dragons are: {}'.format(dragons))
    print('Sharks are: {}'.format(raptors))


    #Write team name to teams.txt file with seperator line
    def write_file():
    	with open("teams.txt", "w") as file:
    		final_sharks = ('The Sharks\n==========================\n{}'.format(sharks))
    		final_dragons = ('The Dragons\n==========================\n{}'.format(dragons))
    		final_raptors = ('The Raptors\n==========================\n{}'.format(raptors))
    		file.write(final_sharks)
    		file.write(final_dragons)
    		file.write(final_raptors)
    write_file()




#Divide experienced players up uevenly into the three teams

#Divide the new players up into the teams

#Check to ensure that each team has 1/3 of players and that experience is equal

  

