# 학생 성적 및 출결 관리하는 프로그램
students= {}

def add_student(student_id,name):
    students[student_id]= {'이름':name,'성적':{},'출결':[]}

def add_grade(student_id,subject,score):
    students[student_id]['성적'][subject]=score

def add_attendance(student_id,status):
    students[student_id]['출결'].append(status)