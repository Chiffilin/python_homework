from student import Student
from group import Group

from custom_exceptions import GroupLimitError

st1 = Student('Male', 30, 'Steve', 'Jobs', 'AN142')
st2 = Student('Female', 25, 'Liza', 'Taylor', 'AN145')
st3 = Student('Male', 22, 'Mark', 'Zuckerberg', 'AN146')
st4 = Student('Male', 24, 'Bill', 'Gates', 'AN147')
st5 = Student('Female', 23, 'Ada', 'Lovelace', 'AN148')
st6 = Student('Male', 27, 'Alan', 'Turing', 'AN149')
st7 = Student('Female', 26, 'Grace', 'Hopper', 'AN150')
st8 = Student('Male', 29, 'Larry', 'Page', 'AN151')
st9 = Student('Male', 28, 'Sergey', 'Brin', 'AN152')
st10 = Student('Female', 25, 'Marissa', 'Mayer', 'AN153')
st11 = Student('Male', 31, 'Elon', 'Musk', 'AN154')


gr = Group('PD1')
try:
    gr.add_student(st1)
    gr.add_student(st2)
    gr.add_student(st3)
    gr.add_student(st4)
    gr.add_student(st5)
    gr.add_student(st6)
    gr.add_student(st7)
    gr.add_student(st8)
    gr.add_student(st9)
    gr.add_student(st10)
    # Attempting to add the 11th student
    gr.add_student(st11)
except GroupLimitError as e:
    print(f"Error: {e}\n")

print(gr)

print("\nІнші тести\n")
assert str(gr.find_student('Jobs')) == str(st1), 'Test1'
assert gr.find_student('Jobs2') is None, 'Test2'
assert isinstance(gr.find_student('Jobs'), Student) is True, 'Метод поиска должен возвращать экземпляр'

gr.delete_student('Taylor')
print(gr)  # Only one student

gr.delete_student('Taylor')  # No error!
