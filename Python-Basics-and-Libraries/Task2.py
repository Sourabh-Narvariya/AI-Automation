# Task 2: Use NumPy to create an array of numbers and string and perform basic operations (sum, mean, median, max, min, split, append, insert, concatenate, sort)
import numpy as np

num_array = np.array([10, 20, 30, 40, 50])
print("Number Array:", num_array)

print("Sum:", np.sum(num_array))
print("Mean:", np.mean(num_array))
print("Median:", np.median(num_array))
print("Max:", np.max(num_array))
print("Min:", np.min(num_array))



appended_array = np.append(num_array, 60)
print("Appended Array:", appended_array)


inserted_array = np.insert(num_array, 2, 25)    
print("Inserted Array:", inserted_array)


concatenated_array = np.concatenate((num_array, np.array([70, 80])))
print("Concatenated Array:", concatenated_array)

sorted_array = np.sort(num_array)
print("Sorted Array:", sorted_array)







str_array = np.array(["apple", "banana", "cherry", "date"])
print("String Array:", str_array)


appended_str_array = np.append(str_array, "elderberry")
print("Appended String Array:", appended_str_array)

inserted_str_array = np.insert(str_array, 1, "blueberry")
print("Inserted String Array:", inserted_str_array)

concatenated_str_array = np.concatenate((str_array, np.array(["fig", "grape"])))
print("Concatenated String Array:", concatenated_str_array)

sorted_str_array = np.sort(str_array)
print("Sorted String Array:", sorted_str_array)

