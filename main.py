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