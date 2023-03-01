s = str(input())

def format(s: str):
    if len(s) < 3: return s

    if s[-3:] != "ing":
        return s + "ing"

    if s[-3:] == "ing":
        return s + "ly"

print(format(s))