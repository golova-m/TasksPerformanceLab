import sys 


def app(n, m):
    print(n, m)
    main_array = [i for i in range(1, n + 1)]
    step = m - 1
    dif = 1 + step
    print(1) 
    while dif != 1:               
        if dif > n:
            dif -= n
        else:
            print(dif)
            dif += step
        

if __name__ == "__main__":
    app(int(sys.argv[1]), int(sys.argv[2]))