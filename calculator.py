"""num1=int(input("enter the first number:"))
num2=int(input("enter the second number:"))
operation=input('enter the operation:')
if operation== "+":
    print("result:" + str(num1 + num2))
elif operation== "-":
    print("result:" + str(num1 - num2))
elif operation== "*":
    print("result:" + str(num1 * num2))
elif operation== "/":
    print("result:" + str(num1 / num2))
else:
    print("invalid")"""
def winner(computer_move,player_move):
if computer_move == player_move:
winner = 'tie'
elif player_move == 'Rock' and computer_move == 'Papper':
winner = 'computer'
elif player_move == 'Papper' and computer_move == 'Scissor':
winner = 'computer'
elif player_move == 'Scissor' and computer_move == 'Rock':
winner= 'computer'
else:
winner='computer'
return winner


     