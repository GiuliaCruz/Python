def concept_grades(value):
    grade = float(value)

    if grade > 10: 
        return 'Invalid Grade'
    elif grade >= 9.1:
        return 'A'
    elif grade >= 8.1:
        return 'A-'
    elif grade >= 7.1:
        return 'B'
    elif grade >= 6.1:
        return 'B-'
    elif grade >= 5.1:
        return 'C'
    elif grade >= 4.1:
        return 'C-'
    elif grade >= 3.1:
        return 'D'
    elif grade >= 2.1:
        return 'D-'
    elif grade >= 1.1:
        return 'E'
    elif grade >= 0:
        return 'E-'
    else:
        return 'Invalid Grade'
    
    if __name__ == '__main__':
        reported_value = input('Student Grade: ')
        concept = concept_grades(reported_value)
        print(concept)
