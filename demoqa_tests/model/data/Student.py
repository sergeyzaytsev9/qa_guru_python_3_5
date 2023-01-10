from dataclasses import dataclass
from datetime import date
from enum import Enum
import datetime
from typing import Literal, List


class Hobby(Enum):
    Music = 1,
    Reading = 2,
    Sports = 3


@dataclass
class Student:
    first_name: str
    last_name: str
    email: str
    phone: str
    address: str
    birthday: datetime.date
    gender: Literal['Male', 'Female', 'Other']
    subject: Literal['Maths', 'Accounting', 'Arts', 'Social Studies', 'English', 'Chemistry', 'Physics',
                     'Computer Science', 'Economics', 'History', 'Civics', 'Commerce', 'Biology', 'Hindi']
    hobby: List[Hobby]
    image: str
    state: Literal['NCR', 'Uttar Pradesh', 'Haryana', 'Rajasthan']
    city: Literal['Karnal', 'Panipat', 'Delhi', 'Gurgaon', 'Noida', 'Agra', 'Merrut', 'Lucknow', 'Jaipur', 'Jaiselmer']


test_zaytsev = Student(
    first_name='Sergey',
    last_name='Zaytsev',
    email='test@demoqa.com',
    phone='1234567890',
    address='Pushkina 8',
    birthday=date(1994, 5, 2),
    gender='Male',
    subject='Computer Science',
    hobby=[Hobby.Music, Hobby.Sports],
    image='Toolsqa.jpg',
    state='NCR',
    city='Delhi')
