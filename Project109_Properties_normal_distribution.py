import statistics as stat
import pandas as pd

df = pd.read_csv("Data\StudentsPerformance.csv")

math_marks_list = df["math score"].tolist()

math_marks_mean = stat.mean(math_marks_list)
math_marks_mode = stat.mode(math_marks_list)
math_marks_median = stat.median(math_marks_list)
math_marks_stdev = stat.stdev(math_marks_list)

print(math_marks_stdev)
print(math_marks_median)
print(math_marks_mean)
print(math_marks_mode)


first_std_math_start, first_std_math_end = math_marks_mean - math_marks_stdev, math_marks_mean + math_marks_stdev
second_std_math_start, second_std_math_end = math_marks_mean - (math_marks_stdev*2), math_marks_mean + (math_marks_stdev*2)
third_std_math_start, third_std_math_end = math_marks_mean - (math_marks_stdev*3), math_marks_mean + (math_marks_stdev*3)



marklist_of_data_within_first_std = [marks for marks in math_marks_list if(marks > first_std_math_start and marks < first_std_math_end)]
percent_of_first_std_data = (len(marklist_of_data_within_first_std)/len(math_marks_list))*100


marklist_of_data_within_second_std = [marks for marks in math_marks_list if(marks > second_std_math_start and marks < second_std_math_end)]
percent_of_second_std_data = (len(marklist_of_data_within_second_std)/len(math_marks_list))*100


marklist_of_data_within_third_std = [marks for marks in math_marks_list if(marks > third_std_math_start and marks < third_std_math_end)]
percent_of_third_std_data = (len(marklist_of_data_within_third_std)/len(math_marks_list))*100

print(percent_of_first_std_data, percent_of_second_std_data, percent_of_third_std_data)
