score_of_student = [120,140,164,147,129,157,146,127,162,152,143,135,141]
total_exam_score = sum(score_of_student)    
# print(total_exam_score)
sum = 0
for i in score_of_student:
    sum = sum + i
    print(sum)    
print(max(score_of_student))