import random
import string

passlen = int(input("Enter length of password: "))

if passlen <= 0:
    print("Please enter a positive integer.")
else:
    charvalues = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(charvalues) for i in range(passlen))
    print("Your random password is:", password)

    output = input("Do you want to save it for any app/source? (Y/y for yes, N/n for no): ")
    print(output)
    if output.lower() == 'y':
        source = input("Enter the name of the source: ")
        with open('save.txt', 'a') as file:
            content = f"{source}: {password}\n"
            file.write(content)
        print("Data saved successfully.")
    if output.lower() == 'n':
        print("Password not saved.")
    else:
        print("Invalid input. Please enter Y/y or N/n.")
