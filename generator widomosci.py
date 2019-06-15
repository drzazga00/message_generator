message = "Hi {},\n\nThis is a reminder that you have {} tasks left to \
submit before you can graduate. You're current grade is {} and can increase \
to {} if you submit all assignments before the due date.\n\n"


##with open('message.txt', 'r') as mess:
##    message = mess.readlines()

def choice_class(num_of_class):
    file = num_of_class + '.txt'
    print(file)
    with open(file, 'r') as name:
        students_from_file = name.readlines()

    def make_student_dict(person):
        person = person.split()
        student_dict = {
            'name' : person[0],
            'tasks' : person[1],
            'grades' : person[2]
            }
        return student_dict


    list_students = []
    def add_student(counter):
        list_students.append(make_student_dict(students_from_file[counter]))



    for i in range(28):
        add_student(i)
        prob = int(list_students[i]['grades'])
        print(message.format(list_students[i]['name'], list_students[i]['tasks'], list_students[i]['grades'], prob + 1))
