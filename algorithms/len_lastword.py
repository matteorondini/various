# Returns the lenght of the last full word contained in the string "s"


def lengthOfLastWord(s: str):
    return len(s.strip().split(" ")[-1])
