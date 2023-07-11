import re

from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def contact_form():
    if request.method == 'POST':
        first_name = request.form.get('first_name')
        last_name = request.form.get('last_name')
        email = request.form.get('email')
        country = request.form.get('country')
        message = request.form.get('message')
        gender = request.form.get('gender')
        topics = request.form.getlist('topics')

        print("First Name:", first_name)
        print("Last Name:", last_name)
        print("Email:", email)
        print("Country:", country)
        print("Message:", message)
        print("Gender:", gender)
        print("Topics:", topics)

        # Sanitization et validation
        if not (first_name and last_name and email and country and message and gender):
            error_message = "Tous les champs sont obligatoires."
            return render_template('contact_form.html', error_message=error_message)

        if not validate_email(email):
            error_message = "Veuillez entrer une adresse email valide."
            return render_template('contact_form.html', error_message=error_message)

        # Envoi des données et affichage de la page de confirmation
        return render_template('confirmation.html', first_name=first_name, last_name=last_name,
                               email=email, country=country, message=message,
                               gender=gender, topics=topics)

    # Affichage du formulaire
    return render_template('contact_form.html')


def validate_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(pattern, email) is not None


if __name__ == '__main__':
    app.run()
