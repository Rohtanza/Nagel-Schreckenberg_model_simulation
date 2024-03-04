import turtle
import numpy as np
import random as rd

# Constants
MAX_X_COORDINATE_ON_SCREEN = 1000
PROB_OF_REDUCING_SPEED = 0.3
INITIAL_CAR_VELOCITY = 0
NUM_OF_CARS = 10
MAX_CAR_VELOCITY = 50
MAX_TIME_SIM = 100

# Initialize lists
#  List to store Turtle objects representing cars.
cars = []
# List to store the velocity of each car.
speeds = [INITIAL_CAR_VELOCITY] * NUM_OF_CARS
# List to store the density of cars in a specific range.
car_density = []
#  List to store the time taken by each car to return to its initial position.
time_to_return = [0] * NUM_OF_CARS
# List to store the number of turns made by each car.
turn_count = [0] * NUM_OF_CARS
# List containing color names for visualization of cars.
colors = ['red','green','blue','black','yellow','orange','magenta','purple','pink','aquamarine']
#  List to store the initial x-coordinates of the cars.
coordinates = []

# This loop generates random initial x-coordinates for each car within a range of -500 to 500 and then sorts them.
for _ in range(NUM_OF_CARS):
    coordinates.append(rd.randint(-500, 500))
coordinates.sort()

# These lines set up the Turtle screen with a width of 1000 pixels, a height of 300 pixels, and a minimal delay.
turtle.Screen().setup(1000, 300, 0, 0)
turtle.Screen().delay(1)

# Function to calculate distance between cars
def car_distance(k):
    next_car_index = (k + 1) % NUM_OF_CARS
    d = abs(coordinates[next_car_index] - coordinates[k])
    return min(d, MAX_X_COORDINATE_ON_SCREEN - d)

# Function to update car speed
def update_speed(k):
    d = car_distance(k)
    speeds[k] = min(speeds[k] + 10, MAX_CAR_VELOCITY)
    speeds[k] = min(speeds[k], d - 10)
    if np.random.uniform(0, 1) >= PROB_OF_REDUCING_SPEED:
        speeds[k] = max(0, speeds[k] - 10)
    return speeds[k]

# Create cars
for j in range(NUM_OF_CARS):
    cars.append(turtle.Turtle())
    cars[j].shape("turtle") # default was arrow but this cools look

# Set car coordinates and color
for i in range(NUM_OF_CARS):
    cars[i].color(colors[i])
    cars[i].penup()
    cars[i].goto(coordinates[i], 0)

# Run simulation
for curr_time in range(MAX_TIME_SIM + 1):
    car_density_count = 0
    for k in range(NUM_OF_CARS):
        cars[k].forward(update_speed(k))
        cars[k].speed(10)
        if cars[k].xcor() >= 500:
            cars[k].ht()
            cars[k].goto(-500, 0)
            cars[k].st()
        if (coordinates[k] >= cars[k].xcor()):
            if 0 <= coordinates[k] - cars[k].xcor() <= 50:
                time_to_return[k] += curr_time
                turn_count[k] += 1
        if (MAX_X_COORDINATE_ON_SCREEN / 2 - 200) <= cars[k].xcor() <= (MAX_X_COORDINATE_ON_SCREEN / 2 - 100):
            car_density_count += 1
    car_density.append(car_density_count)

# Print results
print("==============================")
print("Density on each range x80 and x90: ")
print(car_density)
print("==============================")
for x in range(NUM_OF_CARS):
    if turn_count[x] != 0:
        print(f'Average time for car {x} is {time_to_return[x] / turn_count[x]}')
    else:
        print(f'Average time for car {x} is undefined (no turns)')

