# exercise the shows how you recieve input from users and then print it back

print("how are old are you?" , end=' ')
age = input()
# We put a end=' ' at the end of each print line. This tells print to not end the line with a newline character and go to the next line.
print("How tall are you?" , end=' ')
# input function takes an user's input and assign it to a variable
height = input()
print("How much do you weigh", end=' ')
weight = input()

print(f"So, you're {age} years old, {height} tall and {weight} heavy.")


