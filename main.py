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