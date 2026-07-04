# 학생 성적 및 출결 관리하는 프로그램
students= {}

def add_student(student_id,name):
    students[student_id]= {'이름':name,'성적':{},'출결':[]}

def add_grade(student_id,subject,score):
    students[student_id]['성적'][subject]=score

def add_attendance(student_id,status):
    students[student_id]['출결'].append(status)
    
def get_selected_students(target_names):
    selected_data = []
    
    for student_id, info in students.items():
        if info['이름'] in target_names:
            python_score = info['성적'].get('파이썬', 0)
            attendance = " ".join(info['출결'])
            
            selected_data.append([student_id, info['이름'], python_score, attendance])
            
    return selected_data
