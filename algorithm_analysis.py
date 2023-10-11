import csv
from operator import itemgetter   
from time import perf_counter_ns

class Algorithm_Analysis:
    def __init__(self, data) -> None:
        self.data = data
        self.headers = self.data.pop(0)
        self.sorted_data = sorted(self.data, key=itemgetter(4))
    
    def linear_search(self, value):
        count = 0
        for i in range(len(self.data)):
            count += int(value == self.data[i][2] or value == self.data[i][3])
        return count

    def binary_search(self):
        return 2

    def analysis(self, runs):
        linear_times = 0
        binary_times = 0
        for run in range(runs):
            linear_start = perf_counter_ns()
            count = self.linear_search("Poison")
            linear_stop = perf_counter_ns()
            linear_time = linear_stop - linear_start
            linear_times += linear_time
            binary_start = perf_counter_ns()
            maxes = self.binary_search()
            binary_stop = perf_counter_ns()
            binary_time = binary_stop - binary_start
            binary_times += binary_time
            self.display(run, linear_time, count, binary_time, maxes)


            

    def display(self, run, linear_time, count, binary_time, maxes):
        print(f"""
Starting linear problem solution: {run}
Time taken: {linear_time} nanoseconds 
Frequency of Poison found:  {count}
Starting binary problem solution: {run}
Time taken: {binary_time} nanoseconds 
Key / Value Maximums: {maxes}
""")



if __name__ == "__main__":

    with open('Pokemon_numerical.csv', newline='') as csvfile:
        reader = csv.reader(csvfile)
        data = list(reader)
        test = Algorithm_Analysis(data)
        test.linear_search("Poison")
        test.analysis(5)
    
