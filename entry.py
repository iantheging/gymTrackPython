class Entry:
    def __init__(self, m, d, a, w, c):
        self.month = m
        self.day = d
        self.activity = a
        self.weight = w
        self.count = c

    def to_string(self):
        return "Date: " + str(self.month) + "/" + str(self.day) + " Activity: " + self.activity + " Length: " + \
               str(self.count) + " Weight: " + str(self.weight) + "\n"

    def raw_string(self):
        return str(self.month) + " " + str(self.day) + " " + str(self.activity) + " " + str(self.count) + " " + \
               str(self.weight) + "\n"
