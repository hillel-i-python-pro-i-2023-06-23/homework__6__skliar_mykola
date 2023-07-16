from app.services import read_file
from app.services import generate_users


if __name__ == '__main__':
    print("------1------")
    print(read_file.get_file_content('../files_input/data_input.txt'))
    print("------2------")
    users = generate_users.generate(num_users=100)
    for user in users:
        print(user)
    print("------3------")