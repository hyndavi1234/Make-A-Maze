from Implement import *
import sys

#Defining a store Gamma which stores definitions
gamma = {}

#Read the file
try:
    filename = str(sys.argv[1])
except:
    print("Error: Improper syntax for CLI.")
    exit(0)

program = open(filename, 'r').readlines()

#Global variables
undefinedtype = 'undeftype'

print('\n')

def error_msg(msg, fname):
    if (fname == 'createMaze' or fname=='type_match'):
        print(f'\nError: \nEncountered {msg} of CreateMaze Fun but expected parameter of Variable or Int\n')

#Type check - return the type of the variable
def syntax_check(val):
    if val.isnumeric() == True:
        return 'numeric'
    elif val[0] == '$':
        return 'variable'
    else:
        return undefinedtype

#lookup variable inside the gamma
def var_lookup(var):
    var = var[1:]
    return gamma[var][0]

#do type check and return value
def type_match(val, type):
    if type == 'int':
        if val.isnumeric() == True:
            return True
        else:
            return False

#call function based on syntax_check
def get_value(param, type):
    param = param.strip()
    if (syntax_check(param) == 'numeric') & type_match(param, type):
        return int(param)
    elif (syntax_check(param) == 'variable') & type_match(var_lookup(param), type):
        return int(var_lookup(param))
    else:
        return syntax_check(param)


for index, line in enumerate(program):
    if line != '\n':                    #Exclude blank lines
        line = line.replace('\n', '')   #Remove the \n literal from each line
        
        if line.split()[0] in ('int'):
            dtype, vname, op, value = line.split()   
            gamma[vname] = [value, dtype]

        elif line.__contains__('print'):
            b, kword, s = line.partition('print')
            text = s[s.find('(') + 1 : s.find(')')]
            print('\n', text)

        elif line.__contains__('createMaze'):
            #Type checking + Call ClassMaze
            b, kword, s = line.partition('createMaze')
            cname, oname, op = b.split()

            size = s[s.find('(') + 1 : s.find(')')]
            row, col = size.split(',')
            row = get_value(row, 'int')
            col = get_value(col, 'int')

            if row == undefinedtype:
                error_msg(f'{type(row)} for Maze Width', 'createMaze')
                break
            elif col == undefinedtype:
                error_msg(f'{type(col)} for Maze Height', 'createMaze')
                break
            else:
                objname = ClassMaze(row, col)
                objname.create() 
                objname.flag = 0
                #Add the object to the gamma context
                gamma[oname] = [objname, cname]

        elif line.__contains__('createEmptyCell'):
            #Type checking + Call ClassMaze
            b, kword, s = line.partition('createEmptyCell')
            oname = b.replace('.','')
            obj = gamma[oname][0]

            size = s[s.find('(') + 1 : s.find(')')]
            row, col = size.split(',')
            row = get_value(row, 'int')
            col = get_value(col, 'int')

            if (row != undefinedtype) & (col != undefinedtype):
                obj.update_empty_cell(row, col)
                obj.flag = 0

        elif ((line.__contains__('startCell')) or (line.__contains__('targetCell'))):
            if line.__contains__('startCell'):
                b, kword, s = line.partition('startCell')
                oname = b.replace('.','')
                obj = gamma[oname][0]
                size = s[s.find('(') + 1 : s.find(')')]
                row, col = size.split(',')
                obj.update_start_cell((get_value(row, 'int'), get_value(col, 'int')))

            elif line.__contains__('targetCell'):
                b, kword, s = line.partition('targetCell')
                oname = b.replace('.','')
                obj = gamma[oname][0]
                size = s[s.find('(') + 1 : s.find(')')]
                row, col = size.split(',')
                obj.update_target_cell((get_value(row, 'int'), get_value(col, 'int')))
            obj.flag = 0

        elif line.__contains__('displayMaze'):
            b, kword, s = line.partition('displayMaze')
            oname = b.replace('.','')
            obj = gamma[oname][0]
            print('\n Your Maze view: ')
            obj.display()

        elif line.__contains__('displayCurrentMaze'):
            b, kword, s = line.partition('displayCurrentMaze')
            oname = b.replace('.','')
            obj = gamma[oname][0]
            print('\n Your current Maze view: ')
            obj.display_current_maze()

        elif line.__contains__('makeAMove'):
            b, kword, s = line.partition('makeAMove')
            oname = b.replace('.','')
            obj = gamma[oname][0]
            if(obj.check_path_covered()):
                continue
            size = s[s.find('(') + 1 : s.find(')')]
            direction, steps = size.split(',')

            direction = direction.strip().replace("'",'')
            steps = get_value(steps, 'int')

            res = 0
            (res, current_cell) = obj.move_steps(direction, steps)

            if(res == steps):
                print(f'command makeAMove({direction}, {steps}) succesfully moved {steps} step\s')
            elif((res < steps) and (res > -1)):
                print(f'There is no valid path for the specified steps in command - makeAMove({direction}, {steps})')
            elif(res == -1):
                print(f"Hurray, you've reached the target with the command makeAMove({direction}, {steps})")
            else:
                print(f'There is something wrong when executing command makeAMove({direction}, {steps})')
        elif line.__contains__('finalizeMaze'):
            b, kword, s = line.partition('finalizeMaze')
            oname = b.replace('.','')
            obj = gamma[oname][0]
            if(obj.flag!=True):
                obj.validateMaze()
                if(obj.flag!=True):
                    print("Maze has no proper path")
                    break
                else:
                    print("\nMaze is valid and has been finalized.")
            else:
                print("Maze has already been validated.")
        elif line.__contains__('displaymazeGUI'):
            b, kword, s = line.partition('displaymazeGUI')
            oname = b.replace('.','')
            obj = gamma[oname][0]
            if(obj.flag!=True):
                obj.validateMaze()
                if(obj.flag!=True):
                    print("\nMaze has no proper path.\n")
                    continue
            if(obj.check_path_covered()):
                print("\nUser has already reached the exit before.\n")
                continue
            obj.GUI(oname)
            obj.GetScreen(oname)