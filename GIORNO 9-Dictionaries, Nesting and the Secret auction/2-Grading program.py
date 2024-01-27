student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}

# TODO-1: Create an empty dictionary called student_grades.
student_grades = {}

# TODO-2: Write your code below to add the grades to student_grades.👇
for student in student_scores:
  score = student_scores[student]
  if score > 90:
    student_grades[student] = "Outstanding"
  elif score > 80:
    student_grades[student] = "Exceeds Expectations"
  elif score > 70:
    student_grades[student] = "Acceptable"
  else:
    student_grades[student] = "Fail"

print(student_grades)



# Quando inizia il ciclo for, la prima iterazione estrae la chiave "Harry" e la assegna alla variabile 
# student. Nella seconda iterazione, la chiave "Ron" viene estratta e assegnata a student.

# Punto 4: Assegnazione del punteggio
# In ogni iterazione del ciclo for, dopo aver ottenuto il nome dello studente (la chiave del dizionario), 
# il codice estrae il punteggio corrispondente a quel nome dal dizionario student_scores. 
# Questo viene fatto utilizzando la sintassi student_scores[student], dove student è la chiave corrente
# nel dizionario.


# Esempio di Assegnazione del Punteggio:
# Continuando con l'esempio precedente:
# Nella prima iterazione, student è "Harry". Quindi, score = student_scores[student] assegna a score il 
# valore corrispondente a "Harry" nel dizionario, che è 81.
# Nella seconda iterazione, student è "Ron". Quindi, score = student_scores[student] assegna a score il 
# valore corrispondente a "Ron", che è 78.
# In sintesi, il ciclo for in questo codice passa attraverso tutti gli studenti nel dizionario 
# student_scores, e per ciascuno, estrae il suo punteggio e lo assegna alla variabile score. 
# Questo processo permette poi di valutare ogni studente in base al suo punteggio
