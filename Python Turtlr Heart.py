#🔐Password Strength Analyzer

def check_password(password):
    length_check = len(password) >= 8

    uppercase_check=False
    lowercase_check=False
    digit_check=False
    special_check=False
    space_check=" " not in password

    for character in password:

        if character.isupper():
            uppercase_check=True

        elif character.islower():
            lower_check=True

        elif character.isdigit():
            digit_check=True

        elif not character.isalnum() and character!=" ":
            special_check=True

    score = sum([   
        length_check,
        uppercase_check,
        lowercase_check,
        digit_check,
        special_check,
        space_check,

    ])

        
    if score == 6:
        strength="💪 Strong"

    elif score >= 6:
        strength="🙂 Medium"

    else:
        strength="⚠️Weak"

    print("\n🔐 Password Strength Analysis")
    print("----------------------------")

    print("Length(minimum 8 character)", "passed✅" if length_check else "Failed❌")

