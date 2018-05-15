from Track import Track
from entry import Entry

entry_list = []


def add_to_track(filename):
    while True:
        m = input("Enter Month: ")
        d = input("Enter Day: ")
        a = input("Enter Activity: ")
        w = input("Enter weight: ")
        c = input("Enter count: ")
        e = Entry(m, d, a, w, c)
        entry_list.append(e)
        print("Enter c to add another entry, any other number to exit")
        userexit = input("User Choice: ")
        if userexit is not "c":
            break
    write_to_file(filename)


def read_from_file(filename):
    with open(filename, "r") as f:
        data = f.readlines()
        for line in data:
            info = line.split()
            e = Entry(info[0], info[1], info[2], info[3], info[4])
            entry_list.append(e)


def write_to_file(filename):
    f = open(filename, "w+")
    for e in entry_list:
        f.write(e.raw_string())


while True:
    print(
        "Please select a choice\nn: Enter in information manually\ni: Read in from an existing file\n"
        "Any other number: Exit the program")
    userChoice = input("User Choice: ")

    if userChoice is "n":
        f = input("Name for new file: ")
        add_to_track(f)
    elif userChoice is "i":
        f = input("File name: ")
        read_from_file(f)
        add_to_track(f)
    else:
        print("File additions complete")
        break
