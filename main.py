def create_student():
    name = input('What is the students name: ')
    student_data = {
        'name': name,
        'marks': []
    }

    return student_data


def add_mark(student, mark):
    student['marks'].append(mark)


def calculate_average_mark(student):
    total = sum(student['marks'])
    number = len(student['marks'])
    if number == 0:
        return 0
    return total / number


