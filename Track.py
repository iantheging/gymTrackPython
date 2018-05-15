from entry import Entry


class Track:

    def __init__(self):
        self.entrylist = []

    def read_from_file(self, filename):
        with open(filename, "r") as f:
            data = f.readlines()
            for line in data:
                info = line.split()
                e = Entry(info[0], info[1], info[2], info[3], info[4])
                self.entrylist.append(e)

    def write_to_file(self, filename):
        f = open(filename, "w+")
        for e in self.entrylist:
            f.write(e.raw_string())

    def add(self, e):
        self.entrylist.append(e)