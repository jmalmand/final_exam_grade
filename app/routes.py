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
        numbers_entered = 0


        for field in form:
            try:
                field_data = field.data
                if isinstance(field_data, Decimal):
                    numbers_entered += 1
                    numbers.append(field_data)
            except Exception:
                pass

        if sum(numbers) == 0:
            flash("Enter at least one grade greater than 0.")
            return redirect(url_for('index'))
            

        avg = sum(numbers) / numbers_entered
        avg = round(avg, 2)
    
        for_a = ((94 * 7) - sum(numbers))/ (7 - len(numbers))
        for_a = round(for_a, 2)

        for_a_minus = ((90 * 7) - sum(numbers)) / (7 - len(numbers))
        for_a_minus = round(for_a_minus, 2)


        data = {'avg': avg, 'for_a': for_a, 'for_a_minus': for_a_minus}

            

        return render_template('compute.html', data=data)
    return render_template('index.html', form=form)


@app.route('/compute')
def compute():
    return render_template('compute.html', form=form)


@app.route('/about')
def about():
    return render_template('about.html')