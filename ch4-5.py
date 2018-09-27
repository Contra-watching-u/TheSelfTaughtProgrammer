def error_func(string):
    try:
        float(string)
    except ValueError:
        print("this must be number")
error_func("abc")
