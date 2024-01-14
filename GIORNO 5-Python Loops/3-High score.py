
student_scores = input("Digita i punteggi separati da uno spazio: ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])


max = 0

for massimo in student_scores:
  
  if massimo > max:
    max = massimo
print (f"The highest score in the class is: {max}")