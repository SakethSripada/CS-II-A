import re
import pygal


# PART B ANSWER, so the file is created without depending on other things
def create_pushup_chart():
    chart = pygal.Line()
    chart.title = 'Weekly Pushups'
    chart.x_labels = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    chart.add('Jackson', [50, 42, 37, 40, 45, 55, 24])
    chart.add('Dejuan', [13, 27, 35, 24, 36, 47, 44])
    chart.add('Darcy', [30, 35, 33, 28, 23, 20, 18])
    chart.render_to_file('pushups.svg')


create_pushup_chart()


# PART A ANSWER BELOW
def get_user_input():
    global details
    people = []
    for i in range(3):
        det = input(
            f"Enter details for person {i + 1} in the following format WITHOUT spaces: Name,Age,Phone Number,"
            f"Zip Code,Eye Color)")
        details = det.split(',')
        person = {
            'name': details[0],
            'age': int(details[1]),
            'phone_number': details[2],
            'zip_code': details[3],
            'eye_color': details[4].lower()
        }
        people.append(person)
    return people


people = get_user_input()


def validation(person):
    phone_number_format = re.compile(r'\d{3}-\d{3}-\d{4}')
    zip_code_format = re.compile(r'\d{5}')
    allowed_eye_colors = ['amber', 'brown', 'blue', 'green', 'hazel', 'gray']

    if not (0 <= person["age"] <= 110):
        return False
    if not phone_number_format.match(person["phone_number"]):
        return False
    if not zip_code_format.match(person["zip_code"]):
        return False
    if person["eye_color"] not in allowed_eye_colors:
        return False
    else:
        return True


for person in people:
    print(", ".join([f"{key}: {value}" for key, value in person.items()]))

name = input("Do you want to search for a person's phone number? Type their name.")
for person in people:
    if person["name"].lower().strip() == name.lower().strip():
        print(person["phone_number"])

full_name = input("Type your full name to create a username")
username = full_name.replace(" ", "").lower()
print(f"Your username is {username}")

change_eye_name = input("Enter the name of the person whose eye color you want to change: ")
new_color = input("Enter the new eye color:")
for person in people:
    if person["name"].lower() == change_eye_name.lower():
        person["eye_color"] = new_color
        print(", ".join([f"{key}: {value}" for key, value in person.items()]))

del_zip_name = input("Enter the name of the person whose zip code you want to delete")
for person in people:
    if person["name"].lower() == del_zip_name.lower():
        del person["zip_code"]
        print(", ".join([f"{key}: {value}" for key, value in person.items()]))
