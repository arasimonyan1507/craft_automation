from selenium.webdriver.support.color import Color

from main.data.data import Person, RegistrationForm, StudentRegistrationForm, Date
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
        new_set.add(all_subject_list[random.randint(0, len(all_subject_list) - 1)])
        amount -= 1
    return new_set


def generated_color():
    return ["Red", "Blue", "Green", "Yellow", "Purple", "Black", "White", "Voilet", "Indigo", "Magenta", "Aqua"]


def generated_date():
    yield Date(
        day=str(random.randint(1, 30)),
        month=fake_data.month_name(),
        year=str(fake_data.date_between(1900, 2100)).split("-")[0],
        time=random.sample(
            ['00:00', '00:15', '00:30', '00:45', '01:00', '01:15', '01:30', '01:45', '02:00', '02:15', '02:30', '02:45',
             '03:00', '03:15', '03:30', '03:45', '04:00', '04:15', '04:30', '04:45', '05:00', '05:15', '05:30', '05:45',
             '06:00', '06:15', '06:30', '06:45', '07:00', '07:15', '07:30', '07:45', '08:00', '08:15', '08:30', '08:45',
             '09:00', '09:15', '09:30', '09:45', '10:00', '10:15', '10:30', '10:45', '11:00', '11:15', '11:30', '11:45',
             '12:00', '12:15', '12:30', '12:45', '13:00', '13:15', '13:30', '13:45', '14:00', '14:15', '14:30', '14:45',
             '15:00', '15:15', '15:30', '15:45', '16:00', '16:15', '16:30', '16:45', '17:00', '17:15', '17:30', '17:45',
             '18:00', '18:15', '18:30', '18:45', '19:00', '19:15', '19:30', '19:45', '20:00', '20:15', '20:30', '20:45',
             '21:00', '21:15', '21:30', '21:45', '22:00', '22:15', '22:30', '22:45', '23:00', '23:15', '23:30',
             '23:45'], 1))


def generated_color_for_old_style():
    colors = ["Red", "Blue", "Green", "Yellow", "Purple", "Black", "White", "Voilet", "Indigo", "Magenta", "Aqua"]
    return colors[random.randint(0, len(colors) - 1)]


def generated_car():
    cars = ["Volvo", "Saab", "Opel", "Audi"]
    return cars[random.randint(0, len(cars)-1)]

