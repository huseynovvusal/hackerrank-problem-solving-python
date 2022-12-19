def gradingStudents(grades):
    result = []

    for grade in grades:
        if (grade < 38):
            result.append(grade)
        else:
            q = 5 - (grade % 5)

            if (q < 3):
                result.append(grade + q)
            else:
                result.append(grade)

    return result
