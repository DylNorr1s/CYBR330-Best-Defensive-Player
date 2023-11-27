import csv
import classes
import time
import tracemalloc
# Dylan Norris, Matthew Adams, Ethan Terry
# Uses a sorted priority queue to find top and bottom 5 players for each stat
# Also uses it to find the best stats in each season (i.e., best in 2017 for possession and DRAYMOND,
# Best in 2018 for possession and DRAYMOND etc.)


def main():
    # Starts timer and memory tracker
    time_start = time.perf_counter()
    tracemalloc.start()

    # Creates Sorted Priority Queue object and assigns to variable
    spq = classes.SortedPriorityQueue()

    find_min_max(spq)
    sort_years(spq)

    # Prints (current, peak) memory usage in bytes
    print(tracemalloc.get_traced_memory())
    tracemalloc.stop()

    # Ends timer and prints final time
    time_end = time.perf_counter()
    print(f'{time_end - time_start:.5f} seconds')


def find_min_max(spq):
    # Csv sorts by season, player name, number of possessions a player played, and their DRAYMOND score
    # Draymond is the Defensive Rating Accounting for Yielding Minimal Openness by Nearest Defender
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
        key, row = spq.remove_end()
        print(f'Sorted row for max key {key} {row}')
    print('\n')

    # Finds bottom 5 lowest stats by column
    for x in range(5):
        key, row = spq.remove_min()
        print(f'Sorted row for min key {key} {row}')

    return key, row


def sort_years(spq):
    # Sorts top ten of a season based off the stat you originally sorted by
    search_year = input("\nDo you want to search by year?(y/n)").upper()
    if search_year == 'Y':
        year_to_search = input("Enter year to search: ")
        
        # Uses a pointer to find the right entries
        cursor = spq._data.last()
        printed_rows = 0
        while cursor is not None and printed_rows < 10:
            item = cursor.element()
            row = item._value
            # Checks if the first column is equal to right year and prints it
            if row[0] == year_to_search:
                print(row)
                printed_rows += 1
            cursor = spq._data.before(cursor)

    elif search_year == 'N':
        print("Okay")
    else:
        print("Invalid input")


if __name__ == '__main__':
    main()
