student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])

height_sum = 0

for avg in student_heights:
  height_sum += avg

height_avg = round(height_sum / len(student_heights))

print(height_avg)