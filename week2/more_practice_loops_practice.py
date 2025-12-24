# #for loop 
# # starting , end,stepping (number with range)
# for i in range (1,100,5):
#     print(i)

# # display numbers from 0 to 100 steping by 10
# for i in range(0, 101, 10):
#     print(i)
#for i in range (1, 5,1):
  #  print(i)
    
# for i in range(5):  # Repeat 5 times
#     for j in range(1, 6):  # Print numbers 1 to 5
#         print(j, end=' ')
#     print()  # New line after each row
# for i in range (5):
#     for j in range(1,6):
#         print(j)

# for i in range(5):  
#     for j in range(1, 6):  # Print numbers 1 to 5
#         print(j, end=' ')
#     print()  # New line after each row
# for i in range(1, 6):
#     print(' '.join(map(str, range(1, i + 1))))


# for i in range(1, 6):
#     print(' ' * (5 - i) + ' '.join(map(str, range(1, i + 1))))
# for i in range(0,5,1):
#     for j in range(1, 6):
#         print(j, end=' ')
        
#     print()  # New line after each row


# for i in range(1, 20):
#     print('*' * i)

# rows = 5

# # for i in range(1, rows + 1):
# #     print(' ' * (rows - i) + '* ' * i)


# # rows = 5

# # # Tree leaves
# # for i in range(1, rows + 1):
# #     print(' ' * (rows - i) + '* ' * i)

# # # Tree trunk
# # for _ in range(2):
# #     print(' ' * (rows - 1) + '*')



# # ANSI color codes
# GREEN = '\033[92m'  # Bright Green
# BROWN = '\033[33m'  # Yellow/Brown
# RESET = '\033[0m'   # Reset color

# rows = 5

# # Tree leaves in green
# for i in range(1, rows + 1):
#     print(' ' * (rows - i) + (GREEN + '* ' + RESET) * i)

# # Tree trunk in brown
# for _ in range(2):
#     print(' ' * (rows - 1) + BROWN + '*' + RESET)


#christmas tree

# # ANSI color codes
# GREEN = '\033[92m'      # Bright Green
# DIM_GREEN = '\033[32;2m'  # Dim Green
# RED = '\033[91m'        # Red ornaments
# YELLOW = '\033[93m'     # Yellow ornaments
# BROWN = '\033[33m'      # Brown trunk
# RESET = '\033[0m'       # Reset

# rows = 12

# for i in range(1, rows + 1):
#     line = ' ' * (rows - i)
#     for j in range(i):
#         # Fixed pattern for ornaments and lights:
#         if (i + j) % 7 == 0:
#             line += RED + '*' + RESET + ' '    # red ornament
#         elif (i + j) % 5 == 0:
#             line += YELLOW + '*' + RESET + ' ' # yellow ornament
#         elif (i + j) % 3 == 0:
#             line += DIM_GREEN + '*' + RESET + ' '  # dim green light
#         else:
#             line += GREEN + '*' + RESET + ' '    # normal green leaf
#     print(line)

# # Tree trunk (3 lines)
# for _ in range(3):
#     print(' ' * (rows - 2) + BROWN + '***' + RESET)


#myname GI R U M
# ANSI color codes
GREEN = '\033[92m'
YELLOW = '\033[93m'
RED = '\033[91m'
CYAN = '\033[96m'
MAGENTA = '\033[95m'
RESET = '\033[0m'

letters = {
    'G': [
        "  **** ",
        " *     ",
        "*      ",
        "*  *** ",
        " *   * ",
        "  ***  "
    ],
    'I': [
        " ***** ",
        "   *   ",
        "   *   ",
        "   *   ",
        "   *   ",
        " ***** "
    ],
    'R': [
        " ****  ",
        " *   * ",
        " ****  ",
        " *  *  ",
        " *   * ",
        " *    *"
    ],
    'U': [
        "*     *",
        "*     *",
        "*     *",
        "*     *",
        " *   * ",
        "  ***  "
    ],
    'M': [
        "*     *",
        "**   **",
        "* * * *",
        "*  *  *",
        "*     *",
        "*     *"
    ]
}

# Map each letter to a color
colors = {
    'G': GREEN,
    'I': YELLOW,
    'R': YELLOW,
    'U': RED,
    'M': RED
}

# Print each row
for i in range(6):
    line = ''
    for ch in 'GIRUM':
        line += colors[ch] + letters[ch][i] + RESET + '  '
    print(line)


#Ethiopian Flags
# ANSI color codes
GREEN = '\033[42m'   # Green background
YELLOW = '\033[43m'  # Yellow background
RED = '\033[41m'     # Red background
BLUE = '\033[44m'    # Blue background
RESET = '\033[0m'    # Reset formatting

width = 40
height = 5

# Print green stripe
for _ in range(height):
    print(GREEN + ' ' * width + RESET)

# Print yellow stripe
for _ in range(height):
    print(YELLOW + ' ' * width + RESET)

# Print red stripe
for _ in range(height):
    print(RED + ' ' * width + RESET)

# Optional: Blue circle with yellow star (very simplified)
center_row = ' ' * ((width // 2) - 4) + BLUE + '   ★   ' + RESET
print('\n' + center_row)



# ANSI color codes
CYAN = '\033[96m'
MAGENTA = '\033[95m'
RESET = '\033[0m'

# ASCII Art for "WELCOME"
welcome = [
    "*       *  *****   *       *   *****   *       *  *******",
    "*       *  *       **     **   *       **     **  *      ",
    "*   *   *  *****   * *   * *   *****   * *   * *  *****  ",
    "*  * *  *  *       *  * *  *   *       *  * *  *  *      ",
    "* *   * *  *****   *   *   *   *****   *   *   *  *******"
]

# Print with alternating colors
for line in welcome:
    print(CYAN + line[:35] + RESET + MAGENTA + line[35:] + RESET)
