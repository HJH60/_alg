import numpy as np
def f(x, y, z):
    return 3 * x**2 + y**2 + 2 * z**2

def monte_carlo_integral(num_points):
    points = np.random.rand(num_points, 3)  
    values = f(points[:, 0], points[:, 1], points[:, 2])
    return np.mean(values) * 1.0  

num_points = 100000 
monte_carlo_result = monte_carlo_integral(num_points)
print(f"Monte Carlo Method Integral(num_points={num_points}): {monte_carlo_result}")