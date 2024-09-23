import sys

def check_odd_even(number):
    assert isinstance(number, int), "Argument must be an integer"
    if number % 2 == 0:
        print("I'm even")
    else:
        print("I'm odd")

if __name__ == "__main__":
    assert len(sys.argv) == 2, "You must provide one argument"
    
    try:
        num = int(sys.argv[1])
        check_odd_even(num)
    except ValueError:
        assert False, "Argument must be an integer"
