class Stationary:
    title = None

    def draw(self):
        print("Запуск отприсовки.")


class Pen(Stationary):
    def draw(self):
        print("Pen")


class Pencil(Stationary):
    def draw(self):
        print("Pencil")


class Handle(Stationary):
    def draw(self):
        print("Handle")