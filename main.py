import csv
import classes
import time
import tracemalloc
# Uses a sorted priority queue to find top and bottom ten players for each stat
# Also uses it to find the best stat in each season (i.e., best in 2017 for possession and DRAYMOND,
# Best in 2018 for possession and DRAYMOND etc.) We need to add that part still


def main():
    tracemalloc.start()
    find_min_max()

    # Prints (current, peak) memory usage in bytes
    print(tracemalloc.get_traced_memory())
    tracemalloc.stop()


def find_min_max():
    # Csv sorts by season, player name, number of possessions a player played, and their DRAYMOND score
    # Draymond is the Defensive Rating Accounting for Yielding Minimal Openness by Nearest Defender
    csv_file = 'draymond.csv'
    column_index = int(input("Enter column to grab(0-3): "))
    time_start = time.perf_counter()
    spq = classes.SortedPriorityQueue()

    with open(csv_file, 'r') as file:
        csv_reader = csv.reader(file)

        # Skips the header if there is one
        next(csv_reader, None)

        for row in csv_reader:
            key = row[column_index]
            value = tuple(row)
            spq.add(key, value)

    # Finds top ten highest stats by column
    for x in range(10):
        key, row = spq.remove_end()
        print(f'Sorted row for max key {key} {row}')
    print('\n')

    # Finds bottom ten lowest stats by column
    for x in range(10):
        key, row = spq.remove_min()
        print(f'Sorted row for min key {key} {row}')
    time_end = time.perf_counter()
    print(f'{time_end - time_start:.5f} seconds')


if __name__ == '__main__':
    main()
