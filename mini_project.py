# Space Travel Calculator
print("welcome to the space travel calculator")
distance = input("enter the distance to your destination (in light-years): ")
distance = float(distance)

speed = input("Enter the speed of your spaceship(as a fraction of the speed of light): ")
speed = float(speed)

time = distance / speed

print(f"It would take {time} years to reach your destination.")

