import threading

def halt(f, input, timeout=5):
    def target():
        f(input)
    
    thread = threading.Thread(target=target)
    thread.start()
    thread.join(timeout)  

    if thread.is_alive():
        return False 
    return True  

def f1(n):
    return n * n

def f2(n):
    s = 0
    for _ in range(n):
        for _ in range(n):
            for _ in range(n):
                for _ in range(n):
                    s = s + 1

print('halt(f1, 3) =', halt(f1, 3)) 
print('halt(f2, 10) =', halt(f2, 10)) 
print('halt(f2, 1000) =', halt(f2, 1000))  
