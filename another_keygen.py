from random import randint


def is_password_good(password: str):
    uppers = 0
    lowers = 0
    digits = 0
    
    for c in password:
        if c.isupper():
            uppers += 1
        elif c.islower():
            lowers += 1
        elif c.isdigit():
            digits += 1
    
    return len(password) >= 8 and (uppers * lowers * digits) > 0


def generate_password():

    # возьмём длину пароля от 8 до 15 символов, думаю достаточно
    length = randint(8, 15)
    
    # ASCII коды от 33 до 126 охватывают знаки пунктуации, цифры, скобки,
    # а также большие и маленькие латинские буквы
    password = ''.join(chr(randint(33, 126)) for _ in range(length))
    while True:
        if is_password_good(password):
            return password
        length = randint(8, 15)
        password = ''.join(chr(randint(33, 126)) for _ in range(length))


def main():
    print(generate_password())


if __name__ == '__main__':
    main()