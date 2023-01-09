import PySimpleGUI as sg
import numpy as np
import copy as cp

class ClassMaze:
    def __init__(self, width, height) -> None:
        self.__height = height
        self.__width = width
        self.__maze = [[],[]]
        self.__start_cell = (0, 0)
        self.__target_cell = (height-1, width-1)
        self.__current_cell = list(self.__start_cell)
        self.flag = False
        self.__VARS = {'cellSizeh': '', 'cellSizew': '', 'gridSize': 400, 'canvas': False, 'window': False, 'cellMAP': False}
    
    def create(self):
        self.__maze = np.full((self.__height, self.__width), '#')
        self.__maze[self.__start_cell[0]][self.__start_cell[1]]   = 'S'
        self.__maze[self.__target_cell[0]][self.__target_cell[1]] = 'T'

    def display(self):
        print(self.__maze)

    def display_current_maze(self):
        curr_maze = cp.deepcopy(self.__maze)
        curr_maze[self.__current_cell[0]][self.__current_cell[1]] = 'C'
        print(curr_maze)
    
    def update_empty_cell(self, row, col):
        if(self.__maze[row][col]!='T' and self.__maze[row][col]!='S'):
            self.__maze[row][col] = ' '

    def update_start_cell(self, cell):
        self.__maze[self.__start_cell[0]][self.__start_cell[1]] = '#'
        self.__start_cell = cell
        self.__current_cell = list(self.__start_cell)
        self.__maze[self.__start_cell[0]][self.__start_cell[1]] = 'S'
    
    def update_target_cell(self, cell):
        self.__maze[self.__target_cell[0]][self.__target_cell[1]] = '#'
        self.__target_cell = cell
        self.__maze[self.__target_cell[0]][self.__target_cell[1]] = 'T'

    def check_path_covered(self):
        return (list(self.__current_cell)==list(self.__target_cell))
    def check_path_exists(self):
        if self.solveMazeUtil(self.__start_cell[0], self.__start_cell[1]) == False:
            print("Solution doesn't exist")
            return False
        return True
            
    def check_valid_move(self, x, y):  #checks if a position is empty
        try:
            return ((self.__maze[x][y] == ' ') or (self.__maze[x][y] == 'T')) 
        except:
            return False
            
    def solveMazeUtil1(self,x,y):
        if x == self.__target_cell[0] and y == self.__target_cell[1]:
            return True
         
        if (x<self.__width and x>=0
            and y<self.__height and y>=0 and
                ((self.check_valid_move(x, y) == True) 
             or self.__maze[x][y] =='S' or [x, y]==self.__current_cell)):
            if self.solveMazeUtil1(x + 1, y) == True:
                return True
            if self.solveMazeUtil1(x, y + 1) == True:
                return True
            
            
    def solveMazeUtil2(self,x,y):
        if x == self.__target_cell[0] and y == self.__target_cell[1]:
            return True
         
        if (x<self.__width and x>=0
            and y<self.__height and y>=0 and
                ((self.check_valid_move(x, y) == True) 
             or self.__maze[x][y] =='S' or [x, y]==self.__current_cell)):
            if self.solveMazeUtil2(x - 1, y) == True:
                return True
            if self.solveMazeUtil2(x, y + 1) == True:
                return True
    
    
    def solveMazeUtil3(self,x,y):
        if x == self.__target_cell[0] and y == self.__target_cell[1]:
            return True
         
        if (x<self.__width and x>=0
            and y<self.__height and y>=0 and
                ((self.check_valid_move(x, y) == True) 
             or self.__maze[x][y] =='S' or [x, y]==self.__current_cell)):
            if self.solveMazeUtil3(x - 1, y) == True:
                return True
            if self.solveMazeUtil3(x, y - 1) == True:
                return True    
    
    
    
    def solveMazeUtil4(self,x,y):
        if x == self.__target_cell[0] and y == self.__target_cell[1]:
            return True
         
        if (x<self.__height and x>=0
            and y<self.__width and y>=0 and
                ((self.check_valid_move(x, y) == True) 
             or self.__maze[x][y] =='S' or [x, y]==self.__current_cell)):
            if self.solveMazeUtil4(x + 1, y) == True:
                return True
            if self.solveMazeUtil4(x, y - 1) == True:
                return True    
    
    def validateMaze(self):
        if self.__start_cell[0]<=self.__target_cell[0] and self.__start_cell[1]<=self.__target_cell[1]:
            self.flag = self.solveMazeUtil1(self.__start_cell[0],self.__start_cell[1])
        elif self.__start_cell[0]>=self.__target_cell[0] and self.__start_cell[1]<=self.__target_cell[1]:
            self.flag = self.solveMazeUtil2(self.__start_cell[0],self.__start_cell[1])
        elif self.__start_cell[0]>=self.__target_cell[0] and self.__start_cell[1]>=self.__target_cell[1]:
            self.flag = self.solveMazeUtil3(self.__start_cell[0],self.__start_cell[1])
        elif self.__start_cell[0]<=self.__target_cell[0] and self.__start_cell[1]>=self.__target_cell[1]:
            self.flag = self.solveMazeUtil4(self.__start_cell[0],self.__start_cell[1])    

    def move_steps(self, direc, steps):  #if a proposed move is valid, updates the current cell
    #get the current cell values into x and y
        if(self.flag!=True):
            self.validateMaze()
            if(self.flag!=True):
                print("Maze has no proper path for ", self)
                return
        x, y = self.__current_cell[0], self.__current_cell[1]
        if direc == 'L' or direc == 'l' or direc == "Left" or direc == "left":
            i = 1
            while(i <= steps):
                if(self.check_valid_move(x, y - i)):
                    self.__current_cell = (x, y - i)
                    i += 1
                    self.__maze[self.__current_cell[0]][self.__current_cell[1]] = '\u2190' #to display the path travelled
                    if(self.__current_cell == self.__target_cell):
                        return -1, self.__current_cell
                else:
                    break
            return ((i - 1), self.__current_cell)                                          #returns the valid traversed steps
        if direc == 'R' or direc == 'r' or direc == "right" or direc == "Right":
            i = 1
            while(i <= steps):
                chk = self.check_valid_move(x, y + i)
                if(self.check_valid_move(x, y + i)):
                    self.__current_cell = (x, y + i)
                    i += 1
                    self.__maze[self.__current_cell[0]][self.__current_cell[1]] = '\u2192'
                    if(self.__current_cell == self.__target_cell):
                        return -1, self.__current_cell
                else:
                    break
            return ((i - 1), self.__current_cell)
        if direc == 'T' or direc == 't' or direc == "top" or direc == "Top":
            i = 1
            while(i <= steps):
                if(self.check_valid_move(x - i, y)):
                    self.__current_cell = (x - i, y)
                    i += 1
                    self.__maze[self.__current_cell[0]][self.__current_cell[1]] = '\u2191'
                    if(self.__current_cell == self.__target_cell):
                        return -1, self.__current_cell
                else:
                    break
            return ((i - 1), self.__current_cell)
        if direc == 'B' or direc == 'b' or direc == "bottom" or direc == "Bottom":
            i = 1
            while(i <= steps):
                if(self.check_valid_move(x + i, y)):
                    self.__current_cell = (x + i, y)
                    i += 1
                    self.__maze[self.__current_cell[0]][self.__current_cell[1]] = '\u2193'
                    if(self.__current_cell == self.__target_cell):
                        return -1, self.__current_cell
                else:
                    break
            return ((i - 1), self.__current_cell)

    def validateEvents(self, e):
        move = ''
        if len(e) == 1:
            if ord(e) == 63232:    # UP
                move = 'Up'
            elif ord(e) == 63233:  # DOWN
                move = 'Down'
            elif ord(e) == 63234:  # LEFT
                move = 'Left'
            elif ord(e) == 63235:  # RIGHT
                move = 'Right'
        # Filter key press Windows :
        else:
            if e.startswith('Up'):
                move = 'Up'
            elif e.startswith('Down'):
                move = 'Down'
            elif e.startswith('Left'):
                move = 'Left'
            elif e.startswith('Right'):
                move = 'Right'
        return move

    def drawGrid(self):
        self.__VARS['canvas'].TKCanvas.create_rectangle(
            1, 1, self.__VARS['gridSize'], self.__VARS['gridSize'], outline='BLACK', width=1)
        for x in range(self.__height):
            self.__VARS['canvas'].TKCanvas.create_line(
                ((self.__VARS['cellSizeh'] * x), 0), ((self.__VARS['cellSizeh'] * x), self.__VARS['gridSize']),
                fill='BLACK', width=1)
        for y in range(self.__width):
            self.__VARS['canvas'].TKCanvas.create_line(
                (0, (self.__VARS['cellSizew'] * x)), (self.__VARS['gridSize'], (self.__VARS['cellSizeh'] * x)),
                fill='BLACK', width=1)

    def drawCell(self, x, y, color='GREY'):
        self.__VARS['canvas'].TKCanvas.create_rectangle(
        x, y, x + self.__VARS['cellSizeh'], y + self.__VARS['cellSizew'],
        outline='BLACK', fill=color, width=1)

    def placeCells(self):
        for row in range(self.__VARS['cellMAP'].shape[0]):
            for column in range(self.__VARS['cellMAP'].shape[1]):
                if(self.__maze[column][row] == '#'):
                    self.drawCell((self.__VARS['cellSizeh']*row), (self.__VARS['cellSizew']*column), 'DodgerBlue4')
                elif(self.__maze[column][row] == ' '):
                    self.drawCell((self.__VARS['cellSizeh']*row), (self.__VARS['cellSizew']*column), 'azure3')

    def GUI(self, var):
        AppFont = 'Any 18'
        sg.theme('DarkGrey5')
        self.__VARS['cellSizeh'] = self.__VARS['gridSize']/self.__height
        self.__VARS['cellSizew'] = self.__VARS['gridSize']/self.__width
        self.__VARS['cellMAP'] = self.__maze
        layout = [[sg.Canvas(size=(self.__VARS['gridSize'], self.__VARS['gridSize']),
                    background_color='white',
                    key='canvas')], [sg.Exit(font=AppFont), sg.Text('', key='-exit-', font=AppFont, size=(15, 3))]]

        self.__VARS['window'] = sg.Window(str('Maze Mania for -   Maze '+var), layout, resizable=True, finalize=True, return_keyboard_events=True, titlebar_text_color='TOMATO', titlebar_font='Times New Roman', titlebar_background_color='black')
        self.__VARS['canvas'] = self.__VARS['window']['canvas']
        self.drawGrid()
        self.placeCells()
        self.drawCell((self.__VARS['cellSizeh']*self.__current_cell[1]), (self.__VARS['cellSizew']*self.__current_cell[0]), 'PaleGreen4')
        self.drawCell(self.__target_cell[1]*self.__VARS['cellSizeh'], self.__target_cell[0]*self.__VARS['cellSizew'], 'Sienna4')
        
        
    def GetScreen(self, var):  
        i = self.__current_cell[0]
        j = self.__current_cell[1]

        while True:             # Event Loop
            event, values = self.__VARS['window'].read()
            if event in (None, 'Exit'):
                break
            # Filter key press
            yPos = self.__current_cell[1]
            xPos = self.__current_cell[0]
            if self.validateEvents(event) == 'Up':
                if self.__current_cell[0]>0:
                    if self.__maze[xPos-1][yPos] != '#':
                        self.__current_cell[0] = self.__current_cell[0] - 1
            elif self.validateEvents(event) == 'Down':
                if self.__current_cell[1]<self.__height:
                    if self.__maze[xPos+1][yPos] != '#':
                        #print("Moving down")
                        self.__current_cell[0] = self.__current_cell[0] + 1
            elif self.validateEvents(event) == 'Left':
                if (self.__current_cell[1]>0):
                    if self.__maze[xPos][yPos-1] != '#':
                        #print("Moving Left")
                        self.__current_cell[1] = self.__current_cell[1] - 1
            elif self.validateEvents(event) == 'Right':
                if (self.__current_cell[0]<self.__width):
                    if self.__maze[xPos][yPos+1] != '#':
                        self.__current_cell[1] = self.__current_cell[1] + 1
            self.__VARS['canvas'].TKCanvas.delete("all")
            self.drawGrid()
            self.placeCells()
            self.drawCell((self.__VARS['cellSizeh']*j), (self.__VARS['cellSizew']*i), 'GREY')
            self.drawCell((self.__VARS['cellSizeh']*self.__current_cell[1]), (self.__VARS['cellSizew']*self.__current_cell[0]), 'PaleGreen4')
            self.drawCell(self.__target_cell[1]*self.__VARS['cellSizeh'], self.__target_cell[0]*self.__VARS['cellSizew'], 'Sienna4')


            # Check for Exit:
            yPos = self.__current_cell[1]
            xPos = self.__current_cell[0]
            if [xPos, yPos] == list(self.__target_cell):
                layout = [[sg.Text(text='Congrats! You reached the end!', font = 'Any 18')], 
                    [sg.Exit(font='Any 12', size=(13, 1))]]
                self.__VARS['window'] = sg.Window(str('Maze Mania for -   Maze '+var), layout, resizable=True, finalize=True, return_keyboard_events=True, titlebar_text_color='TOMATO', titlebar_font='Times New Roman', titlebar_background_color='black')
            else:
                self.__VARS['window']['-exit-'].update('')
        self.__VARS['window'].close()