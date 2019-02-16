def test_fib():
    """
    Applied machine learning assignment 1, task 1.2:
    Write a function “fib” that computes the Fibonacci sequence. 
    Write a unit test that ensures that the fib(2) is 1, that fib(5) 
    is 5 and fib(12) is 144.
    """
    from task12_fib import fib
    
    assert fib(2) == 1, 'fib(2) should be 1'
    assert fib(5) == 5, 'fib(5) should be 5'
    assert fib(12) == 144, 'fib(12) should be 144'
    