class Table:
    def __init__(self):
        self.length = 0
        self.size = 0
        self.T = []

    def _expand(self):
        if self.size == 0:
            self.T = [None] * 1
            self.size = 1
        else:
            new_size = self.size * 2
            new_table = [None] * new_size
            for i in range(0, self.size):
                new_table[i] = self.T[i]
            self.T = new_table
            self.size = new_size

    def _shrink(self):
        new_size = int(self.size * 3 / 4)
        new_table = [None] * new_size
        for i in range(0, new_size):
            new_table[i] = self.T[i]
        self.T = new_table
        self.size = new_size

    def insert(self, x):
        if self.length == self.size:
            self._expand()
        self.T[self.length] = x
        self.length += 1
