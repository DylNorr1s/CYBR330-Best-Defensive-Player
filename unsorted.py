import csv
import classes
import time
import tracemalloc


def main():
    tracemalloc.start()
    uspq = classes.UnsortedPriorityQueue()
    column_index = int(input("Enter column to grab(0-3): "))
    find_min_max(uspq, column_index)
    sort_years(uspq, column_index)

    print(tracemalloc.get_traced_memory())
    tracemalloc.stop()


def find_min_max(uspq, column_index):
    csv_file = 'draymond.csv'
    time_start = time.perf_counter()
    
    with open(csv_file, 'r') as file:
        csv_reader = csv.reader(file)

        # Skips the header if there is one
        next(csv_reader, None)

        # Assigns rows to key variable, columns to value variable, and adds it to the unsorted priority queue
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


def sort_years(uspq, column_index):
    # Sorts top ten of a season
    search_year = input("\nDo you want to search by year?(y/n)").upper()

    time_start = time.perf_counter()
    if search_year == 'Y':
        year_to_search = input("Enter year to search: ")
        # Sorts items in the dataset based on a custom key function, lambda, which returns a tuple,
        # Which serves as the sorting key
        sorted_items = sorted(uspq._data, key=lambda item: (item._value[0] == year_to_search,
                                                            float(item._value[column_index])), reverse=True)

        # Iterates through the sorted items, prints them accordingly
        printed_rows = 0
        for item in sorted_items:
            row = item._value
            print(row)
            printed_rows += 1
            if printed_rows >= 10:
                break

    elif search_year == 'N':
        print("Okay")
    else:
        print("Invalid input")

    time_end = time.perf_counter()
    print(f'{time_end - time_start:.5f} seconds to sort by year')


if __name__ == '__main__':
    main()
