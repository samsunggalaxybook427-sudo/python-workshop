students = {
    101: {"name": "Henry", "age": 19, "marks": (85, 90, 88), "section": "A"},
    102: {"name": "Alice", "age": 20, "marks": (70, 75, 80), "section": "B"},
    103: {"name": "Bob", "age": 19, "marks": (95, 92, 98), "section": "A"},
    104: {"name": "Emily", "age": 21, "marks": (60, 65, 55), "section": "C"},
    105: {"name": "Cherry", "age": 20, "marks": (88, 82, 91), "section": "B"}
}
sections = {"A", "B", "C"}
while True:
    print("\n1.Add 2.Display 3.Search 4.Remove 5.Topper 6.Unique Sections 7.Exit")
    ch = input("Enter choice: ")
    if ch == "1":
        roll_number = int(input("Enter roll number: "))
        if roll_number in students:
            s = students[roll_number]
            print("Already exists! Details:", "Roll:", roll_number, "Name:", s["name"], "Marks:", s["marks"], "Age:", s["age"], "Section:", s["section"])
        else:
            name = input("Enter name: ")
            age = int(input("Enter age: "))
            m1 = float(input("Sub1 marks: "))
            m2 = float(input("Sub2 marks: "))
            m3 = float(input("Sub3 marks: "))
            sec = input("Enter section: ")
            students[roll_number] = {"name": name, "age": age, "marks": (m1, m2, m3), "section": sec}
            sections.add(sec)
            print("Added successfully. Details are:")
            print("Roll Number:", roll_number, "Name:", name, "Age:", age, "Marks:", (m1, m2, m3), "Section:", sec)
    elif ch == "2":
        for r in students:
            print("Roll Number:", r, "Data:", students[r])
    elif ch == "3":
        roll_number = int(input("Enter roll number to search: "))
        if roll_number in students:
            print(students[roll_number])
        else:
            print(" student data Not found")
    elif ch == "4":
        roll_number = int(input("Enter roll number to remove: "))
        if roll_number in students:
            del students[roll_number]
            print("student data is Removed")
        else:
            print("student data is Not found")
    elif ch == "5":
        top_score = -1
        topper_name = ""
        for r in students:
            total = sum(students[r]["marks"])
            if total > top_score:
                top_score = total
                topper_name = students[r]["name"]
        print("Topper is:", topper_name, "Score:", top_score)
    elif ch == "6":
        print("Unique sections:", sections)
    elif ch == "7":
        break