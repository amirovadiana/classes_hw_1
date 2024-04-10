list_of_students = []
list_of_lecturers = []

class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        list_of_students.append(self)

    def rate_lectures(self, lecturer, course, lectures_grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.lectures_grades:
                lecturer.lectures_grades[course] += [lectures_grade]
            else:
                lecturer.lectures_grades[course] = [lectures_grade]
        else:
            return 'Ошибка'

    def calculate_average(self):
        all_grades = []
        quantity_grades = 0
        if len(self.grades) == 0:
            return 0
        else:
            for grade in self.grades.values():
                all_grades.extend(grade)
                quantity_grades += 1
        return round(sum(all_grades) / len(all_grades))

    def __lt__(self, other):
        if (self.calculate_average()) > other.calculate_average():
            return True
        else:
            return False

    def __str__(self):
        return (f'Имя: {self.name}\n'
                f'Фамилия: {self.surname}\n'
                f'Средняя оценка за домашние задания: {round(self.calculate_average(), 2)}\n'
                f'Курсы в процессе изучения: {", ".join(self.courses_in_progress)}\n'
                f'Завершенные курсы: {", ".join(self.finished_courses)}')



class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.lectures_grades = {}
        self.lectures_course = []
        list_of_lecturers.append(self)

    def calculate_average(self):
        all_lectures_grades = []
        quantity_lectures_grades = 0
        if len(self.lectures_grades) == 0:
            return 0
        else:
            for lecture_grade in self.lectures_grades.values():
                all_lectures_grades.extend(lecture_grade)
                quantity_lectures_grades += 1
        return round(sum(all_lectures_grades) / len(all_lectures_grades))

    def __lt__(self, other):
        if (self.calculate_average()) > other.calculate_average():
            return True
        else:
            return False

    def __str__(self):
        return (f'Имя: {self.name} \n'
                f'Фамилия: {self.surname} \n'
                f'Средняя оценка за лекции: {self.calculate_average():.2f}')


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f'Имя: {self.name} \nФамилия: {self.surname}'


best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']
best_student.courses_in_progress += ['C++']
best_student.finished_courses += ['Java']

student_1 = Student('Eddy', 'Smith', 'Man')
student_1.courses_in_progress += ['Python']
student_1.courses_in_progress += ['Java']

student_2 = Student('Emma', 'Wotson', 'Female')
student_2.courses_in_progress += ['C++']
student_2.finished_courses += ['Python']

cool_lecturer = Lecturer('Sam', 'Green')
cool_lecturer.courses_attached += ['Python']
cool_lecturer.courses_attached += ['Java']

lecturer_1 = Lecturer('Jack', 'Black')
lecturer_1.courses_attached += ['Java']

lecturer_2 = Lecturer('Lora', 'Blue')
lecturer_2.courses_attached += ['C++']

cool_reviewer = Reviewer('Some', 'Buddy')
cool_reviewer.courses_attached += ['Python']

cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(student_1, 'Python', 10)
cool_reviewer.rate_hw(student_1, 'Python', 9)

reviewer_1 = Reviewer('Chak', 'Roth')
reviewer_1.rate_hw(best_student, 'Python', 10)
reviewer_1.rate_hw(best_student, 'Python', 10)
reviewer_1.rate_hw(student_1, 'Python', 9)
reviewer_1.rate_hw(student_1, 'Python', 10)
reviewer_1.rate_hw(student_1, 'Java', 9)
reviewer_1.rate_hw(student_1, 'Java', 8)

reviewer_2 = Reviewer('Bob', 'Steel')
reviewer_2.rate_hw(best_student, 'C++', 10)
reviewer_2.rate_hw(best_student, 'C++', 10)
reviewer_2.rate_hw(student_2, 'C++', 7)
reviewer_2.rate_hw(student_2, 'C++', 10)

best_student.rate_lectures(cool_lecturer, 'Python', 10)
best_student.rate_lectures(cool_lecturer, 'Python', 7)
best_student.rate_lectures(lecturer_2, 'C++', 9)
best_student.rate_lectures(lecturer_2, 'C++', 8)

student_1.rate_lectures(cool_lecturer, 'Python', 10)
student_1.rate_lectures(cool_lecturer, 'Python', 9)
student_1.rate_lectures(cool_lecturer, 'Java', 9)
student_1.rate_lectures(cool_lecturer, 'Java', 10)
student_1.rate_lectures(lecturer_1, 'Java', 10)
student_1.rate_lectures(lecturer_1, 'Java', 10)

student_2.rate_lectures(lecturer_2, 'C++', 7)
student_2.rate_lectures(lecturer_2, 'C++', 8)
student_2.rate_lectures(lecturer_2, 'C++', 8)

print(best_student.grades)
print(cool_lecturer.lectures_grades)

print(best_student)
print(student_1)
print(student_2)
print(cool_lecturer)
print(lecturer_1)
print(lecturer_2)
print(reviewer_1)
print(reviewer_2)

def calc_average_all_students(list_of_students, course):
    average_all_students = []
    quantity_students = 0
    medium = 0
    if len(list_of_students) == 0:
        return 'Error'
    else:
        for student in list_of_students, course:
            if isinstance(student, Student) and course in student.courses_in_progress:
                medium += student.calculate_average()
                quantity_students += 1
                if len(average_all_students) > 0:
                    return print(round(medium) / len(average_all_students))
                else:
                    return 'Error'

def calc_average_all_lecturers(list_of_lecturers, course):
    average_all_lecturers = []
    quantity_lecturers = 0
    medium = 0
    if len(list_of_lecturers) == 0:
        return 'Error'
    else:
        for lecturer in list_of_lecturers, course:
            if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached:
                medium += lecturer.calculate_average()
                quantity_lecturers += 1
                if len(average_all_lecturers) > 0:
                    return print(round(medium) / len(average_all_lecturers))
                else:
                    return 'Error'


print(best_student > student_1)
print(student_1 > student_2)
print(cool_lecturer > lecturer_2)

print(best_student.calculate_average())
print(student_1.calculate_average())
print(student_2.calculate_average())
print(cool_lecturer.calculate_average())
print(lecturer_1.calculate_average())
print(lecturer_2.calculate_average())
calc_average_all_students([best_student, student_1], 'Python')
calc_average_all_lecturers([cool_lecturer, lecturer_1], 'Java')
