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
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def find_average_grade(self):
        sum_ = 0
        quantity = 0
        for list_ in self.grades.values():
            sum_ += sum(list_)
            quantity += len(list_)
        if quantity == 0:
            result = "нет оценок"
        else:
            result = round(sum_/quantity, 1)
        return result

    def __str__(self):
        str_courses_in_progress = ", ".join(self.courses_in_progress)
        str_finished_courses = ", ".join(self.finished_courses)
        message = (
            f"Имя: {self.name}\n"
            f"Фамилия: {self.surname}\n"
            f"Средняя оценка за домашние задания: {self.find_average_grade()}\n"
            f"Курсы в процессе изучения: {str_courses_in_progress}\n"
            f"Завершенные курсы: {str_finished_courses}\n"
        )
        return message

    def __lt__(self, other):
        if not isinstance(other, Student):
            print("Не студент")
            return
        return self.find_average_grade() < other.find_average_grade()


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def find_average_grade(self):
        sum_ = 0
        quantity = 0
        for list_ in self.grades.values():
            sum_ += sum(list_)
            quantity += len(list_)
        if quantity == 0:
            result = "нет оценок"
        else:
            result = round(sum_/quantity, 1)
        return result

    def __str__(self):
        message = (
            f"Имя: {self.name}\n"
            f"Фамилия: {self.surname}\n"
            f"Средняя оценка за лекции: {self.find_average_grade()}\n"
        )
        return message

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print("Не лектор")
            return
        return self.find_average_grade() < other.find_average_grade()


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
        message = (
            f"Имя: {self.name}\n"
            f"Фамилия: {self.surname}\n"
        )
        return message


def find_average_student_grade(selected_course, list_):
    course = selected_course
    student_list = list_
    sum_ = 0
    quantity = 0
    for student in student_list:
        if not isinstance(student, Student):
            return "Ошибка"
        sum_ += sum(student.grades.get(course, [0]))
        if course in student.grades:
            quantity += len(student.grades.get(course))
    if quantity == 0:
        result = 0
    else:
        result = round(sum_ / quantity, 1)
    return result


def find_average_lecturer_grade(selected_course, list_):
    course = selected_course
    lecturer_list = list_
    sum_ = 0
    quantity = 0
    for lecturer in lecturer_list:
        if not isinstance(lecturer, Lecturer):
            return "Ошибка"
        sum_ += sum(lecturer.grades.get(course, [0]))
        if course in lecturer.grades:
            quantity += len(lecturer.grades.get(course))
    if quantity == 0:
        result = 0
    else:
        result = round(sum_ / quantity, 1)
    return result


best_student = Student('Чак', 'Норрис', 'мужчина')
worst_student = Student('Александр', 'Biglove', 'мужчина')

cool_lecturer = Lecturer('Ганнибал', 'Барка')
warm_lecturer = Lecturer('Доктор', 'Попов')

cool_reviewer = Reviewer('Жерар', 'Депардье')
warm_reviewer = Reviewer('Волк', 'Залдостанов')

best_student.courses_in_progress += ['Python', 'Git', 'Приседания с ДЗ']
worst_student.courses_in_progress += ['Приседания с ДЗ']

cool_lecturer.courses_attached += ['Python', 'Git', 'Приседания с ДЗ']
warm_lecturer.courses_attached += ['Приседания с ДЗ']

cool_reviewer.courses_attached += ['Python', 'Git', 'Приседания с ДЗ']
warm_reviewer.courses_attached += ['Приседания с ДЗ']

cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 8)
cool_reviewer.rate_hw(best_student, 'Python', 7)

warm_reviewer.rate_hw(worst_student, 'Приседания с ДЗ', 5)
warm_reviewer.rate_hw(worst_student, 'Приседания с ДЗ', 1)
warm_reviewer.rate_hw(worst_student, 'Приседания с ДЗ', 2)

best_student.rate_lecture(cool_lecturer, 'Python', 8)
best_student.rate_lecture(cool_lecturer, 'Python', 9)
best_student.rate_lecture(cool_lecturer, 'Python', 10)

worst_student.rate_lecture(warm_lecturer, 'Приседания с ДЗ', 1)
worst_student.rate_lecture(warm_lecturer, 'Приседания с ДЗ', 2)
worst_student.rate_lecture(warm_lecturer, 'Приседания с ДЗ', 1)

print(best_student)
print(worst_student)
print('best_student < worst_student: ', best_student < worst_student)
print()

print(cool_lecturer)
print(warm_lecturer)
print('cool_lecturer > warm_lecturer: ', cool_lecturer > warm_lecturer)
print()

print('Средняя оценка у студентов по Python: ', find_average_student_grade('Python', [best_student, worst_student]))
print('Средняя оценка у лекторов по приседам с ДЗ: ', find_average_lecturer_grade('Приседания с ДЗ',
                                                                                  [cool_lecturer, warm_lecturer]))
