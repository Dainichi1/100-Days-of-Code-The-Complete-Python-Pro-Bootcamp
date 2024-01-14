line1 = ["⬜️","️⬜️","️⬜️"]
line2 = ["⬜️","⬜️","️⬜️"]
line3 = ["⬜️️","⬜️️","⬜️️"]
map = [line1, line2, line3]
print("Hiding your treasure! X marks the spot.")
position = input("Inserisci una lettera a scelta tra A, B, C seguita da 1, 2 o 3:\n") # Where do you want to put the treasure?

lettera = (position[0]).upper()
numero = (position[1])
croce = "X"

if lettera == "A":
  if numero == "1":
    map[0][0] = croce
if lettera == "A":
  if numero == "2":
    map [1][0] = croce
if lettera == "A":
  if numero == "3":
    map [2][0] = croce
if lettera == "B":
  if numero == "1":
    map[0][1] = croce
if lettera == "B":
  if numero == "2":
    map [1][1] = croce
if lettera == "B":
  if numero == "3":
    map [2][1] = croce
if lettera == "C":
  if numero == "1":
    map[0][2] = croce
if lettera == "C":
  if numero == "2":
    map [1][2] = croce
if lettera == "C":
  if numero == "3":
    map [2][2] = croce


print(f"{line1}\n{line2}\n{line3}")