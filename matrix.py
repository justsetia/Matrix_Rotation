import numpy as np
import matplotlib.pyplot as plt
import math

x = 1
y = 1

def rotate_flash(degree):
    global x, y

    rad = -math.radians(degree)
    flash = np.array([[0, x],  [0, y]])

    editedX = x * math.cos(rad) - y * math.sin(rad)
    editedY = x * math.sin(rad) + y * math.cos(rad)

    Rotated_flash = np.array([[0, editedX], [0, editedY]])

    # Clear the previous plot
    plt.cla()

    # Plot the original and rotated flash
    plt.plot(flash[0], flash[1], 'r', lw=3, label='Original Flash')
    plt.plot(Rotated_flash[0], Rotated_flash[1], 'b', lw=3, label='Rotated Flash')
    plt.xlim(-2, 2)
    plt.ylim(-2, 2)
    plt.gca().set_aspect('equal', adjustable='box')
    plt.grid(True)
    plt.title(f'Flash rotated by {degree} degrees')
    plt.legend()

    # Update the plot
    plt.draw()
    plt.pause(0.1)

plt.ion()

# Create an empty figure
plt.figure()

rotate_flash(0)
while True:
    degree_input = int(input("Enter degree to rotate: "))
    rotate_flash(degree_input)
