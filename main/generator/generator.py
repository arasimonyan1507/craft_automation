from main.data.data import Person, RegistrationForm, StudentRegistrationForm
from faker import Faker
from pathlib import Path
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


def generated_file():
    file_path = r"C:/Users/araga/PycharmProjects/craft_automation/main/generator/generated_file.txt"
    path = Path(file_path)
    with open(path, "w") as new_generated_file:
        new_generated_file.write(f"Random integer is equal to {random.randint}")
    file_name = path.name
    return file_name, file_path


def generated_student_registration_form():
    yield StudentRegistrationForm(
        first_name=fake_data.name().split()[0],
        last_name=fake_data.name().split()[1],
        email=fake_data.email(),
        phone_number=fake_data.msisdn()
    )


def generated_subject_set(amount=random.randint(1, 14)):
    all_subject_list = ["Hindi", "English", "Maths", "Physics", "Chemistry", "Biology", "Computer Science", "Commerce",
                        "Accounting", "Economics", "Arts", "Social Studies", "History", "Civics"]
    new_set = set()
    while amount:
        new_set.add(all_subject_list[random.randint(0, len(all_subject_list)-1)])
        amount -= 1
    return new_set

