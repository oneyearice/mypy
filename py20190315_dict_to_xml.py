from xml.dom.minidom import Document
from py20190315_dict import qytang_dict

doc = Document()
root = doc.createElement('root')
doc.appendChild(root)

qytang_commany = doc.createElement('公司')
qytang_commany.setAttribute('name','乾颐堂')
root.appendChild(qytang_commany)


for sub_depart in qytang_dict.get('公司').get('乾颐堂').get('部门'):
    department = doc.createElement('部门')
    department.setAttribute('name',sub_depart.get('部门名'))
    qytang_commany.appendChild(department)

    teachers = doc.createElement('师资')
    department.appendChild(teachers)

    for teacher in sub_depart.get('师资'):
        teacher_name = doc.createElement('老师')
        teacher_name.setAttribute('name',teacher)
        teachers.appendChild(teacher_name)

    courses = doc.createElement('课程')
    department.appendChild(courses)

    for course in sub_depart.get('课程'):
        course_name = doc.createElement('课程名')
        course_name.setAttribute('name',course)
        courses.appendChild(course_name)

xml_file = open('test.xml','w',encoding='utf-8')
xml_file.write(doc.toprettyxml(indent='   '))
xml_file.close()
