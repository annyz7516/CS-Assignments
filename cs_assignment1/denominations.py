import random

def denominations(amount):
    """
    Given the total amount (in cents), display the 
    denominations required to pay the amount

    First round off the amount to nearest 5 cents.

    See sample outputs for format required.
    """
    print("original value (in cents): "+str(amount))
    if amount%5 >= 3:
        amount = amount + 5
    amount = amount - amount%5
    print("rounded off to nearest 5 cents: "+str(amount))
    print("Amount in dollars: $"+str(amount/100))
    print("$100 x "+str(amount//10000))
    amount=amount%10000
    print("$50 x "+str(amount//5000))
    amount=amount%5000
    print("$20 x "+str(amount//2000))
    amount=amount%2000
    print("$10 x "+str(amount//1000))
    amount=amount%1000
    print("$5 x "+str(amount//500))
    amount=amount%500
    print("$2 x "+str(amount//200))
    amount=amount%200
    print("$1 x "+str(amount//100))
    amount=amount%100
    print("50amount x "+str(amount//50))
    amount=amount%50
    print("20amount x "+str(amount//20))
    amount=amount%20
    print("10amount x "+str(amount//10))
    amount=amount%10
    print("$5amount x "+str(amount//5))
    print("--------")
    
def main():
    denominations(12)
    denominations(1729)
    denominations(1234)
    denominations(82021)

if __name__ == "__main__":
    main()
