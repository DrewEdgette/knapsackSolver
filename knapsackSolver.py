import random
#------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------
# knapsackSolver() takes 4 arguments:
#   capacity = how much weight the bag can hold
#   items = how many items are being stolen
#   prices = array of price for each item
#   weights = array of weight for each item

# solves using the tabulation method


def knapsackSolver(capacity, items, prices, weights):
    # the solution will be an array of size items
    solution = [0] * items

    # if your bag cant even hold a single item, don't bother with the rest
    if min(weights) > capacity:
        return solution

    # increase both by one so that one row and col hold the zeros
    capacity = capacity + 1
    items = items + 1

    # creates the table with 0 as the default value
    table = [[0 for w in range(capacity)] for i in range(items)]


    # for every element in the table, we plug it into a formula that will tell us what it should be. 
		# If the difference between the table weight value and the value of the corresponding element in 
		# the weight list is negative, we don't have to compare with max(). If it's positive, 
		# we need to find out which one is larger.
    for i in range(1, items):
        for w in range(capacity):
            diff = w - weights[i - 1]
            if diff < 0:
                table[i][w] = table[i - 1][w]
            else:
                table[i][w] = max(
                    table[i - 1][w],
                    table[i - 1][diff] + prices[i - 1])  # formula

    # once we have all of the table values, we need to start from the end of it and find the maximum
		# value. Then we need to find the lowest row where that value shows up.

    maximum = 0
    index = 0

    for i in reversed(table):
        if max(i) >= maximum:
            maximum = max(i)  # maximum value
            index = table.index(i)  # row where it shows up

    # take maximum and subtract the corresponding prices index value. 
		# This will give us the next element to look for.

    # If we are certain that this is the lowest row that value shows up in, 
		# we can say that the item in solution[index-1] can be taken.

    next1 = maximum - prices[index - 1]
    solution[index - 1] = 1

    # keep looking for the next element until the index is 0
    while index > 0:
        for i in reversed(table):
            if next1 in i:
                index = table.index(i)

        if index > 0:
            next1 = next1 - prices[index - 1]
            solution[index - 1] = 1
        else:
            next1 = next1 - prices[index]

    return solution


#------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------

# random example

numJewels = 4
bagSize = 8

priceList = []
weightList = []

for j in range(numJewels):
    priceList.append(random.randrange(1, 9))
    weightList.append(random.randrange(1, 9))

solution = knapsackSolver(bagSize, numJewels, priceList, weightList)

print("Number of jewels: " + str(numJewels))
print("Carrying capacity: " + str(bagSize) + "lbs\n")
print(str(priceList) + " prices")
print(str(weightList) + " weights")
print(str(solution) + " solution")
