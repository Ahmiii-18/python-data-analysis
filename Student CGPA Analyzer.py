import numpy as np 
# Example dataset: student names and CGPAs
students = ["Ali","Sara","Ahmed","Hina","Bilal"]
cgpa = np.array([3.5,3.8,3.2,3.9,3.0])

# Basic Analysis
average_cgpa = np.mean(cgpa)
highest_cgpa = np.max(cgpa)
lowest_cgpa = np.min(cgpa)
total_cgpa = np.sum(cgpa)

# Students above average
above_avg = [students[i] for i in range(len(cgpa)) if cgpa[i]> average_cgpa]

# Output
print("Average CGPA: ", average_cgpa)
print("Highest CGPA: ",highest_cgpa)
print("Lowest CGPA: ", lowest_cgpa)
print("Total CGPA: ",total_cgpa)
print("Students above average: ", above_avg)

import matplotlib.pyplot as plt

plt.bar(students, cgpa, color='skyblue')
plt.title("Student CGPA")
plt.xlabel("Students")
plt.ylabel("CGPA")
plt.show()