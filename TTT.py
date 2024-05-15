# grid = [["_","_","_"],["_","_","_"],["_","_","_"]]
# num = 0
# while True:
#     if num == 9:
#         break
#     if num % 2 == 0:
#         while True:
#             x = int(input("Player 1's Turn. Enter X Coordinate: "))
#             y = int(input("Enter Y Coordinate: "))
#             if grid[2-(y-1)][x-1] == "_":
#                 grid[2-(y-1)][x-1] = "1"
#                 break
#             else:
#                 print(f"Error: There is already an element in ({x},{y})")
#     else:
#         while True:
#             x = int(input("Player 2's Turn. Enter X Coordinate: "))
#             y = int(input("Enter Y Coordinate: "))
#             if grid[2-(y-1)][x-1] == "_":
#                 grid[2-(y-1)][x-1] = "2"
#                 break
#             else:
#                 print(f"Error: There is already an element in ({x},{y})")
#     #wincon spotting
#     for row in grid:
#         for elem in row:
#             print(elem, end = "\t")
#         print("\n")
    
#     num += 1

from pynput import keyboard

def on_press(key):
    try:
        print('alphanumeric key {0} pressed'.format(
            key.char))
    except AttributeError:
        print('special key {0} pressed'.format(
            key))

def on_release(key):
    print('{0} released'.format(
        key))
    if key == keyboard.Key.esc:
        # Stop listener
        return False

# Collect events until released
with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()
