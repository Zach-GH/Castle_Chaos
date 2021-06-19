#Zachary Meisner
import sys


def start(): #start function, first thing player sees explains game and how to play
    print('\n        ', 'Welcome to Castle Chaos\n'                   
                        'The Castle has been taken over by an evil wizard.\n'
                        'Everyone has been turned into creatures!\n'
                        'Stop the wizard and avoid being turned into a frog.\n'
                        'Explore the castle and find all the items in order win!\n'
                        
                        
          '            ', 'HOW TO PLAY\n'
          '-----------------------------------------\n'
          'Move commands: North, South, East, West\n'
          "Add to inventory: get, take, or grab 'item'\n"
          'See player Status: Status'
          "See item description: inspect 'item'\n"
          'Exit the game with q or quit\n'
          'To see this page again type options\n'
          '-----------------------------------------')
    while True: #basic loop to start the game, keeps it from crashing if the player enters a wrong command, or lets them quit.
        start_game = input('Would you like to start playing?(Y/N)').strip().lower()
        if start_game == 'y':
            main()
        elif start_game == 'n':
            print('see you soon!')
            sys.exit()
        else:
            print("I don't understand that command.")
            continue

def options(): #function made in the case player forgets commands, can be called any time by the player.
    print('            ', 'HOW TO PLAY\n'
    '-----------------------------------------\n'
    'Move commands: North, South, East, West\n'
    "Add to inventory: get, take, or grab 'item'\n"
    "See Player Status: Status"
    "See item description: inspect 'item'\n"
    'Exit the game with q or quit\n'
    'To see this page again type options\n'
    '-----------------------------------------')


def main(): #main game loop, including the game map, and other functions.
    rooms = { #Creates game map with callable keys, in order to make the game play smooth and feel realistic
        'Foyer':
             {'name': 'Foyer', #name of the room
              'south': 'Dining Room', #Get player input, Push to Dining Room
              'text': 'A beautiful entry hall\n' 
                      'You see a door to the south.',
              'item': False #There is no item in this room.
              },
        'Dining Room':
             {'name': 'Dining Room',
              'north': 'Foyer',
              'west': 'Armory',
              'text': 'It looks like everyone was about to have dinner!\n'
                      'You see some cats having a birthday party.\nthey even have party hats!\n'
                      'You see a door to the north.\n'
                      'You see a door to the west.',
              'item': ['shield'], #Get player input TAKE 'ITEM'
              'item description': 'This is one giant dinner plate.'}, #Get player input INSPECT ITEM
        'Armory':
             {'name': 'Armory',
              'east': 'Dining Room',
              'north': 'Servants Quarters',
              'south': 'Guards Quarters',
              'west': 'Throne Room',
              'text': 'Armor and weapons galore! Too bad all of them are locked away.\n'
                      'You see a door to the east.\n'
                      'You see a door to the north.\n'
                      'You see a door to the south.\n'
                      'You see a door to the west.',
              'item': ['helmet'],
              'item description': "This goes on your egg noggin!"},

        'Servants Quarters':
             {'name': 'Servants Quarters',
              'east': 'Royal Bedroom',
              'south': 'Armory',
              'text': 'This is the cleanest place in the castle!\n'
                      'I guess the wizard still needs someone to keep things tidy.\n'
                      'There are imps in uniforms everywhere!\n'
                      'You see a door to the east.\n'
                      'You see a door to the south.',
              'item': ['banana'],
              'item description': "Be careful where you throw this!"},
        'Royal Bedroom':
             {'name': 'Royal Bedroom',
              'west': 'Servants Quarters',
              'text': "Looks like somebody didn't make their bed!\n"
                      'You see a door to the west.',
              'item': ['cape'],
              'item description': "Made out of bedsheets!."},
        'Guards Quarters':
             {'name': 'Guards Quarters',
              'north': 'Armory',
              'east': 'Kitchen',
              'text': "You see a bunch of dogs sitting around a table playing poker.\n"
                      'You see a door to the north.\n'
                      'You see a door to the east.',
              'item': ['sword'],
              'item description': 'Shiny!'},
        'Kitchen':
             {'name': 'Kitchen',
              'west': 'Guards Quarters',
              'text': 'This place is an absolute disaster\n'
                      'There is a unicorn with a chefs hat!\n'
                      'You see a door to the west.',
              'item': ['cake'],
              'item description': 'The cake is a lie'},

        'Throne Room':
            {'name': 'Throne Room',
              'text': False #Does not return text upon entering room.
              },
         }

    directions = ['north', 'south', 'east', 'west'] #Directions accepted
    current_room = rooms['Foyer'] #Room the player starts in
    inventory = [] #Empty inventory, Player input puts items here.
    inventory_counter = 0 #Player Records, helps maintain lock status on final door
    actions = 0 #fun function for player score
    rooms_visited = 1 #fun function for player score

    def status():
        print('You are in {}.'.format(current_room['name']))  # Where is the player
        if current_room['item']: #If there is an item in the room
            print('You see a {} on the ground'.format(', '.join(current_room['item']))) #OUTPUT ITEM to Get input
        else:
            pass #If there is no item in the room skip this.
        print('Inventory:', inventory)
        print('Rooms Visited:', rooms_visited)
        print('Actions:', actions)
        print('Inventory Value:', inventory_counter)

    while True: #beginning of input
        print()
        print('You are in {}.'.format(current_room['name'])) #Where is the player
        print()
        print(current_room['text']) #Call text key from corresponding room
        print('Inventory :', inventory) #Keeps track of player inventory
        if current_room['item']: #If there is an item in the room
            print('You see a {} on the ground'.format(', '.join(current_room['item']))) #OUTPUT ITEM to Get input
        command = input('\nWhat do you do?\n').strip().lower() #Player input
        if command in directions: #basic movement functionality
            if command in current_room: #command needs to be made in room to designate which areas they can go to
                current_room = rooms[current_room[command]]
                actions = actions + 1
                rooms_visited = rooms_visited + 1
            else:
                print("You can't go that way.") #Wrong input No door that way

        elif command in ('q', 'quit'): #Quit command
            sys.exit()

        elif command.lower().split()[0] in ('get', 'take', 'grab'): #Player Pick up items
            item = command.lower().split()[1] #split item from sentence
            if item in current_room['item']:
                current_room['item'].remove(item) #removes item from room and places in inventory
                inventory.append(item)
                inventory_counter = inventory_counter + 1 #if player picks item up, inventory_counter adds 1

            else:
                print("I don't see that here.")

        elif command.lower().split()[0] in ('drop'): #Player drops item
            item = command.lower().split()[1]
            if item in inventory:
                current_room['item'].append(item) #appends item to room
                inventory.remove(item) #removes item from inventory
                inventory_counter = inventory_counter - 1 #if player drops item, inventory counter drops 0
            else:
                print("You aren't carrying that")

        elif command.lower().split()[0] in ('inspect'): #inspect item description
            item = command.lower().split()[1]
            if item in inventory: #item has to be in inventory
                print(current_room['item description']) #call key item description

        elif command in ('options'): #options panel
            options()

        elif command in ('status'):  # status panel
            status()
        else:
            print("I don't understand that command.")




        if inventory_counter != 6 and current_room == rooms['Throne Room']: #uses inventory counter to tell wether or not player can enter room
                    print('You see the evil wizard sitting on the throne.\n'
                          'Realizing you do not have all the items\n'
                          'You try to make a run for it!\n'
                          'But fall on your face!\n'
                          'You see your legs starting to turn green.\n'
                          'And you turn into a frog!\n'
                          'Game Over! Ribbit!') #You lose!
                    print('Commands Entered:', actions) #output player scores
                    print('Rooms Visited:', rooms_visited)
                    print('Items Collected:', inventory)
                    print()
                    sys.exit()

        if inventory_counter == 6 and current_room == rooms['Throne Room']:
            print('You walk in and see the evil wizard on the throne.\n'
                  'Luckily you came prepared!\n'
                  'As the evil wizard goes to cast a spell.\n'
                  'You throw a banana!\n'
                  'All of a sudden, you see a monkey jump out from behind the chair.\n'
                  'He sits on the wizard!.\n'
                  'You walk up, and offer the cake to the monkey.\n'
                  'The money accepts the cake, as it is a banana cake.\n'
                  'Monkey: "I see you came prepared for a fight!\n'
                  'Monkey: Luckily you did not have to.\n'
                  'You have set the castle free with just a banana!\n')
            print('You win!') #You win!
            print('Commands Entered:', actions)
            print('Rooms Visited:', rooms_visited)
            print('Items Collected:', inventory)
            sys.exit()

start() #starts game with function above
