import csv
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

    def open_file():
    	with open("soccer_players.csv", newline = '') as csvfile:
    		reader = csv.DictReader(csvfile, delimiter = ',')
    		for row in reader:
    			print(row['Name'], row['Soccer Experience'])

    
    #Create logic that seperates the experiences players from the new players
    # def create_roster(Experience):

    


    #Write team name to teams.txt file with seperator line
    def write_file():
    	with open("teams.txt", "w") as file:
    		file.write('Test writer') #Change this to actual team names
    write_file()




#Divide experienced players up uevenly into the three teams

#Divide the new players up into the teams

#Check to ensure that each team has 1/3 of players and that experience is equal

  

