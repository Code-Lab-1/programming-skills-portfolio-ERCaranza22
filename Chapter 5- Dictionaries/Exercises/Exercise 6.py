# Student Information

Student = {"Name": "Errol Caranza", "Age": "19", "Gender": "Male", "Nationality":"Filipino"}
Student["Name"] = "Errol"
print(Student)

print(Student.keys())

print(Student.values())

x = Student.items()
print(x)

if "Name" in Student:
  print("Yes Name exists in the Student Dictionary")

Student.update({"Name":"Renselle", "Age":"22", "Gender":"Male"})
print(Student)

Student["Nationality"] = "British"
print(Student)

Student.pop("Nationality")
print(Student)

Student.popitem()
print(Student)