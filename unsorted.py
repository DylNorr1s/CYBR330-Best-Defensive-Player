import csv
import classes
import time
import tracemalloc


def main():
    uspq = classes.UnsortedPriorityQueue()
    find_min_max(uspq)
    sort_years(uspq)


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
            uspq.add(key, value)


# Finds top 5 highest stats by column
    for x in range(5):
        key, row = uspq.remove_max()
        print(f'Sorted row for max key {key} {row}')
    print('\n')

    # Finds bottom 5 lowest stats by column
    for x in range(5):
        key, row = uspq.remove_min()
        print(f'Sorted row for min key {key} {row}')

    time_end = time.perf_counter()
    print(f'{time_end - time_start:.5f} seconds to sort min/max')
    return key, row


def sort_years(uspq):
    # Sorts top ten of a season based off the stat you originally sorted by
    search_year = input("\nDo you want to search by year?(y/n)").upper()

    time_start = time.perf_counter()
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

    time_end = time.perf_counter()
    print(f'{time_end - time_start:.5f} seconds to sort by year')


if __name__ == '__main__':
    main()
