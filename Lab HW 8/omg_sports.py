# Uses 2D lists to analyze basketball scoring data

# Returns total points scored by player p
def player_total_points(data, p):
    total = 0 # Stores player total points
    for i in range(len(data[p])): # Goes through each game
        total += data[p][i] # Adds game points to total
    return total # Returns total points


# Returns average points per game for player p
def player_average_ppg(data, p):
    total = player_total_points(data, p) # Gets total points
    average = total / len(data[p]) # Calculates average
    return average # Returns average points


# Returns index of player with most total points
def best_overall_player(data):
    best_index = 0 # Starts with first player
    best_points = player_total_points(data, 0) # Starting high score
    for i in range(len(data)): # Checks every player
        current = player_total_points(data, i) # Gets current player's points
        if current > best_points:
            best_points = current # Updates highest point total
            best_index = i # Updates best player index
    return best_index # Returns best player


# Returns team points scored in game g
def team_points_in_game(data, g):
    total = 0 # Stores team point total
    for i in range(len(data)): # Goes through each player
        total += data[i][g] # Adds points from game g
    return total # Returns team total

# Stores basketball scoring data
scores = [
[20,27,16,23,20,27,18],
[8,18,14,17,9,12,0],
[34,19,25,22,19,25,31],
[17,8,11,34,15,0,9],
[2,0,3,0,10,2,4]
]

# Tests all functions
print(player_total_points(scores,2), "Expected: 175")
print(player_average_ppg(scores,2), "Expected: 25.0")
print(best_overall_player(scores), "Expected: 2")
print(team_points_in_game(scores,6), "Expected: 62")