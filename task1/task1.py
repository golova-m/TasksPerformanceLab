import sys 


def app(n, m):
    start_value = 1
    step = m - 1
    print(start_value)
    dif = start_value + step 
    while dif != start_value:               
        if dif > n:
            dif -= n 
        else:
            print(dif)
            dif += step
        

if __name__ == "__main__":
    app(int(sys.argv[1]), int(sys.argv[2]))