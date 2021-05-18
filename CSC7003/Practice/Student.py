class Student:
    def __init__(self, name):
        self.name = name
        self.courses = []
    def add_course(self, cno, credits, grade):
        self.courses.append((cno, credits, grade))
    def gpa(self):
        grades = {'A+': 4.3, 'A': 4.0, 'A-': 3.7, 'B+': 3.3, 'B': 3.0, 'B-': 2.7, 'C+': 2.3, 'C': 2.0, 'D+': 1.3, 'D': 1.0, 'F': 0.0}
        points = 0
        creds = 0
        for (cn, cr, gr) in self.courses:
            points += cr*(grades[gr])
            creds += cr
        if(creds > 0):
            return(round(points/creds, 2))
        else:
            return None
