# python3

def parallel_processing(n, m, data):
    output = []
    # TODO: write the function for simulating parallel tasks, 
    # create the output pairs
    
    thread = [(i, 0) for i in range (n)]
    for i in range (m):
        ind, end = min(thread, k = lambda x: x[1])
        output.append((ind,end))
        thread[ind] = (ind, end + data[i])

    return output

def main():
    # TODO: create input from keyboard
    # input consists of two lines
    # first line - n and m
    # n - thread count 
    # m - job count
    n = 0
    m = 0
    

    # second line - data 
    # data - contains m integers t(i) - the times in seconds it takes any thread to process i-th job
    data = []

    n, m = map(int, input().split())
    data = list(map(int, input().split()))
    
    # TODO: create the function
    result = parallel_processing(n,m,data)
    
    # TODO: print out the results, each pair in it's own line
    for i in range(m):
        print(result[i][0], result[i][1])


if __name__ == "__main__":
    main()
