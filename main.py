import tools
from tabulate import tabulate
tools.add_student('12261247', '나승재')
tools.add_grade('12261247', '컴퓨터프로그래밍파이썬', 95)
tools.add_attendance('12261247', 'O')
tools.add_attendance('12261247', 'O')

tools.add_student('12261223', '기장님')
tools.add_grade('12261223', '컴퓨터프로그래밍파이썬', 93)
tools.add_attendance('12261223', 'X')
tools.add_attendance('12261223', 'O')
table_data = []
for student_id, info in tools.students.items():
    name = info['이름']
    python_score = info['성적'].get('컴퓨터프로그래밍파이썬', 0) 
    attendance_record = " ".join(info['출결']) 
    table_data.append([student_id, name, python_score, attendance_record])
record = ["학번", "이름", "컴퓨터프로그래밍파이썬이썬 성적", "출결 기록"]
print(tabulate(table_data, record=record, tablefmt="grid"))