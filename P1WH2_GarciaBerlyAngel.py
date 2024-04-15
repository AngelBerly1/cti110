#Angel Garcia
#4/14/24
#Assignment name P1HW2
#Todays assignment is to create a python code filed named P1HW2
print()
print("This program calculates and displays travel expenses")
# user is asked to enter initial budget
budget=int(input('Enter your budget: '))
# user is asked to enter travel destination
travel_destination=input('Enter travel destination: ')
# user is asked how much they think they will spend on gas
gas=int(input('How much do you think you will spend on gas? '))
# user is asked how much they will spend on accomodations
accomodations=int(input('Approximately, how much will you need for accomodation/hotel? '))
# user is asked how much they will spend on food
food=int(input('Last, how much do you need for food?: '))
print()
expense = gas + accomodations + food
balance = budget - expense


#print('---------------Travel Expenses--------------')
print(12*'-' + 'Travel Expenses' + 12*'-')
print("Location: ", travel_destination)
print("Initial Budget: ", budget)
print()
print("Fuel: ", gas)
print("Accomodation: ", accomodations)
print("Food: ", food)
print()
remaining = balance - expense
print("Remaining balance: ", balance)
