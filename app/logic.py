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
                data[key] = "Minimum Grade Possible"
                done = True
            else:
                data[key] = "-"               

    return data

def make_chart(scores):
    # Bokeh Libraries
    from bokeh.plotting import figure, show
    from bokeh.embed import components

    assessment_names = ['T1', 'T2', 'T3', 'T4', 'T5', 'HW']
    scores = [float(score) for score in scores]
    avg = round(sum(scores) / len(scores), 2) 

    # Create chart
    chart = figure(title='Scores',
                x_range=assessment_names,
                plot_height=300, plot_width=300,        # TODO Make plot responsive
                y_minor_ticks=4,
                toolbar_location=None)

    # Draw vertical bars representing the assessment scores
    chart.vbar(x=assessment_names, top=scores, width=0.75, color='#007BFF')

    # Draw line representing assessment average
    chart.line(x=range(len(scores)+1), y=avg, color='red')

    # Modify properties of chart
    chart.xgrid.grid_line_color = None
    chart.y_range.start = 0
    chart.y_range.end = 100

    # return plot
    return components(chart)
