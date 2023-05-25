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
yourTotal = 0
counter = 0
for i in range(2):
    your_cards.append(random.choice(cards))
    computers_cards.append(random.choice(cards))
computers_printable_card = ['hidden', computers_cards[0]]
print("\n")
print(f"your cards : {your_cards}\n")
print(f"computers cards : {computers_printable_card}\n")
time.sleep(1)
shouldRepeat = True
while shouldRepeat:
    pickAgain = input("Enter 'y' to risk picking another card, enter 'n' to pass: ")
    if pickAgain.lower() == 'y' or pickAgain.lower() == 'n':
        shouldRepeat = False
    print()
if pickAgain.lower() == 'y':
    your_cards.append(random.choice(cards))
    print(f'you picked a {your_cards[len(your_cards)-1]} card\n')
    time.sleep(1)
print("", end='')
print(f"Computers cards : {computers_cards}\n")
time.sleep(1.5)
print(f'your cards : {your_cards}\n')
time.sleep(1)
for i in your_cards:
    if i == 'ace':
        counter += 1
    if i != 'ace':
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
if 'ace' in your_cards:
    for e in sum_cards:
        yourTotal = yourTotal + e
    for d in range(counter):
        print(f"you have {counter} ace cards\n")
        time.sleep(2)
        if d < 3:
            value = int(input(f"What value do you want for {d+1}'st ace card: "))
            print("", end='')
            yourTotal = yourTotal + value
        else:
            value = int(input(f"What value do you want for {d+1}'rd ace card: "))
            print("", end='')
            yourTotal = yourTotal + value
else:
    for i in sum_cards:
        yourTotal = yourTotal + i
if yourTotal > 21:
    print(f'your total : {yourTotal}\n')
    time.sleep(1)
    print("BUST!!")
    print("You lost. Your total was above 21")
else:
    if 'ace' in computers_cards:
        if (computerTotal + 11) > 21:
            computerTotal = computerTotal + 1
            print("Computer says it's Ace takes the value 1\n")
        else:
            computerTotal = computerTotal + 11
            print("Computer says it's Ace takes the value 11\n")
    if computerTotal < 17:
        print("computers total is less than 17 it has to pick again\n")
        computers_printable_card.append(random.choice(cards))
        time.sleep(2.5)
        print(f"computer picked a {computers_printable_card[len(computers_printable_card)-1]} card\n")
        time.sleep(1)
        if computers_printable_card[len(computers_printable_card)-1] == 'king' or computers_printable_card[len(computers_printable_card)-1] == 'queen' or computers_printable_card[len(computers_printable_card)-1] == 'jack':
            computerTotal = computerTotal + 10
        elif computers_printable_card[len(computers_printable_card)-1] == 'ace':
            if (computerTotal + 11) > 21:
                computerTotal = computerTotal + 1
                print("Computer says it's Ace takes the value 1\n")
            else:
                computerTotal = computerTotal + 11
                print("Computer says is Ace takes the value 11\n")
        else:
            computerTotal = computerTotal + computers_printable_card[len(computers_printable_card)-1]
    print(f'your total : {yourTotal}\n')
    time.sleep(1)
    print(f'computer total : {computerTotal}\n')
    if computerTotal > 21:
        print('CONGRATULATIONS!! YOU WON\n')
        time.sleep(0.5)
        print('COMPUTER BUST!!')
        time.sleep(1)
    else:
        if yourTotal > computerTotal:
            print('CONGRATULATIONS!! YOU WON')
            time.sleep(1)
        elif yourTotal < computerTotal < 22:
            print('SORRY COMPUTER WON THIS ONE!!')
            time.sleep(1)
        elif yourTotal == computerTotal:
            print('DRAW!!!  A TIGHT ONE')
            time.sleep(1)

