import random
import time

print('''
                    Yb        dP 888888 88      dP""b8  dP"Yb  8b    d8 888888  
                     Yb  db  dP  88__   88     dP   `" dP   Yb 88b  d88 88__          
                      YbdPYbdP   88""   88  .o Yb      Yb   dP 88YbdP88 88""          
                       YP  YP    888888 88ood8  YboodP  YbodP  88 YY 88 888888 ''')
print('''
      888888  dP"Yb      88""Yb 88        db     dP""b8 88  dP  88888    db     dP""b8 88  dP 
        88   dP   Yb     88__dP 88       dPYb   dP   `" 88odP      88   dPYb   dP   `" 88odP  
        88   Yb   dP     88""Yb 88  .o  dP__Yb  Yb      88"Yb  o.  88  dP__Yb  Yb      88"Yb  
        88    YbodP      88oodP 88ood8 dP""""Yb  YboodP 88  Yb "bodP' dP""""Yb  YboodP 88  Yb ''')

cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'king', 'queen', 'jack', 'ace', ]
your_cards = []
computers_cards = []
sum_cards = []
sum_computer = []
computerTotal = 0
for i in range(2):
    your_cards.append(random.choice(cards))
    computers_cards.append(random.choice(cards))
computers_printable_card = ['hidden', computers_cards[0]]
print("\n")
print(f"your cards : {your_cards}")
print()
print(f"computers cards : {computers_printable_card}")
time.sleep(1)
print()
pickAgain = input("Enter 'y' to risk picking another card, enter 'n' to pass: ")
print()
if pickAgain.lower() == 'y':
    your_cards.append(random.choice(cards))
    print(f'you picked a {your_cards[len(your_cards)-1]}')
print()
print(f"Computers cards : {computers_cards}")
for i in your_cards:
    sum_cards.append(i)
for i in computers_cards:
    if i != 'ace':
        sum_computer.append(i)
for i in sum_cards:
    if i == 'king' or i == 'queen' or i == 'jack':
        sum_cards[sum_cards.index(i)] = 10
for i in computers_cards:
    if i == 'king' or i == 'queen' or i == 'jack':
        sum_computer[sum_computer.index(i)] = 10
for i in sum_computer:
    computerTotal = computerTotal + i
if 'ace' in computers_cards:
    if (computerTotal + 11) > 21:
        computerTotal = computerTotal + 1
        print("Computer says it's Ace takes the value 1")
    else:
        computerTotal = computerTotal + 11
        print("Computer says is Ace takes the value 11")
print()
print(f'your cards : {your_cards}')


