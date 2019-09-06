# Reverses integer, if reversed integer is over 32bit maximum returns 0 instead


def reverse(number: int):
    abs_num = abs(number)
    if number < 0:
        r_number = int(("-" + (str(abs_num)[::-1])))
        if abs(r_number) > 0x7FFFFFFF:
            return 0
        return(int(r_number))
    else:
        r_number = int(str(abs_num)[::-1])
        if abs(r_number) > 0x7FFFFFFF:
            return 0
        return(int(r_number))
