from app.services import read_file
from app.services import generate_users
from app.services import who_is_here


if __name__ == '__main__':
    print("------1------")
    print(read_file.get_file_content('../files_input/data_input.txt'))
    print("------2------")
    users = generate_users.generate(num_users=10)
    for user in users:
        print(user)
    print("------3------")
    link = 'http://api.open-notify.org/astros.json'
    print(who_is_here.parsing(link))