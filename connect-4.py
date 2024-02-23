import turtle

# Constants
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
GRID_ROWS = 6
GRID_COLUMNS = 7
CELL_SIZE = 80
BORDER = 20
GRID_WIDTH = GRID_COLUMNS * CELL_SIZE
GRID_HEIGHT = GRID_ROWS * CELL_SIZE
PLAYER1_COLOR = "red"
PLAYER2_COLOR = "yellow"

# Initialize screen
screen = turtle.Screen()
screen.title("Connect Four")
screen.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
screen.bgcolor("blue")

# Initialize turtle
t = turtle.Turtle()
t.speed(0)
t.penup()
t.hideturtle()

# Initialize game grid
game_grid = [[0 for _ in range(GRID_COLUMNS)] for _ in range(GRID_ROWS)]

# Initialize current player
current_player = 1

# Function to draw a circle at a specific position
def draw_circle(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.color("white")
    t.begin_fill()
    t.circle(CELL_SIZE / 2 - 5)  # Adjust circle size
    t.end_fill()

# Function to handle a click event
def on_click(x, y):
    column = int((x + GRID_WIDTH / 2) // CELL_SIZE)
    if 0 <= column < GRID_COLUMNS:
        for row in range(GRID_ROWS-1, -1, -1):
            if game_grid[row][column] == 0:
                game_grid[row][column] = current_player
                draw_disc(column, row, current_player)
                if check_win(current_player):
                    screen.textinput("Connect Four", f"Player {current_player} wins!")
                    screen.bye()
                switch_player()
                break

# Function to draw a disc
def draw_disc(column, row, player):
    t.penup()
    x = column * CELL_SIZE - GRID_WIDTH / 2 + CELL_SIZE / 2
    y = row * CELL_SIZE - GRID_HEIGHT / 2 + CELL_SIZE / 2
    t.goto(x, y)
    t.pendown()
    t.color(PLAYER1_COLOR if player == 1 else PLAYER2_COLOR)
    t.begin_fill()
    t.circle(CELL_SIZE / 2 - 5)  # Adjust circle size
    t.end_fill()

# Function to switch players
def switch_player():
    global current_player
    current_player = 1 if current_player == 2 else 2

# Check for win condition
def check_win(player):
    # Check horizontally
    for row in range(GRID_ROWS):
        for col in range(GRID_COLUMNS - 3):
            if game_grid[row][col] == player and game_grid[row][col+1] == player and game_grid[row][col+2] == player and game_grid[row][col+3] == player:
                return True

    # Check vertically
    for row in range(GRID_ROWS - 3):
        for col in range(GRID_COLUMNS):
            if game_grid[row][col] == player and game_grid[row+1][col] == player and game_grid[row+2][col] == player and game_grid[row+3][col] == player:
                return True

    # Check diagonally (positive slope)
    for row in range(GRID_ROWS - 3):
        for col in range(GRID_COLUMNS - 3):
            if game_grid[row][col] == player and game_grid[row+1][col+1] == player and game_grid[row+2][col+2] == player and game_grid[row+3][col+3] == player:
                return True

    # Check diagonally (negative slope)
    for row in range(3, GRID_ROWS):
        for col in range(GRID_COLUMNS - 3):
            if game_grid[row][col] == player and game_grid[row-1][col+1] == player and game_grid[row-2][col+2] == player and game_grid[row-3][col+3] == player:
                return True

    return False

# Draw circles for each cell
for row in range(GRID_ROWS):
    for col in range(GRID_COLUMNS):
        x = col * CELL_SIZE - GRID_WIDTH / 2 + CELL_SIZE / 2
        y = -row * CELL_SIZE + GRID_HEIGHT / 2 - CELL_SIZE / 2
        draw_circle(x, y)

# Bind click event
screen.onclick(on_click)

# Start the game
screen.mainloop()
