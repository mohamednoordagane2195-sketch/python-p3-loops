def happy_new_year():
    """Print out the phrase "Happy New Year!" once per second, for 10 seconds."""
    # YOUR CODE HERE
    for i in range(10):
        print("Happy New Year!")
        time.sleep(1)

def square_integers(int_list):
    """Return a new list of integers from int_list, squared."""
    # YOUR CODE HERE
    return [i**2 for i in int_list] 

def fizzbuzz():
    """Print the numbers from 1 to 100. But for multiples of three print "Fizz"
    instead of the number, and for the multiples of five print "Buzz". For
    numbers which are multiples of both three and five print "FizzBuzz"."""
    # YOUR CODE HERE
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)


            