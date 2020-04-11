players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players)

# slicing the list
print(players[0:3])

print(players[1:4])

print(players[:4])

print(players[2:])

print(players[-3:])

# looping through a slice
print("\nHere are the first three players on my team")
for players in players[:3]:
    print(players.title())