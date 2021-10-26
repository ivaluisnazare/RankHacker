# Enter with:
# 1. number of student;
# 2. Name and scores each student, as string;
# 3. choose one student's name for mean;
# 4. choose one student's name, for to have the mean.
n = int(input())
student_marks = {}
for _ in range(n):
    name, *line = input().split()
    scores = list(map(float, line))
    student_marks[name] = scores
query_name = input()
for i in student_marks.keys():
    if i == query_name:
        nota_name = student_marks.get(i)
mean = sum(nota_name)/len(scores)
print(f'{mean:0.2f}')