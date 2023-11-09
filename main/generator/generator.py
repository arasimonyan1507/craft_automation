from main.data.data import Person
from faker import Faker

fake_data = Faker()
# fake.seed()


def generated_person():
    yield Person(
        full_name=fake_data.name(),
        email=fake_data.email(),
        current_address=fake_data.address(),
        permanent_address=fake_data.address()
    )
