import sys 


def app(n, m):
    print(n, m)
    main_array = [i for i in range(1, n + 1)]
    step = m - 1
    print(main_array[0]) 
    dif = main_array[0] + step 
    while dif != main_array[0]:               
        if dif > n:
            dif -= n
        else:
            print(dif)
            dif += step
        

if __name__ == "__main__":
    app(int(sys.argv[1]), int(sys.argv[2]))