# #ДЗ 14.1. Виняток користувача
# class GroupLimit(Exception):
#     def __init__(self, max_students):
#         super().__init__(f"Group limit {max_students} exceeded.")
#
# class Human:
#
#     def __init__(self, gender, age, first_name, last_name):
#         self.gender = gender
#         self.age = age
#         self.first_name = first_name
#         self.last_name = last_name
#
#     def __str__(self):
#         return f"{self.first_name.title()} {self.last_name.title()} {self.gender} {self.age}"
#
# class Student(Human):
#
#     def __init__(self, gender, age, first_name, last_name, record_book):
#         super().__init__(gender, age, first_name, last_name)
#         self.record_book = record_book
#
#     def __str__(self):
#         return super().__str__() + f"{self.record_book}"
#
# class Group:
#
#     def __init__(self, number, max_students = 10):
#         self.number = number
#         self.group = set()
#         self.max_students = max_students
#
#
#     def add_student(self, student):
#         if len(self.group) > self.max_students:
#             raise GroupLimit(self.max_students)
#         self.group.add(student)
#
#
#     def delete_student(self, last_name):
#        for student in self.group.copy():
#         if student.last_name == last_name:
#             self.group.remove(student)
#         else:
#             return f"Not found {last_name}"
#
#     def find_student(self, last_name):
#         for student in self.group:
#             if student.last_name == last_name:
#                 return student
#         return None
#
#     def __str__(self):
#         all_students = ''
#         for student in self.group:
#          all_students += student.__str__()+ "\n"
#         return f'Number:{self.number}\\n {all_students} '
#
# st1 = Student('Male', 30, 'Steve', 'Jobs', 'AN142')
# st2 = Student('Female', 25, 'Liza', 'Taylor', 'AN145')
# gr = Group('PD1')
# gr.add_student(st1)
# gr.add_student(st2)
# print(gr)
# assert str(gr.find_student('Jobs')) == str(st1), 'Test1'
# assert gr.find_student('Jobs2') is None, 'Test2'
# assert isinstance(gr.find_student('Jobs'), Student) is True, 'Метод поиска должен возвращать экземпляр'
#
# gr.delete_student('Taylor')
# print(gr)  # Only one student
#
# gr.delete_student('Taylor')  # No error!