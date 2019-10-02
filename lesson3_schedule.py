class LessonSchedule:
    def __init__(self):
        self.lessons = []

    def addLesson(self, lesson):
        self.lessons.append(lesson)

    def deleteLesson(self, lesson):
        self.lessons.remove(lesson)

    def print_all(self):
        for lesson in self.lessons:
            lesson_ = lesson.day_of_week + ' ' + str(lesson.hour) + ':' + str(lesson.minute) + ' ' + lesson.name
            return lesson_