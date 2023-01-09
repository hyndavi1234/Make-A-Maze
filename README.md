# Make-A-Maze

Make-A-Maze is a Domain-Specific Language (DSL) for constructing mazes, a concrete console-based application using Python as an interpreter language with GUI compatibility. This helps in developing gaming applications.

Through graphic user interface, we were also able to graphically represent the maze pattern and how it is used to play the game. Three different layers make up the implementation. The top layer consists of the DSL (user-written instructions), the Interpretation Layer (user commands are interpreted by performing syntactic and type checks, then calling the appropriate methods), and the Implementation Layer has the DSL commands' fundamental functionality. This performs many rules and small-step/big-step semantics internally behind the operational capability of DSL commands.

In order to have their Maze layout and utilize it, the user must first compose commands in accordance with the documentation rules. The DSL includes several commands, such as setting the variables for the maze's width and height, designing the layout, changing the cells in accordance with the programmer's preferences, printing their own statements similar to the print() feature in other imperative languages, displaying the maze's current structure, validating the maze to make sure the path leads from start to target, and finally moving through the designed maze. The user can interact with the maze by utilizing key events to navigate the graphical maze.

## Documentation

### Quick Start
The user will need to install following modules using the following commands
```
pip install PySimpleGUI
pip install numpy
```

### Program Instructions
#### Variables
Programmer can create the variables in the following format 
```
# Format 
<datatype> <varname> = <value>

# Example
int mazeWidth = 5
```
The currently supported datatype is integer (int). To pass variable as an argument to a function, prefix the variable name with $ sign.
```
createMaze($mazeWidth, $mazeHeight)
```

#### Functions
print(): To print a customized message
```
print('hi')
```

#### Maze Class
##### Class Definition:
createMaze(height, width): Command to create the maze instance with specified dimensions(int values or variables) which returns the maze object
```
Maze z = createMaze(3,3)
Maze z = createMaze($mazeWidth, $mazeHeight)
```

##### Fields
startCell and targetCell can be defined in the following way. By default the startCell will be initialized to (0,0) and the targetCell to (height-1,width-1)
```
z.startCell = (1, 1)
z.targetCell = (3, 4)
```

##### Methods
1. createEmptyCell(row, col): To create an empty cell in the maze
```
z.createEmptyCell(3, 0)
```

2. makeAMove(direction, steps): To move the current position of a player according to following directions followed by number of steps
  - Right  : {'R', 'r', 'right', 'Right'}
  - Left   : {'L', 'l', 'left', 'Left'}
  - Bottom : {'B', 'b', 'bottom', 'Bottom'}
  - Top    : {'T', 't', 'top', 'Top'}
  ```
  z.makeAMove('R', 2)
  z.makeAMove('Right', 2)
  z.makeAMove('r', 2)
  z.makeAMove('right', 2)
  ```

3. finalizeMaze(): To check valid path of a maze from start to target cell
```
z.finalizeMaze()
```

4. displayCurrentMaze(): To display the current status of the maze in console
```
z.displayCurrentMaze()
```

5. displaymazeGUI(): To show a GUI maze for the user to interact
```
z.displaymazeGUI()
```


### Execution Instructions
Create a directory and place all the core python files (Interpret.py, Implement.py) in this folder.
Create the custom program having commands according to the "Program Instructions" defined above.
To run the implementation, please change the directory in python console and then execute the Interpret.py using the following command in console
``` 
# Format
python Interpret.py <filename> 

# Example
python Interpret.py Maze1.txt
```

### GUI Maze
#### Cell Representations
| Name                           | Color                 |
| ------------------------------ | --------------------- |
| Target cell                    | Sienna4 (Brown shade) |
| Start cell                     | DarkGrey5             |
| Blocked cell                   | DodgerBlue4           |
| Current position of a player   | PaleGreen4            |
| Path cell to make moves        | azure3 (Gray shade)   |

#### Player Instructions
The player need to use the arrow keys to move through the maze. Once the current position and target position coincide, a success message pops up. User to click 'Exit' to exit the window.
