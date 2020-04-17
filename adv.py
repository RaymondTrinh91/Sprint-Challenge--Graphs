from room import Room
from player import Player
from world import World
from helper import Graph, Queue, Stack

import random
from ast import literal_eval

# Load world
world = World()

# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# # Fill this out with directions to walk
# # traversal_path = ['n', 'n']
traversal_path = []
reversed_path = []
rooms = {}
reverse_direction = {'n': 's', 's': 'n', 'e': 'w', 'w': 'e'}

# rooms[0] = player.current_room.get_exits()

# while len(rooms) < len(room_graph) - 1:
#     current = player.current_room
#     if current.id not in rooms:
#         rooms[current.id] = current.get_exits()
#         previous = reversed_path[-1]
#         rooms[current.id].remove(previous)

#     while len(rooms[player.current_room.id]) < 1:
#         reverse = reversed_path.pop()
#         traversal_path.append(reverse)
#         player.travel(reverse)

#     next_direction = rooms[player.current_room.id].pop(0)
#     traversal_path.append(next_direction)
#     reversed_path.append(reverse_direction[next_direction])
#     player.travel(next_direction)

rooms = []
visited = set()
def traverse(current_location):
    rooms.append(current_location)
    if current_location not in visited:
        visited.add(current_location)
        for direction, room_id in room_graph[current_location][1].items():
            # print(room_graph[current_location].items())
            if room_id not in visited:
                traverse(room_id)
                rooms.append(current_location)

def traverse_rooms(rooms):
    for i in range(len(rooms) - 1):
        for direction, room_id in room_graph[rooms[i]][1].items():
            if room_id == rooms[i + 1]:
                traversal_path.append(direction)

traverse(player.current_room.id)
traverse_rooms(rooms)

# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")



#######
# UNCOMMENT TO WALK AROUND
#######
# player.current_room.print_room_description(player)
# while True:
#     cmds = input("-> ").lower().split(" ")
#     if cmds[0] in ["n", "s", "e", "w"]:
#         player.travel(cmds[0], True)
#     elif cmds[0] == "q":
#         break
#     else:
#         print("I did not understand that command.")
