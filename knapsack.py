import numpy as np

class Knapsack01Problem:
    """This class encapsulates the Knapsack 0-1 Problem from RosettaCode.org
    """
    def __init__(self):
        # initialize instance variables:
        self.items = []
        self.maxCapacity = 0
        
        # initialize the data:
        self.__initData()
        
    def __initData(self):
        """initializes the RosettaCode.org knapsack 0-1 problem data
        """
        self.items = [
            {"name": "map", "weight": 9, "value": 150},
            {"name": "compass", "weight": 13, "value": 35},
            {"name": "water", "weight": 153, "value": 200},
            {"name": "sandwich", "weight": 50, "value": 160},
            {"name": "glucose", "weight": 15, "value": 60},
            {"name": "tin", "weight": 68, "value": 45},
            {"name": "banana", "weight": 27, "value": 60},
            {"name": "apple", "weight": 39, "value": 40},
            {"name": "cheese", "weight": 23, "value": 30},
            {"name": "beer", "weight": 52, "value": 10},
            {"name": "suntan cream", "weight": 11, "value": 70},
            {"name": "camera", "weight": 32, "value": 30},
            {"name": "t-shirt", "weight": 24, "value": 15},
            {"name": "trousers", "weight": 48, "value": 10},
            {"name": "umbrella", "weight": 73, "value": 40},
            {"name": "waterproof trousers", "weight": 42, "value": 70},
            {"name": "waterproof overclothes", "weight": 43, "value": 75},
            {"name": "note-case", "weight": 22, "value": 80},
            {"name": "sunglasses", "weight": 7, "value": 20},
            {"name": "towel", "weight": 18, "value": 12},
            {"name": "socks", "weight": 4, "value": 50},
            {"name": "book", "weight": 30, "value": 10}
        ]
        
        self.maxCapacity = 400  # decagrams (4kg)

    def __len__(self):
        """
        :return: the total number of defined items
        """
        return len(self.items)
        
    def getValue(self, zeroOneList):
        """
        Calculates the value of the selected items in the list, while ignoring items that will cause the accumulating weight to exceed the maximum weight
        :param zeroOneList: a list of 0/1 values corresponding to the list of the problem's items. '1' means that item was selected.
        :return: the calculated value
        """
        totalWeight = totalValue = 0
        
        for i in range(len(zeroOneList)):
            if zeroOneList[i] == 1:
                item = self.items[i]
                if totalWeight + item["weight"] <= self.maxCapacity:
                    totalWeight += item["weight"]
                    totalValue += item["value"]
                else:
                    pass  # skip if overweight
        
        return totalValue
    
    def printItems(self, zeroOneList):
        """
        Prints the selected items in the list, while ignoring items that will cause the accumulating weight to exceed the maximum weight
        :param zeroOneList: a list of 0/1 values corresponding to the list of the problem's items. '1' means that item was selected.
        """
        totalWeight = totalValue = 0
        
        for i in range(len(zeroOneList)):
            if zeroOneList[i] == 1:
                item = self.items[i]
                if totalWeight + item["weight"] <= self.maxCapacity:
                    totalWeight += item["weight"]
                    totalValue += item["value"]
                    print(f"- Adding {item['name']}: weight = {item['weight']}, value = {item['value']}, "
                          f"accumulated weight = {totalWeight}, accumulated value = {totalValue}")
                else:
                    print(f"- Skipping {item['name']}: would exceed max weight")
        
        print(f"- Total weight = {totalWeight}, Total value = {totalValue}")


# Пример использования (можно удалить в рабочей версии):
if __name__ == "__main__":
    knapsack = Knapsack01Problem()
    randomSolution = np.random.randint(2, size=len(knapsack))
    print("Random Solution = ", randomSolution)
    print("Value = ", knapsack.getValue(randomSolution))
    print("Items:")
    knapsack.printItems(randomSolution)