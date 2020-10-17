class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {
            "wage": wage,
            "bonus": bonus
        }


class Position(Worker):
    @staticmethod
    def from_worker(worker: Worker):
        self = Position(worker.name, worker.surname, worker.position, worker._income["wage"], worker._income["bonus"])
        return self

    def get_full_name(self):
        return f"{self.name} {self.surname}"

    def get_total_incomes(self):
        return self._income["wage"] + self._income["bonus"]