from dataclasses import dataclass


@dataclass
class Person:
    full_name: str = None
    email: str = None
    current_address: str = None
    permanent_address: str = None


@dataclass
class RegistrationForm:
    first_name: str = None
    last_name: str = None
    email: str = None
    age: int = None
    salary: int = None
    department: str = None


@dataclass
class StudentRegistrationForm:
    first_name: str = None
    last_name: str = None
    email: str = None
    phone_number: str = None


@dataclass
class Date:
    day: str = None
    month: str = None
    year: str = None
    time: str = None
