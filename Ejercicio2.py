from sage.all import *

# Define the variables
x, y, z = var('x y z')

# Define the function to integrate
f = x^2 + y^2 + z^2

# Define the region of integration
region = (x, -1, 1), (y, -1, 1), (z, -1, 1)

# Compute the integral
integral_result = integral(f, *region)

# Print the result
print(f"Integral result: {integral_result}")

# Plot the 3D model of the function
plot3d(f, (x, -1, 1), (y, -1, 1)).show()