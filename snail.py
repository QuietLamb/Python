well = 30
day = 0
up = 3
down = 2
current = 0

while True:
    current += up
    day += 1
    if current>=well:
        break
    current -= down
print("It tooks {} days for snail to escape".format(day))
