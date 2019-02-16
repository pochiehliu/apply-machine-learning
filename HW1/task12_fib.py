def fib(x):
    """
    Applied machine learning assignment 1, task 1.2:
    Write a function “fib” that computes the Fibonacci sequence. 
    Write a unit test that ensures that the fib(2) is 1, that fib(5) 
    is 5 and fib(12) is 144.
    """
    
    assert (int(x) == x and x>=0), " x must be a positive integer."
    
    if x == 0 or x == 1:
        return x
    
    fib_array = [0 for x in range(x+1)]
    
    fib_array[0], fib_array[1] = 0, 1
    
    for i in range(2, x+1):
        fib_array[i] = fib_array[i-1] + fib_array[i-2]
        
    return fib_array[-1]
    