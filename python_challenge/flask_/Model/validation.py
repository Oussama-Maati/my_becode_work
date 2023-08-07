import re


def validate_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(pattern, email) is not None


def contains_special_characters(input_):
    pattern = r'[^a-zA-Z\s]'
    return bool(re.search(pattern, input_))


def not_msg(input_):
    pattern = r'[^a-zA-Z0-9\s]'
    return bool(re.search(pattern, input_))


def msg(input_):
    pattern = r'[^a-zA-Z0-9\s]'
    return re.sub(pattern, '', input_)


def del_spe_char(input_):
    return re.sub(r'[^a-zA-Z\s]', '', input_)


def remove_numbers(input_):
    return re.sub(r'\d+', '', input_)


def validate_form_data(first_name, last_name, email, country, message, gender, topics):
    errors = {}

    if not (first_name and last_name and email and country and message and gender):
        errors['error_message'] = "Every input is mandatory"
    if not validate_email(email):
        errors['email_error'] = "Please enter a valid email"
    if not topics:
        errors['topic_error'] = "Please select at least one topic."
    for i, input_ in enumerate([first_name, last_name]):
        if contains_special_characters(input_):
            errors[f"error{i}"] = "Invalid Characters"
        elif input_.strip() == "":
            errors[f"error{i}"] = "Cannot be empty"

    if not_msg(message):
        errors[f"error{2}"] = "Invalid Characters"

    return errors
