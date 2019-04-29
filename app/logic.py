def calculate_required_grade(numbers, percent):
    min_grade = min(numbers[0:5])
    value = ((percent * 7) - sum(numbers) + min_grade) / 2
    value = round(value, 0)

    if value < min_grade:
        value = (percent * 7) - sum(numbers)

    return value   

def calculate_grade_data(numbers):
    data = {'for_a':       calculate_required_grade(numbers, 94),
            'for_a_minus': calculate_required_grade(numbers, 90),
            'for_b_plus' : calculate_required_grade(numbers, 87),
            'for_b':       calculate_required_grade(numbers, 84),
            'for_b_minus': calculate_required_grade(numbers, 80),
            'for_c_plus' : calculate_required_grade(numbers, 77),
            'for_c':       calculate_required_grade(numbers, 74),
            'for_c_minus': calculate_required_grade(numbers, 70),
            'for_d_plus' : calculate_required_grade(numbers, 67),
            'for_d':       calculate_required_grade(numbers, 64),
            'for_d_minus': calculate_required_grade(numbers, 60),
            'avg': round(sum(numbers) / len(numbers), 2)
            }

    done = False
    for key in data.keys():
        if data[key] <= 0:
            if not done:
                data[key] = "0"
                done = True
            else:
                data[key] = "-"               

    return data