#create a guest list and invite them to dinner
guests = ['pooh', 'tigger', 'eeyore', 'rabbit']

name = guests[0].title()
print('Greetings, ' + name + '. You are cordially invited to dinner!')

name = guests[1].title()
print('Greetings, ' + name + '. You are cordially invited to dinner!')

name = guests[2].title()
print('Greetings, ' + name + '. You are cordially invited to dinner!')

name = guests[3].title()
print('Greetings, ' + name + '. You are cordially invited to dinner!')

#someone can't come!
name = guests[1].title()
print('\n' + name + ' has to do laundry, and cannot make it.')

#replace that guest with a new guest, and resend the invites
guests[1] = 'kanga'

name = guests[0].title()
print('\nGreetings, ' + name + '. You are cordially invited to dinner!')

name = guests[1].title()
print('Greetings, ' + name + '. You are cordially invited to dinner!')

name = guests[2].title()
print('Greetings, ' + name + '. You are cordially invited to dinner!')

name = guests[3].title()
print('Greetings, ' + name + '. You are cordially invited to dinner!')

#we found a bigger table!
print('\nGood news everyone, we found a bigger table!')

#add three more guests and resend invites
guests.insert(0, 'owl')
guests.insert(3, 'roo')
guests.append('piglet')

name = guests[0].title()
print('\nGreetings, ' + name + '. You are cordially invited to dinner!')

name = guests[1].title()
print('Greetings, ' + name + '. You are cordially invited to dinner!')

name = guests[2].title()
print('Greetings, ' + name + '. You are cordially invited to dinner!')

name = guests[3].title()
print('Greetings, ' + name + '. You are cordially invited to dinner!')

name = guests[4].title()
print('Greetings, ' + name + '. You are cordially invited to dinner!')

name = guests[5].title()
print('Greetings, ' + name + '. You are cordially invited to dinner!')

name = guests[6].title()
print('Greetings, ' + name + '. You are cordially invited to dinner!')

#print a message indicating how many people you are inviting to dinner
number = len(guests)
print("\nCurrently, there are " + str(number) + " guests coming to dinner.")

#oops, the table won't come in time for dinner...
print('\nSorry guys, I made a mistake with my Amazon order. Looks like I can only have two people over this time!')

#send apologies to four guests
name = guests.pop(0)
print('\nHey ' + name.title() + ', can I invite you over next time instead?')

name = guests.pop(1)
print('Hey ' + name.title() + ', can I invite you over next time instead?')

name = guests.pop(1)
print('Hey ' + name.title() + ', can I invite you over next time instead?')

name = guests.pop(1)
print('Hey ' + name.title() + ', can I invite you over next time instead?')

name = guests.pop(1)
print('Hey ' + name.title() + ', can I invite you over next time instead?')

#send a message to two guests to let them know they're still invited
name = guests[0].title()
print("\nHey " + name + ", it'll be a small gathering, but please come over still!")

name = guests[1].title()
print("Hey " + name + ", it'll be a small gathering, but please come over still!")

#delete the last two names and print list to show it is empty
del guests[0]
del guests[0]
print(guests)