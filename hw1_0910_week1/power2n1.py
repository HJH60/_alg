# 方法 a
def power2n_a(n):
    return 2**n

# 方法 b：用遞迴
def power2n_b(n):
    if n == 0: return 1
    return power2n_b(n-1)+power2n_b(n-1)

# 方法 c：用遞迴
def power2n_c(n):
    # pass
    if n == 0: return 1
    return 2*power2n_c(n-1)

# 方法 d：用遞迴+查表
power2n = [None]*10000
power2n[0] = 1
# power2n[1] = 1
def power2n_d(n):
    pass
    if n < 0: raise
    if not power2n[n] is None: return power2n[n]
    power2n[n] = power2n_d(n-1) + power2n_d(n-1) 
    return power2n[n]

print('power2n(10)=', power2n_b(10))
print('power2n(10)=', power2n_d(10))
print('power2n(40)=', power2n_d(40))