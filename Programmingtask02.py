import csv
import crimelist
import numpy

my_file = 'crime.csv'


def import_data(delimited_file):
    with open(delimited_file, 'rb') as csvfile:
        all_data = list(csv.reader(csvfile, delimiter=','))
    return all_data


def seperate_headings_from_data(data):
    headings = data[0]
    data.pop(0)
    print crimelist.DataFrame(data, columns=headings)
    

def get_basic_stats(data):
    murder = []
    for assault in data:
        murder.append(float(assault[1]))
    return murder




def get_state(assault, min_max, data):
    state = []
    min_index = assault.index(min_max[0])
    max_index = assault.index(min_max[1])
    for assault in data:
        state.append(assault[0])
    return state[min_index], state[max_index]

if __name__ == '__main__':
    data = import_data(my_file)
    seperate_headings_from_data(data)
    min_max = calculate_min_and_max(murder)
    states = get_state(murder, min_max, data)
    print "\n assault  Statistics"
    print "-----------------"
    print "Mean: {}".format((stats)[0])
    print "Median: {}".format((stats)[1])
    print "Std. Deviation: {}".format((stats)[2])
    print "Highest crime rate: {} with a rate of {}".format(
        (states)[0], (min_max)[0])
    print "Lowest crime rate: {} with a rate of {}".format(
        (states)[1], (min_max)[1])
