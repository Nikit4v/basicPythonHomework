from main import Worker, Position

worker = Worker(
    name='SOME NAME',
    surname="SOME SURNAME",
    position="SOME POSITION",
    wage=10,
    bonus=20
)
print(worker)
print(Position.from_worker(worker).get_full_name())