def trip_cost():
    miles = int(424)
    mpg = int(24)
    price = float(3.24)
    gallonsUsed = miles // mpg
    gasCost = price * gallonsUsed
    totalCost = gasCost

    return (totalCost)

trip_cost()

def main():
    miles = int(input("How many miles are in your trip? "))
    mpg = int(input("How many miles per gallon does your vehicle get? "))
    price = float(input("What's the price of gas per gallon? $ "))
    tank = int(input("How many gallons can your tank hold? "))

    return trip_cost()

main()



