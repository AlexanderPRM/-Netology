class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
    def rate_lecture(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.lectur_grades:
                lecturer.lectur_grades[course] += grade
            else:
                lecturer.lectur_grades[course] = grade
        else:
            print('Ошибка')
    def value(self):
        count = 0
        if self.grades:
            for el in self.grades:
                count += sum(self.grades[el])
                return count
        else:
            return 'Ошибка'
    def values_len(self):
        count = 0
        if self.grades:
            for el in self.grades.values():
                if len(el) > 1:
                    for num in el:
                        count += 1
                else:
                    count += 1
            return count
        else:
            return 'Ошибка'
    def middle_grade(self):
        mid_grade = self.value() / self.values_len()
        return mid_grade

    def progress_courses(self):
        res = ', '.join(self.courses_in_progress)
        return res
    def finished_cours(self):
        res = ', '.join(self.finished_courses)
        return res
    def __str__(self):
        res = f'''
Имя: {self.name}
Фамилия: {self.surname}
Средняя оценка за домашние задания: {self.middle_grade()}
Курсы в процессе изучения: {self.progress_courses()}
Завершенные курсы: {self.finished_cours()}'''
        return res
    def __lt__(self, arg):
        if isinstance(arg, Student):
            return self.middle_grade() > arg.middle_grade()
        else:
            print(f'{arg} не является студентом')




class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.lectur_grades = {}
    def middle_grade(self):
        if self.lectur_grades == True:
            mid_grade = sum(self.lectur_grades.values()) / len(self.lectur_grades)
            return mid_grade
        else:
            return 'Нет оценок'
    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.middle_grade()}'
        return res
    def __lt__(self, arg):
        if isinstance(arg, Lecturer):
            return self.middle_grade() > arg.middle_grade()
        else:
            print(f'{arg} не является лектором')

class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'
    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}'
        return res


def main_middle_grade_students(list_student, course):
    count = 0
    for student in list_student:
        if isinstance(student, Student) and course in student.courses_in_progress:
            for courses in student.grades:
                if course == courses:
                    count += sum(student.grades[courses])
    return count

def main_middle_grade_lecturers(list_lecturer, course):
    count = 0
    for lectur in list_lecturer:
        if isinstance(lectur, Lecturer) and course in lectur.courses_attached:
            for courses in lectur.lectur_grades:
                if course == courses:
                    count += sum(lectur.lectur_grades[courses])
    return count


# Проверки
student_alex = Student('Alexander', 'Volkov', 'man')
student_masha = Student('Maria', 'Borodina', 'woman')

student_alex.courses_in_progress += ['C++']
student_masha.courses_in_progress += ['C#']
student_masha.courses_in_progress += ['C++']

cool_mentor = Reviewer('Oleg', 'Petrov')
very_cool_lecture  = Lecturer('Vladimir', 'Mask')
very_cool_lecture_two  = Lecturer('Petya', 'Petrovich')

cool_mentor.courses_attached += ['C++', 'C#']

cool_mentor.rate_hw(student_alex, 'C++', 10)
cool_mentor.rate_hw(student_masha, 'C#', 10)
cool_mentor.rate_hw(student_alex, 'C++', 10)
cool_mentor.rate_hw(student_masha, 'C++', 10)

print(student_alex)
print(student_masha, '\n')
print(cool_mentor, '\n')
print(very_cool_lecture, '\n')
print(very_cool_lecture > very_cool_lecture_two)
print(student_alex > student_masha)
print(main_middle_grade_students([student_masha, student_alex], 'C++'))
print(main_middle_grade_lecturers([very_cool_lecture_two, very_cool_lecture], 'C++'))