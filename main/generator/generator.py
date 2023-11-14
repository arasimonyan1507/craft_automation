from main.data.data import Person, RegistrationForm
from faker import Faker
import random

fake_data = Faker()
# fake.seed()


def generated_person():
    yield Person(
        full_name=fake_data.name(),
        email=fake_data.email(),
        current_address=fake_data.address(),
        permanent_address=fake_data.address()
    )


def generated_registration_form():
    yield RegistrationForm(
        first_name=fake_data.name().split()[0],
        last_name=fake_data.name().split()[1],
        email=fake_data.email(),
        age=random.randint(1, 10),
        salary=random.randint(1000, 10000),
        department=fake_data.company()

    )
