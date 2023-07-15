import random

MAX_LINES = 3 
MAX_BET = 100
MIN_BET = 1 

ROWS = 3
COLS = 3

symbol_count = {
     "A": 2,
     "B": 4,
     "C": 6,
     "D": 8
}

symbol_value = {
     "A": 5,
     "B": 4,
     "C": 3,
     "D": 2
}


def check_winning(columns, lines, bet, values):
    winnings = 0
    winning_line = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else: 
            winnings += values[symbol] * bet
            winning_line.append(line + 1)

    return (winnings,winning_line)



def get_slot_machine_spin(rows, cols ,symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items(): # .item gives both the keys and values associated with dictinary
        for x in range(symbol_count):
            all_symbols.append(symbol)

    columns = []
    for x in range(cols):
        column = []
        current_symbol = all_symbols[:]
        for x in range(rows):
           value = random.choice(current_symbol) # random.choice() is used to pick up a random value
           current_symbol.remove(value)
           column.append(value)
        
        columns.append(column)
    
    return columns

def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):  # emumerate() gives the index 0,1,2,3.... as well as the items
            if i != len(columns) - 1:   #it is the maximum index that we have
                print(column[row], end= " | ")  # end="" , it tells the print statement when to end the line
            else:
                print(column[row],  end= "")  

        print()        



def deposit():
    while True:
        amount = input("what would you like to deposit? $ ")
        if amount.isdigit():  #ifdigit() id used to see the input given by the user is num or not
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("amount should be greater than 0. ")
        else:
            print("enter a number. ")
        
    return(amount)


def get_number_of_lines():
    while True:
        lines = input("enter the number of lines to bet on(1-" + str(MAX_LINES) + ")? ")
        if lines.isdigit():  #ifdigit() id used to see the input given by the user is num or not
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("enter valid number of lines ")
        else:
            print("enter a number. ")
        
    return(lines)

def get_bet():
    while True:
        amount = input("what would you like to bet on each line? $ ")
        if amount.isdigit():  #ifdigit() id used to see the input given by the user is num or not
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"Amount must be between ${MIN_BET} - ${MAX_BET}. ")
        else:
            print("enter a number. ")
        
    return(amount)


def spin(balance):
    lines = get_number_of_lines()
    bet = get_bet()

    while True: 
        total_bet = bet * lines

        if total_bet > balance:
            print(f"you do not have enough to bet that amount, your current balance is: ${balance} ")
        else:
            break

    print(f"you are betting ${bet} on {lines} lines. The total bet is equal to: ${total_bet}" )
    

    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)
    winnings,winning_line = check_winning(slots,lines,bet,symbol_count)
    print(f"you won ${winnings}.")
    print(f"you won on lines:", *winning_line)
    return winnings - total_bet


def main():
    balance = deposit()
    while True:
        print(f"Current balance is ${balance}")
        answer = input("press enter to play(q to quit).")
        if answer == "q":
            break
        balance += spin(balance)

    print(f"you left with ${balance}")

    

main()

