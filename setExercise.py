biology = {'Todd', 'Marcy', 'Pamelia', 'Bill', 'Vera', 'Rickey', 'Margaret', 'Howard', 'Luke', 'Walton', 'Elwood', 'Harris', 'Delia', 'Brian', 'Brodie', 'Donald', 'Alexa'}
physics = {'Carol', 'Marcy', 'Janet', 'Jennifer', 'Bill', 'Donald', 'Liam', 'Gerald', 'Jack', 'Jospeh', 'Madge', 'Muriel', 'Alexa', 'Emma'}
music = {'Alexa', 'Janet', 'Brad', 'Marcy', 'Finn', 'Jake', 'Harris', 'Emma', 'Luke', 'Jack', 'Donald', 'John', 'Vinnie', 'Cassandra', 'Janell', 'Donna'}


students = set()
isMusicStudent = 'false'
isPhysicStudent = 'false'
isBiologyStudent = 'false'

countPeopleInAllSubjects = 0
contSubjects = 0

studentsWithOneSubject = dict()


for student in biology:
    students.add(student)

for student in physics:
    students.add(student)

for student in music:
    students.add(student)

for student in students:
    for musicStudent in music:
        if student is musicStudent:
            isMusicStudent = 'true'
            contSubjects += 1
            break

    for physicStudent in physics:
        if student is physicStudent:
            isPhysicStudent = 'true'
            contSubjects += 1
            break

    for biologyStudent in biology:
        if student is biologyStudent:
            isBiologyStudent = 'true'
            contSubjects += 1
            break

    if isMusicStudent is 'true' and isPhysicStudent is 'true':
        print(student + " is student of music and physics")
    if (isMusicStudent is 'true' or isPhysicStudent is 'true') and isBiologyStudent is 'false':
        print(student + " is student of music or physics but not biology")
    if isBiologyStudent is 'true':
        print(student + " is student of biology")
    if isPhysicStudent is 'true':
        print(student + " is student of physics")
    if isMusicStudent is 'true' and isPhysicStudent is 'false' and isBiologyStudent is 'true':
        print(student + " is student of music and biology but not physics")
    if contSubjects == 1:
        if isMusicStudent is 'true':
            studentsWithOneSubject.update({student:'study music'})
        elif isBiologyStudent is 'true':
            studentsWithOneSubject.update({student: 'study biology'})
        elif isPhysicStudent is 'true':
            studentsWithOneSubject.update({student: 'study physics'})

    if isMusicStudent is 'true' and isPhysicStudent is 'true' and isBiologyStudent:
        countPeopleInAllSubjects += 1

    isMusicStudent = 'false'
    isPhysicStudent = 'false'
    isBiologyStudent = 'false'
    contSubjects = 0

print("===============================================")
print("Number of students in all the subjects:"+str(countPeopleInAllSubjects))
print("===============================================")
print("Students studying just only one subject")
print(studentsWithOneSubject)
print("===============================================")