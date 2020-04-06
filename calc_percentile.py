def percentile(marks, n):
    if len(marks) < n:
        return "Input value if greater than length of list"
    if not marks:
        raise IndexError("list is empty")
    score = marks[n - 1]
    marks = sorted(marks)
    count_of_std = len(marks)
    std_having_less_marks = len(marks[:marks.index(score)])
    percentile_of_std = (std_having_less_marks * 100) / count_of_std
    return percentile_of_std




#marks = [80,78,90,67,86,99,54,76,89,40]
#print(percentile(marks,6))