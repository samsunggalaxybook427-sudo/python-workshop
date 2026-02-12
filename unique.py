data = {
    "student names": ["ravi", "harry",
    "sai", "jai", "nandhu"],
    "Roll_number": [100, 101, 102, 104,
    105]
}
name = input("Enter your name: ")
Roll_number = int(input("Enter your Roll number: "))
if name in data["student names"]:
    index = data["student names"].index(name)
    if data["Roll_number"][index] == Roll_number:
        print("user exists!")
        print("name:", name)
        print("Roll_number:", Roll_number)
    else:
        print("Name exists but Roll_number does not match")
else:
    data["student names"].append(name)
    data["Roll_number"].append(Roll_number)
    print("new user added")
    print("name:", name, "roll_number:", Roll_number)