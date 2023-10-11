import csv
from operator import itemgetter   

class Algorithm_Analysis:
    def __init__(self, data) -> None:
        self.data = data
        self.headers = self.data.pop(0)
        self.sorted_data = sorted(self.data, key=itemgetter(4))
    
    def linear_search(self, value: str):
        count = 0
        for i in range(len(self.data)):
            count += int(value == self.data[i][2] or value == self.data[i][3])
        print(count)
        return count





if __name__ == "__main__":

    with open('Pokemon_numerical.csv', newline='') as csvfile:
        reader = csv.reader(csvfile)
        data = list(reader)
        test = Algorithm_Analysis(data)
        test.linear_search("Poison")
    