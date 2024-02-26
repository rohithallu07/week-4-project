import random
import string


def generate_password(length=12):
    # Define characters to be used in the password
    characters = string.ascii_letters + string.digits + string.punctuation

    # Generate the password
    password = ''.join(random.choice(characters) for _ in range(length))

    return password


def generate_multiple_passwords(num_passwords=1, length=12):
    passwords = [generate_password(length) for _ in range(num_passwords)]
    return passwords


def main():
    print("Welcome to the Password Generator!")

    # Get user input for password length and quantity
    length = int(input("Enter the desired length for the password: "))
    num_passwords = int(input("Enter the number of passwords to generate: "))

    # Generate and display passwords
    passwords = generate_multiple_passwords(num_passwords, length)
    print("\nGenerated Passwords:")
    for i, password in enumerate(passwords, start=1):
        print(f"Password {i}: {password}")


if __name__ == "__main__":
    main()
