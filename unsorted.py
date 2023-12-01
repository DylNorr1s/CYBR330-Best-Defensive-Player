import csv
import classes
import time
import tracemalloc


def main():
    uspq = classes.UnsortedPriorityQueue()
    find_min_max(uspq)


def find_min_max(uspq):
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


# Finds top 5 highest stats by column
    for x in range(5):
        key, row = uspq.remove_end()
        print(f'Sorted row for max key {key} {row}')
    print('\n')

    # Finds bottom 5 lowest stats by column
    for x in range(5):
        key, row = uspq.remove_min()
        print(f'Sorted row for min key {key} {row}')

    time_end = time.perf_counter()
    print(f'{time_end - time_start:.5f} seconds to sort min/max')
    return key, row


if __name__ == '__main__':
    main()
