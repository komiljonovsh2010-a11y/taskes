import json
with open("students.json") as fayl:
    students=json.load(fayl)

def best_worst_student(students:list):
    best_student=max(students,key=lambda x : x['grade'])
    wors_student=min(students,key=lambda x : x["grade"])
    ortacha=sum(student['grade'] for student in students)/len(students)
    print(f"Eng yaxshi o'quvchi\n{best_student['name']} : {best_student['grade']} ball\nEng yomon o'quvchi\n{wors_student['name']} : {wors_student['grade']} ball\nO'rtacha baho\n{ortacha:.1f}")
best_worst_student(students)
