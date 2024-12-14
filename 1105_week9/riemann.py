def f(x, y, z):
    return 3 * x**2 + y**2 + 2 * z**2

def riemann_integral(n):
    dx = 1 / n
    dy = 1 / n
    dz = 1 / n
    total = 0

    for i in range(n):
        for j in range(n):
            for k in range(n):
                x = (i + 0.5) * dx
                y = (j + 0.5) * dy
                z = (k + 0.5) * dz
                total += f(x, y, z) * dx * dy * dz
    return total

n = 100
riemann_result = riemann_integral(n)
print(f"Riemann Integral (n={n}): {riemann_result}")
