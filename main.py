import csv
import classes
import time
import tracemalloc
# Uses a sorted priority queue to find top and bottom ten players for each stat
# Also uses it to find the best stat in each season (i.e., best in 2017 for possession and DRAYMOND,
# Best in 2018 for possession and DRAYMOND etc.)


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
    for x in range(5):
        key, row = spq.remove_end()
        print(f'Sorted row for max key {key} {row}')
    print('\n')

    # Finds bottom ten lowest stats by column
    for x in range(5):
        key, row = spq.remove_min()
        print(f'Sorted row for min key {key} {row}')

    # Sort by years
    search_year = input("\nDo you want to search by year?(y/n)").upper()
    if search_year == 'Y':
        year_to_search = input("Enter year to search: ")
        cursor = spq._data.last()

        printed_rows = 0
        while cursor is not None and printed_rows < 10:
            item = cursor.element()
            row = item._value
            if row[0] == year_to_search:
                print(row)
                printed_rows += 1
            cursor = spq._data.before(cursor)

    elif search_year == 'N':
        print("Okay")

    time_end = time.perf_counter()
    print(f'{time_end - time_start:.5f} seconds')


if __name__ == '__main__':
    main()
