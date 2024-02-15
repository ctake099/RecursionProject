# import sys
# import random

# min_n = 0
# max_n = 0

# while (min_n >= max_n):
#     try:

#         sys.stdout.buffer.write(b"Please input the minimum number :   \n")
#         sys.stdout.flush()
#         min_n = int(sys.stdin.buffer.readline().decode())


#         sys.stdout.buffer.write(b"Please input the maximum number :   \n")
#         sys.stdout.flush()
#         max_n = int(sys.stdin.buffer.readline().decode())
#     except:
#         sys.stdout.buffer.write(b"Please input the number\n")
#         sys.stdout.flush()   

#     if min_n >= max_n:
#         sys.stdout.buffer.write(b"Please input the mamimum number is higher than minimum number\n")
#         sys.stdout.flush()     

# target = random.randint(min_n, max_n)

# for i in range(1, 6):
#     sys.stdout.buffer.write(b"input the guess number\n")
#     sys.stdout.flush()
#     guess_n = int(sys.stdin.buffer.readline().decode())
#     if (target == guess_n):
#         sys.stdout.buffer.write(b"correct\n")
#         sys.stdout.flush()
#         break
#     else:
#         sys.stdout.buffer.write(b"incorrect\n")
#         sys.stdout.flush()
    
#     if i == 5:
#         sys.stdout.buffer.write(b"Sorry, you've reached the maximum number of tries.\n")
#         sys.stdout.buffer.write(f"The correct number was {target}.\n".encode())  # 正解を教える
#         sys.stdout.flush()

import sys
import random

def input_number(prompt):
    while True:
        sys.stdout.buffer.write(prompt.encode())
        sys.stdout.flush()
        try:
            return int(sys.stdin.buffer.readline().decode())
        except ValueError:
            sys.stdout.buffer.write(b"Please input a valid integer number.\n")

min_n = input_number("Please input the minimum number: ")
max_n = input_number("Please input the maximum number: ")
while min_n >= max_n:
    sys.stdout.buffer.write(b"Maximum number must be greater than minimum number. Please input again.\n")
    max_n = input_number("Please input the maximum number: ")

target = random.randint(min_n, max_n)

for i in range(1, 6):
    guess_n = input_number("Input the guess number: ")
    if target == guess_n:
        sys.stdout.buffer.write(b"Correct!\n")
        sys.stdout.flush()
        break
    else:
        sys.stdout.buffer.write(b"Incorrect.\n")
        sys.stdout.flush()
    
    if i == 5:
        sys.stdout.buffer.write(b"Sorry, you've reached the maximum number of tries.\n")
        sys.stdout.buffer.write(f"The correct number was {target}.\n".encode())
        sys.stdout.flush()
