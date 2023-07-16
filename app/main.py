import faker



def print_name():
    print(faker.Faker().name())


if __name__ == '__main__':
    print_name()
    print('hello')