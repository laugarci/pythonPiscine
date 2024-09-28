import sys
from ft_filter import ft_filter


def filter_words(s, n):
    assert isinstance(s, str) and isinstance(n, int), "Error: you must enter a string and an int"
    return ft_filter(lambda word: len(word) > n, s.split())


if __name__ == "__main__":
    try:
        if len(sys.argv) != 3:
            raise AssertionError("Error: you must enter two arguments")
        
        # Validar que el primer argumento sea un string que no sea completamente numérico
        s = sys.argv[1]
        if s.isdigit():
            raise AssertionError("Error: first argument must be a non-numeric string")
        
        # Validar que el segundo argumento sea un número
        try:
            n = int(sys.argv[2])
        except ValueError:
            raise AssertionError("Error: second argument must be an integer")
        
        result_ft_filter = filter_words(s, n)
        result_filter = list(filter(lambda word: len(word) > n, s.split()))
        
        print("Result from ft_filter: ", result_ft_filter)
        print("Result from filter: ", result_filter)
        
    except AssertionError as e:
        print(e)
        sys.exit(1)
