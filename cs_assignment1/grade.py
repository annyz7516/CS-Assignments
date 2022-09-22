def grade(mark, hurdle):
    """Display the grade based on the raw mark and whether
    student passed the hurdle requirements
    
    raw mark is an integer between 0 and 100 (inclusive on both sides)
    hurdles cleared is either True or False
    
    Rules:
    
    If mark is less than 50, no need to worry about hurdle,
    Outcome is mark, F

    If mark is more than or equal to 50,
    Hurdle is check. If hurdle is not cleared, 
    Outcome is 49, FH (mark drops to 49)

    If hurdle is cleared, the minimum marks and grades are:
    0: F
    50: P
    65: CR
    75: D
    85: HD

    Refer to sample output for more details
    """
    print("Original mark: "+str(mark))
    print("Hurdles cleared: "+str(hurdle))
    if hurdle == False:
        if mark >= 50:
            print("49, FH")
        else:
            print(str(mark)+", F")
    else:
        if mark < 50:
            print(str(mark)+", F")
        elif mark < 65:
            print(str(mark)+", P")
        elif mark < 75:
            print(str(mark)+", CR")
        elif mark < 85:
            print(str(mark)+", D")
        else:
            print(str(mark)+", HD")
    print("--------")

def main():
    grade(30, True)
    grade(50, True)
    grade(65, True)
    grade(75, True)
    grade(85, True)
    grade(100, True)
    grade(49, True)
    grade(64, True)
    grade(74, True)
    grade(84, True)

    grade(30, False)
    grade(50, False)
    grade(65, False)
    grade(75, False)
    grade(85, False)
    grade(100, False)
    grade(49, False)
    grade(64, False)
    grade(74, False)
    grade(84, False)

if __name__ == "__main__":
    main()
