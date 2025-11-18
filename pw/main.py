from strongpassword import checkStrongPassword

def main():
    validator = checkStrongPassword()

    password = validator.getPassword()

    if password:
        print("Validating Password...")
        
        validated_password = validator.validate_password(password)

        if validated_password:
            print("Password Validated")
            validator.savetoClipboard()

if __name__ == "__main__":
    main()