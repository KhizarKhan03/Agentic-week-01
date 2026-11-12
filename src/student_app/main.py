from config import APP_NAME 
from config import DEBUG 
from config import MAX_STUDENTS
from logger import logger
from utils.validation import validate_name
from utils.validation import validate_marks

import json

def load_student():
 with open("../../data/student.json", "r") as file:
    student = json.load(file)

 return student

def main():
 print("Application Starting...")
 print()
 logger.info("Application started")
 print(f"Application Name: {APP_NAME}")
 print(f"Debug Mode: {DEBUG}")
 print(f"Maximum Students: {MAX_STUDENTS}")
 print()

 student = load_student()

 name = input("Enter student name: ")
 if not validate_name(name):
    logger.warning("Empty student name entered")
    print("Error: Name cannot be empty.")
    exit()
 try:
    marks = int(input("Enter student marks: "))
 except ValueError:
    logger.error("Invalid marks entered")
    print("Error: Marks must be a number.")
    exit()
 
 if not validate_marks(marks):
    logger.warning(
        f"Invalid marks entered: {marks}"
    )
 
    print("Error: Marks must be between 0 and 100.")
    exit()
 
 if marks >= 80:
    grade = "A"
 elif marks >= 70:
    grade = "B"
 elif marks >= 60:
    grade = "C"
 elif marks >= 50:
    grade = "D"
 else:
    grade = "F" 
 
 print()
 print("Student Report")
 print("----------------")
 print(f"Name: {name}")
 print(f"Marks: {marks}")
 print(f"Grade: {grade}")


if __name__ == "__main__": main()
