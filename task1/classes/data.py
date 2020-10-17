class Data:
    def __init__(self, data):
        self.data = data

    @property
    def s(self):
        return str(self.data)

    def get_data(self):
        return self.data

    def set_data(self, data):
        self.data = data