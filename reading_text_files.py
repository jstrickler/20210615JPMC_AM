x = 5

def read_without_with():
    mary_in = open('DATA/mary.txt')
    print(mary_in)
    mary_in.close()

def read_by_line():
    with open('DATA/mary.txt') as mary_in:
        for raw_line in mary_in:  # mary_in.readline()
            line = raw_line.rstrip()
            print(line)
    print("-" * 60)

def read_entire_file():
    with open('DATA/mary.txt') as mary_in:
        entire_file = mary_in.read()
        print("RAW:")
        print(repr(entire_file))
        print("COOKED:")
        print(entire_file)
    print("-" * 60)

def read_into_list_with_nl():
    with open('DATA/mary.txt') as mary_in:
        all_lines_with_nl = mary_in.readlines()
        print(all_lines_with_nl)
    print("-" * 60)

def read_into_list_without_nl():
    with open('DATA/mary.txt') as mary_in:
        all_lines_without_nl = [line.rstrip() for line in mary_in]
        print(all_lines_without_nl)
    print("-" * 60)

def count_rabbits():
    count = 0
    with open("DATA/alice.txt") as alice_in:
        for raw_line in alice_in:
            if "alice" in raw_line.lower():
                count += 1
    print("count is", count)
    # OR...
    with open("DATA/alice.txt") as alice_in:
        entire_file = alice_in.read()
        rabbit_count = entire_file.lower().count('alice')
        print("new count is", rabbit_count)


read_without_with()
read_by_line()
read_entire_file()
read_into_list_with_nl()
read_into_list_without_nl()
count_rabbits()
