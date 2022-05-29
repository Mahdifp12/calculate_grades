import os
from sys import platform

import termcolor

list_of_number_grades = []
list_of_g = []


def clear_screen():

    if platform in ["linux", "linux2", "darwin"]:
        os.system("clear")

    elif platform == "win32":
        os.system("cls")


clear_screen()


def print_first_time_run():

    print(termcolor.colored('        <--- Current Grades --->        ',
            'red', 'on_grey',
        attrs=['reverse', 'blink', 'bold']))

    print(termcolor.colored('\nGrades:\n', color='blue',
    attrs= ['reverse', 'bold']))


print_first_time_run()


def first_read_file():

    with open('grades.txt', 'r') as grades_reader:
        all_data = grades_reader.read()
        print(termcolor.colored(all_data, 'green'))


first_read_file()


def check_input(list_of_grade):
    while True:

        yes_or_no_grade = input(
            'Do you want add more grade (y:yes n:no)?: ').lower()

        if yes_or_no_grade == 'n':
            return

        if yes_or_no_grade == 'y':

            while yes_or_no_grade == 'y':
                name = input('Enter name: ')
                grade = input('Enter grade: ')

                if yes_or_no_grade == 'n':
                    return

                try:
                    list_of_grade.append({
                        'name': name,
                        'grade': int(grade)
                    })
                except ValueError:

                    try:
                        list_of_grade.append({
                            'name': name,
                            'grade': float(grade)
                        })

                    except ValueError as e:
                        print(termcolor.colored(
                            f'Error : {e}', 'red', attrs=['bold']))

                yes_or_no_grade = input(
                    'Do you want add more grade (y:yes n:no)?: ').lower()

            else:
                return list_of_grade

        else:
            print(termcolor.colored('your Input Invalid! Try Agin.',
                                    'red', attrs=['bold']))


last_of_list_grade = check_input(list_of_g)


def append_in_file(list_of_grades):

    with open('grades.txt', 'a') as grades_file:
        for data in list_of_grades:
            grades_file.write(f"\n{data['name']} {data['grade']}")


try:
    append_in_file(last_of_list_grade)

except TypeError as e:
    print('Do you not add more grade !')


def second_read_file(list_of_number_grades):

    with open('grades.txt', 'r') as grades_reader:
        grades_data = grades_reader.read().split('\n')

        for line in grades_data:
            grade = line.split(' ')[1]

            try:
                list_of_number_grades.append(int(grade))

            except ValueError:

                try:
                    list_of_number_grades.append(float(grade))

                except ValueError as e:
                    print(termcolor.colored(
                        f'your grade invalid : {e}', 'red', attrs=['bold']))

        return list_of_number_grades


numbers_of_average = second_read_file(list_of_number_grades)

print(f'Average: {sum(numbers_of_average) / len(numbers_of_average)}')
