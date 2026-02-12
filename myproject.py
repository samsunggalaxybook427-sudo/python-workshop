roll_numbers = [200,201,202,203,204,205,206,207,207,208,209,210]
names = ['abhi','sai','jai','srinu','satya','praveen','mani','manoj','hemanth','vinay']
roll = int(input("Enter your roll number:"))
name = input("Enter your name:")
if roll in roll_numbers:
    print("Roll number already exists")
    i = roll_numbers.index(roll)
    print("name:",names[i])
    print("roll number:",roll_numbers[i])
else:
    print("roll number not found.")
    print("name not found.")
    new_roll_number = input("new roll number:")
    new_name = input("new name:")
    print("roll number:",new_roll_number)
    print("name:",new_name)
    print("\n Account created successfully")
    print("new roll number:",new_roll_number)
    print("new name:",new_name)
        
