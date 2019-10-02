from all_lessons import *
from datetime import datetime
from lesson3_schedule import LessonSchedule
from tkinter import *


day_of_the_week = str(datetime.today().strftime('%A'))
now = datetime.now()
hour = now.hour
minute = now.minute

lesson_schedule = LessonSchedule()


class Which_Lesson:
    def __init__(self):
        self.lesson = Lesson_
        self.day_of_the_week = day_of_the_week
        self.hour = hour
        self.minute = minute
    def check_lesson(self):
        if self.day_of_the_week == self.lesson.day_of_week:
            if self.hour == self.lesson.hour:
                if self.minute <= 45:
                    return True






def lessonn_check():
    lesson = Which_Lesson()
    if lesson.check_lesson() == True:
        name =lesson_schedule.print_all()
        return str(name)



class Lesson_check:
    def __init__(self):
        self.lesson = Lesson_

    def check_lesson(self):
        lesson_schedule.addLesson(Lesson_)
        lessonn_check()
        lesson_schedule.deleteLesson(Lesson_)



check = Lesson_check

Lesson_ = Wednesday_1
check.check_lesson(Lesson_)


Lesson_ = Wednesday_2
check.check_lesson(Lesson_)

Lesson_ = Wednesday_3
check.check_lesson(Lesson_)


Lesson_ = Wednesday_4
check.check_lesson(Lesson_)

Lesson_ = Wednesday_5
check.check_lesson(Lesson_)


Lesson_ = Wednesday_6
check.check_lesson(Lesson_)

Lesson_ = Wednesday_7
check.check_lesson(Lesson_)


Lesson_ = Wednesday_8
check.check_lesson(Lesson_)




