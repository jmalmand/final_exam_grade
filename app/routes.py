from flask import render_template, redirect, url_for, flash
from app import app
from app.forms import ComputeForm
from decimal import Decimal

from app.logic import calculate_grade_data

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

        data = calculate_grade_data(numbers)

        return render_template('compute.html', data=data)
    return render_template('index.html', form=form)


@app.route('/compute')
def compute():
    return render_template('compute.html', form=form)


@app.route('/about')
def about():
    return render_template('about.html')