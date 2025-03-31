# import random

# result = []
# time = 0

# while time < 3:
#     result1 = random.randint(0, 101)
#     if result1 % 5 == 0:
#         result.append(result1)
#         time += 1

# print(result)
    
import datetime

love_start = datetime.datetime(2025,2,15)
aniversary = love_start + datetime.timedelta(days=100)
print(aniversary)