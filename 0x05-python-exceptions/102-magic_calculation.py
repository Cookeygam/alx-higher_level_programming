#!/usr/bin/python3

def magic_calculation(a, b):
    result = 0
    for i in range(1, 3):
        try:
            if i > a:
                raise Exception('Too far')
<<<<<<< HEAD

            result += a ** b / i
=======
            else:
                result += a ** b / i
>>>>>>> 8a221194591db8b65e451d73f713bfbb001c7d29
        except:
            result = b + a
            break
    return (result)
