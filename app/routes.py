from flask import render_template, redirect, url_for, flash
from app import app
from app.forms import ComputeForm
from decimal import Decimal

@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    form = ComputeForm()
    if form.validate_on_submit():

        numbers = []

        for field in form:
            try:
                field_data = field.data
                if isinstance(field_data, Decimal):
                    numbers.append(field_data)
            except Exception:
                pass

        if len(numbers) < 6:
            flash("Check to make sure that all grades were entered", "danger")
            return redirect(url_for('index'))


        avg = sum(numbers) / 6
        avg = round(avg, 0)


        min_grade = min(numbers[0:5])

        for_a = ((94 * 6) - sum(numbers) + min_grade)
        for_a = round(for_a, 0)

        for_a_minus = ((90 * 6) - sum(numbers) + min_grade)
        for_a_minus = round(for_a_minus, 0)

        for_b = ((80 * 6) - sum(numbers) + min_grade)
        for_b = round(for_b, 0)

        for_c = ((70 * 6) - sum(numbers) + min_grade)
        for_c = round(for_c, 0)

        for_d = ((60 * 6) - sum(numbers) + min_grade)
        for_d = round(for_d, 0)

        data = {'avg': avg, 
                'min_grade': min_grade,
                'for_a': for_a,
                'for_a_minus': for_a_minus,
                'for_b': for_b,
                'for_c': for_c,
                'for_d': for_d}

            

        return render_template('compute.html', data=data)
    return render_template('index.html', form=form)


@app.route('/compute')
def compute():
    return render_template('compute.html', form=form)


@app.route('/about')
def about():
    return render_template('about.html')