
# LEARN ABOUT LISTS
fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]
 
dirty_dozen = [fruits, vegetables]
 
print(dirty_dozen[1][0])


# LED DISPLAY
led = [
  ["###", " #", "###", "###"],
  ["# #", " #", "  #", "  #"],
  ["# #", " #", "###", "###"],
  ["# #", " #", "#  ", "  #"],
  ["###", " #", "###", "###"]]


display = input("What number will be displayed?")

for x in range(5):
  display_index = 0
  for no in display:
    if display_index == len(display)-1:
      print(led[x][int(no)])
    else:
      print(led[x][int(no)], end=" ")
    display_index += 1