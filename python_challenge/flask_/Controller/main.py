from flask import Flask, render_template, request
from dotenv import load_dotenv
import os
load_dotenv()
from flask_.Model.db_query_sql_alchemy import db, ContactForm, start_db, send_db
from flask_.Model.validation import remove_numbers, msg, del_spe_char, validate_form_data

app = Flask(__name__, template_folder='../View/templates', static_folder='../View/static')
app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+mysqlconnector://{os.getenv("DB_USER")}:{os.getenv("DB_PASSWORD")}@localhost/Order_contact'
db.init_app(app)

@app.route('/', methods=['GET', 'POST'])
def contact_form():
    # db.init_app(app)
    start_db(app)
    if request.method == 'POST':
        first_name = request.form.get('first_name').strip()
        last_name = request.form.get('last_name').strip()
        email = request.form.get('email').strip()
        country = request.form.get('country')
        message = request.form.get('message').strip()
        gender = request.form.get('gender')
        topics = request.form.getlist('topics')
        topics_str = ",".join(topics)

        errors = validate_form_data(first_name, last_name, email, country, message, gender, topics)

        first_name = remove_numbers(del_spe_char(first_name))
        last_name = remove_numbers(del_spe_char(last_name))
        message = msg(message)

        if errors:
            return render_template('contact.html', errors=errors, form_data={
                'first_name': first_name,
                'last_name': last_name,
                'email': email,
                'country': country,
                'message': message,
                'gender': gender,
                'topics': topics})

        values = (first_name, last_name, email, country, message, gender, topics_str)
        send_db(values)
        return render_template('summary.html', first_name=first_name, last_name=last_name,
                               email=email, country=country, message=message,
                               gender=gender, topics=topics)

    return render_template('contact.html')
