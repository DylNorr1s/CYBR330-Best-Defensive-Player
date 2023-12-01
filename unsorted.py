import csv
import classes
import time
import tracemalloc


def main():
    uspq = classes.UnsortedPriorityQueue()
    find_min_max()


def find_min_max():
    time_start = time.perf_counter()
    csv_file = 'draymond.csv'
    column_index = int(input("Enter column to grab(0-3): "))

    with open(csv_file, 'r') as file:
        csv_reader = csv.reader(file)

        # Skips the header if there is one
        next(csv_reader, None)

        # Assigns rows to key variable, columns to value variable, and adds it to the sorted priority queue
        for row in csv_reader:
            key = row[column_index]
            value = tuple(row)
            spq.add(key, value)


if __name__ == '__main__':
    main()
