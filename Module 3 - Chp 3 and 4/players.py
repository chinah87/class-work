#creating a slice
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])
print(players[1:4])

#omit the first index and Python will automatically start from list beginning
print(players[:4])

#same with omitting the last index...Python will automatically go to list ends
print(players[2:])

#output the last three players on the list with negative numbers
print(players[-3:])
print("\n")

#loop through the first three players
print("Here are the first three players on my team:")
for player in players[:3]:
    print(player.title())
print("\n")