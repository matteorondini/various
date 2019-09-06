# Checks if int number is palindrome


def isPalindrome(number: int):
    copy = number  # store copy
    reverse = 0  # store reverse
    while copy > 0:  # executes until copy is above 0
        last_dig = copy % 10  # gets last digit from copy
        # reverse * 10, then appends last digit to reverse
        reverse = (reverse * 10) + last_dig
        copy = copy // 10  # cuts last digit from copy by integer division
    return number == reverse
