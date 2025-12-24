# import random
# import time

# # ANSI color codes
# GREEN = "\033[32m"
# YELLOW = "\033[33m"
# RED = "\033[31m"
# RESET = "\033[0m"

# height = 20  # bigger tree
# trunk_height = 4
# trunk_width = 5

# # Function to create a big festive tree
# for i in range(1, height + 1):
#     row = ""
#     for j in range(2 * i - 1):
#         # Randomly pick leaf or lights
#         rnd = random.random()
#         if rnd < 0.1:
#             row += YELLOW + "*" + RESET  # yellow light
#         elif rnd < 0.2:
#             row += RED + "*" + RESET  # red light
#         else:
#             row += GREEN + "*" + RESET  # green leaf
#     print(" " * (height - i) + row)
#     time.sleep(0.05)  # small delay for visual effect

# # Tree trunk
# for i in range(trunk_height):
#     print(" " * (height - trunk_width // 2 - 1) + GREEN + "*" * trunk_width + RESET)


### Dynamic tree size with decorations
import random
import time
import os

# ANSI color codes
GREEN = "\033[32m"
YELLOW = "\033[33m"
RED = "\033[31m"
RESET = "\033[0m"
CLEAR_SCREEN = "\033[2J\033[H"

height = 20
trunk_height = 4
trunk_width = 5

def draw_tree():
    tree_lines = []

    # Tree leaves with random lights
    for i in range(1, height + 1):
        row = ""
        for j in range(2 * i - 1):
            rnd = random.random()
            if rnd < 0.08:
                row += YELLOW + "*" + RESET  # yellow light
            elif rnd < 0.16:
                row += RED + "*" + RESET  # red light
            else:
                row += GREEN + "*" + RESET  # green leaf
        tree_lines.append(" " * (height - i) + row)

    # Tree trunk
    trunk_line = " " * (height - trunk_width // 2 - 1) + GREEN + "*" * trunk_width + RESET
    for _ in range(trunk_height):
        tree_lines.append(trunk_line)

    return tree_lines

# Animate the tree
while True:
    print(CLEAR_SCREEN, end="")  # clear terminal
    tree = draw_tree()
    for line in tree:
        print(line)
    time.sleep(0.3)  # change speed for dim/twinkle effect
