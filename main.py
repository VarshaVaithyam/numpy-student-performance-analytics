import numpy as np 
print("Numpy Version:", np.__version__)

# Generate random marks for 100 students (range: 0 to 100)
student_marks = np.random.randint(0, 101, size=100)

#Display student information
print("Student Marks:", student_marks)
print("Total Students:", np.size(student_marks))

#Display array properties
print("Array Shape:", student_marks.shape)
print("Array Data Type:", student_marks.dtype)
print("Array dimensions:", student_marks.ndim)

#student performance statistics
average_marks= np.mean(student_marks)
highest_marks= np.max(student_marks)
lowest_marks= np.min(student_marks)
total_marks= np.sum(student_marks)
median_marks= np.median(student_marks)
standard_deviation= np.std(student_marks)

print("Average marks:", average_marks)
print("Highest marks:", highest_marks)
print("Lowest marks:", lowest_marks)
print("Total marks:", total_marks)
print("Median marks:", median_marks)
print("Standard deviation:", standard_deviation)

#Filter student marks 
above_90= student_marks[student_marks > 90]
below_40= student_marks[student_marks < 40]
between_60_and_80= student_marks[(student_marks >= 60) & (student_marks <= 80)]

print("student scoring above 90:", above_90)
print("student scoring below 40:", below_40)
print("student scoring between 60 and 80:", between_60_and_80)
print("number of student scoring above 90:", np.size(above_90))
print("failed student:", np.size(below_40))

# Student Marks Indexing & Slicing
print("first student mark:", student_marks[0])
print("last student mark:", student_marks[-1])
print("5th student mark:", student_marks[4])
print("marks of first 10 students:", student_marks[0:10])
print("marks of last 10 students:", student_marks[-10:])
print("marks of student between 20 to 30:", student_marks[20:30])
print("alternate students marks:", student_marks[::2])
print("reverse student but every second student:", student_marks[::-2])

# Sort Student Marks
ascending_marks = np.sort(student_marks)
print("ascending student marks:", ascending_marks)
print("desecnding student marks:", ascending_marks[::-1])
print("top highest marks:", ascending_marks[-10:])
print("lowest 10 marks:", ascending_marks[0:10])
print("highest mark:", ascending_marks[-1])
print("lowest mark:", ascending_marks[0])

# Arithmetic Operations
print("grace marks:", student_marks + 5)
print("reduced marks:", student_marks -10)
print("double marks:", student_marks * 2)
print("half marks:", student_marks / 2)

attendance_bonus = np.random.randint(0, 6, size=100)
final_marks = student_marks + attendance_bonus
print(student_marks)
print(attendance_bonus)
print(final_marks)

print("student who pass:", student_marks [student_marks >= 40])
print("student scoring full marks:", student_marks [student_marks == 100])
print("student who did not score 50:", student_marks [student_marks != 50])

# Broadcasting Operations
bonus_marks = 10
updated_marks = student_marks + bonus_marks
print(updated_marks)
penalty = 5
penalty_subtracted =student_marks - penalty
print(penalty_subtracted)
scaled_marks = student_marks * 1.1
print(scaled_marks)
attendance_bonus = np.random.randint(0, 6, size=100)
updated_marks = attendance_bonus + student_marks
print(updated_marks)


# Student Performance Report
# Generate marks for 100 students
student_marks = np.random.randint(0, 101, size=100)
# Total Students
total_students = student_marks.size
# Statistics
average_marks = np.mean(student_marks)
highest_marks = np.max(student_marks)
lowest_marks = np.min(student_marks)
median_marks = np.median(student_marks)
standard_deviation = np.std(student_marks)
# Filtering
below_40 = student_marks[student_marks < 40]
above_90 = student_marks[student_marks > 90]
between_60_and_80 = student_marks[(student_marks >= 60) & (student_marks <= 80)]
# Passed & Failed Students
failed_students = below_40.size
passed_students = total_students - failed_students
# Percentages
pass_percentage = (passed_students / total_students) * 100
fail_percentage = (failed_students / total_students) * 100
# Sorting
ascending_marks = np.sort(student_marks)
descending_marks = ascending_marks[::-1]
# Display Report
print("STUDENT PERFORMANCE REPORT")
print(f"Total Students         : {total_students}")
print(f"Average Marks          : {average_marks:.2f}")
print(f"Highest Marks          : {highest_marks}")
print(f"Lowest Marks           : {lowest_marks}")
print(f"Median Marks           : {median_marks}")
print(f"Standard Deviation     : {standard_deviation:.2f}")
print(f"Passed Students        : {passed_students}")
print(f"Failed Students        : {failed_students}")
print(f"Pass Percentage        : {pass_percentage:.2f}%")
print(f"Fail Percentage        : {fail_percentage:.2f}%")
print("Top 10 Marks:")
print(descending_marks[:10])
print("Lowest 10 Marks:")
print(ascending_marks[:10])
print(f"Students Above 90      : {above_90.size}")
print(f"Students Between 60-80 : {between_60_and_80.size}")
# Grade Distribution
a_grade = student_marks[student_marks >= 90]
b_grade = student_marks[(student_marks >= 75) & (student_marks < 90)]
c_grade = student_marks[(student_marks >= 50) & (student_marks < 75)]
d_grade = student_marks[(student_marks >= 40) & (student_marks < 50)]
fail_grade = student_marks[student_marks < 40]
print("\nGrade Distribution")
print(f"A Grade (90-100) : {a_grade.size}")
print(f"B Grade (75-89)  : {b_grade.size}")
print(f"C Grade (50-74)  : {c_grade.size}")
print(f"D Grade (40-49)  : {d_grade.size}")
print(f"Fail (<40)       : {fail_grade.size}")