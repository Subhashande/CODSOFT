import random
import string
def generate_password(length, uppercase=True, lowercase=True, digits=True, special_chars=True):
    characters = ""
    if uppercase:
        characters += string.ascii_uppercase
    if lowercase:
        characters += string.ascii_lowercase
    if digits:
        characters += string.digits
    if special_chars:
        characters += string.punctuation
    if not characters:
        print("Please select at least one character type (uppercase, lowercase, digits, special characters).")
        return
    password = ''.join(random.choice(characters) for _ in range(length))
    return password
def main():
    print("Password Generator")
    length = int(input("Enter the desired length of password: "))
    uppercase = input("Does it can include uppercase letters (Y/N): ").lower() == 'y'
    lowercase = input("Does it can contain lowercase letters (Y/N): ").lower() == 'y'
    digits = input("Does it can contain digits (Y/N): ").lower() == 'y'
    special_chars = input("Include special characters (Y/N): ").lower() == 'y'
    password = generate_password(length, uppercase, lowercase, digits, special_chars)
    if password:
        print(f"Password is succesfully generated: {password}")
    else:
        print("Password generation failed.")
    print("THANK YOU")
if __name__ == "__main__":
    main()