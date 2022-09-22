import random

def parkingFee(duration):
    """
    duration is in minutes.

    Display duration in hours and minutes format.
    See sample outputs for more details.

    Then display "Parking fee: $<Fee>"

    Rules:

    3 hours or under: $0
    Over 3 hours, and 3 hours 30 minutes or under: $3
    Over 3 hours 30 minutes, and 4 hours or under: $4
    Over 4 hours, and 5 hours or under: $8
    Over 5 hours, and 6 hours or under: $15
    Over 6 hours, and 8 hours or under: $25
    Over 8 hors: $100    
    """
    print(str(duration//60)+" hours "+str(duration%60)+" minutes")
    if duration <= 180:
        print("Parking fee: $0")
    elif duration <= 210:
        print("Parking fee: $3")
    elif duration <= 240:
        print("Parking fee: $4")
    elif duration <= 300:
        print("Parking fee: $8")
    elif duration <= 360:
        print("Parking fee: $15")
    elif duration <= 480:
        print("Parking fee: $25")
    else:
        print("Parking fee: $100")
    print("--------")
    
def main():
    parkingFee(10)
    parkingFee(180)
    parkingFee(181)
    parkingFee(210)
    parkingFee(211)
    parkingFee(240)
    parkingFee(241)
    parkingFee(300)
    parkingFee(301)
    parkingFee(360)
    parkingFee(361)
    parkingFee(480)
    parkingFee(481)

if __name__ == "__main__":
    main()
