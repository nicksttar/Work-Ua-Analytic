from analytic import *
from reader import *
from sys import exit
from os import remove
from handlers import validator

print("----------Wellcome to Work Ua Analytic generator----------\n")
print('''Commands: 
y- Yes
n- No
c- Clear Data\n''')

    
user_input = validator('Have you data.csv on this directory?: ', ['y', 'n', 'c'])
if user_input == 'n':
    user_input = input('Write job to analise: ')
    write_file(user_input)
elif user_input == 'c':
    try:
        remove('data.csv')
    except FileNotFoundError:
        print('Nothing to clear, try again')
        exit()
    else:
        print('Data was cleared')
        exit()
elif user_input == 'y':
    try:
        with open('data.csv') as file:
            pass
    except FileNotFoundError:
        print('No, you have not data.csv, restart programm to create new')
        exit()
    
user_input = validator('Choose way to analise job: 1-responses, 2-viewers, 3-salaries: ')
analitics(mode=int(user_input))
