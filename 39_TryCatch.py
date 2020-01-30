def calculate():
    try:
        return 5 / 0
    except ZeroDivisionError:
        raise Exception("Cant dividable by 0")
    finally:
        print('Finally block for cleanup ')


calculate()