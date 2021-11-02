local = 6
def example():
    # making local variable as global
    global local
    print(local)
    local+=7
    print(local)
example()