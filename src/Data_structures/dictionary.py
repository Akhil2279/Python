students = {
    "Akhil": 85,
    "Ravi": 90,
    "Sneha": 88
}

print("Marks of Ravi:", students["Ravi"])


#Access dictionary values
student = {
    "name": "Akhil",
    "age": 22
}

print(student["name"])
print(student["age"])


#Add new key and value
student = {
    "name": "Akhil",
    "age": 22
}

student["city"] = "Bangalore"
print(student)


#Update value in dictionary
student = {
    "name": "Akhil",
    "age": 22
}

student["age"] = 23
print(student)


#Remove key-value pair from dictionary

student = {
    "name": "Akhil",
    "age": 22
}

student.pop("age")
print(student)


#Check if key exists in dictionary
student = {
    "name": "Akhil",
    "age": 22
}

if "name" in student:
    print("Key exists")
else:
    print("Key not found")

