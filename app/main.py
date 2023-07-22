from app.services import read_file
from app.services import generate_users
from app.services import who_is_here
from app.services import midle
import os


def main():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    print("------1------")
    link_1 = os.path.join(current_dir, "../files_input/data_input.txt")
    print(read_file.get_file_content(link_1))
    print("------2------")
    users = generate_users.generate(num_users=10)
    for user in users:
        print(user)
    print("------3------")
    link_3 = "http://api.open-notify.org/astros.json"
    print(who_is_here.parsing(link_3))
    print("------4------")
    link_4 = os.path.join(current_dir, "../files_input/people_data(extended).csv")
    print(
        f"height {midle.parameter_averaging(link_4)[0]} "
        f"weight {midle.parameter_averaging(link_4)[1]}"
    )
