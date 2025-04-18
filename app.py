import random
import string


def password_generator(length, use_lower, use_upper, use_number,use_special):
    chars = ""

    if use_lower:
        chars += string.ascii_lowercase
    if use_upper:
        chars += string.ascii_uppercase
    if use_number:
        chars += string.digits
    if use_special:
        chars += string.punctuation

    if not chars:
        print("⚠️ Oops! No character type selected. Using lowercase and special characters by default.")
        chars = string.ascii_lowercase
        chars += string.punctuation

    password = ""
    for _ in range(length):
        password  += random.choice(chars)

    return password


def check_password_strength(password):
    score = min(len(password)/16, 1.0)
    has_lower = any(c.islower() for c in password)
    has_upper = any(c.isupper() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(c in string.punctuation for c in password)

    variety = (has_lower + has_special + has_digit + has_upper) / 4.0

    final_score  = (score * 0.6) + (variety *0.4)

    if final_score >= 0.8:
        return "ULTRA STRONG !"
    elif final_score >= 0.6:
        return "STRONG!"
    elif final_score >= 0.4:
        return "DECENT!"
    else:
        return "NEED IMPROVEMENT"

def get_yes_no_input(question):
    while True:
        response = input(question +" (y/n): ").lower()
        if response in ["yes",'y']:
            return True
        if response in ['no','n']:
            return False
        else:
            print("Please enter valid response!")

def main():
    print("🔐 ----- SECUREPASS MAKER ----- 🔐")
    print("✨ Create a super strong and secure password with ease!")


    while True:
        try:
            pwd_length = int(input("\nEnter password length (8-30): "))
            if 8 <= pwd_length <= 30:
                break
            else:
                print("Please choose a length between 8 and 30!")
        except ValueError:
            print("Oops! Please enter valid number")

    print("\n🔧 Let's customize your password:")
    use_lower = get_yes_no_input("✅ Include lowercase letters (a-z)?")
    use_upper = get_yes_no_input("✅ Include uppercase letters (A-Z)?")
    use_number = get_yes_no_input("✅ Include numbers (0-9)?")
    use_special = get_yes_no_input("✅ Include special characters (!@#$ etc)?")

    print("\n🔄 Generating your secure password...")
    password = password_generator(pwd_length, use_lower,use_upper,use_number,use_special)

    print("🆕 -------- Your New Password -------- 🆕")
    print(f"🔑 {password}")

    strength = check_password_strength(password)
    print(f"\n📊 Password Strength: {strength}")

    print("\n💡 Password Tips:")
    print("• Use a combination of upper, lower, numbers, and special characters.")
    print("• Avoid using common words or patterns.")
    print("• Change your passwords regularly.")
    print("• Use a password manager to store complex passwords.")

    if get_yes_no_input("\n🔁 Would you like to create another password?"):
        main()
    else:
        print("\n✅ Thank you for using SecurePass Maker! Stay safe online 🌐🔐")

if __name__ == "__main__":
    main()
