#from __future__ import print_function

import random

class Person(object):
    
    def __init__(self, choice):
        self.choice=choice

    
class Computer(object):

    def __init__(self, choice):
        self.choice = choice

def PersonChoice():
    print("Choose 1 for Paper, 2 for Scissors, 3 for Rock")
    Person.choice=''
    while Person.choice not in '1 2 3'.split():

        Person.choice=input('choose an option following the guide:')
        Person.choice=str(Person.choice)

    if Person.choice =='1' :
        print("You chose Paper")
    elif Person.choice =='2':
        print("You chose Scissors")
    else:
        print("You chose Rock")

def ComputerChoice():
    Computer.choice =random.randint(1,3)
    Computer.choice=str(Computer.choice)
    #print(compchoice)
    if Computer.choice == '1':
        print("She chose Paper")
    elif Computer.choice == '2':
        print("She chose Scissors")
    else:
        print("She chose Rock")

def ChooseWinner():
   if Person.choice==Computer.choice:
       print('its a draw ')
   elif Person.choice== '1' and Computer.choice=='3':
       print('You win')
   elif Person.choice== '1' and Computer.choice=='2':
       print('You lose')
   elif Person.choice== '2' and Computer.choice=='3':
       print('You lose')
   elif Person.choice== '2' and Computer.choice=='1':
       print('You win')
   elif Person.choice== '3' and Computer.choice=='2':
       print('You win')
   else:# Person.choice== '3' and Computer.choice=='1':
       print('You lose')

   PlayAgain()

def PlayAgain():
    pa = input("Wanna play again?, type yes if you do:")
    if pa== 'yes':
        PersonChoice()
        ComputerChoice()
        ChooseWinner()
    else:
        pass

PersonChoice()
ComputerChoice()
ChooseWinner()
