import tools
from tabulate import tabulate
tools.add_student('12261247', '나승재')
tools.add_grade('12261247', '파이썬', 95)
tools.add_attendance('12261247', 'O')

tools.add_student('12261223', '윤종현')
tools.add_grade('12261223', '파이썬', 88)
tools.add_attendance('12261223', 'X')

tools.add_student('12261234', '김파이썬')
tools.add_grade('12261234', '파이썬', 100)
tools.add_attendance('12261234', 'O')

tools.add_student('12264321', '김백엔드')
tools.add_grade('12264321', '파이썬', 75)
tools.add_attendance('12264321', 'O')

print("[등록된 학생 명단]: 나승재, 윤종현, 김파이썬, 김백엔드")
user_input = input("검색할 학생의 이름을 띄어쓰기로 입력하세요 (예: 나승재 윤종현): ")

target_names = user_input.split() 

table_data = tools.get_selected_students(target_names)

print("\n" + "="*40)
if table_data: 
    headers = ["학번", "이름", "파이썬 성적", "출결 기록"]
    print(tabulate(table_data, headers=headers, tablefmt="grid"))
else: 
    print("❌ 일치하는 학생이 없습니다. 이름을 다시 확인해주세요.")
print("="*40 + "\n")
