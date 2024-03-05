#2D list
number_grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [0]
]

#print(number_grid[0][0])
#[left] showing row, [right] which element you chosen

#nested for loop
for row in number_grid:
    for col in row:
        print(col)

#building a traslator
#def translate(phrase):
#     translation = ""
#    for letter in phrase:
        #if letter in "aeiou":
          #  translation = translation + "g"
       # else:
        #    translation =translation + letter
#    return translation 

#print(translate(input("Enter phrase: ")))

#Try and except
try:
    answer = 10/0
    number = int(input("Enter a number: "))
    print(number)
#add as err , show division by zero.
except ZeroDivisionError as err:
    print(err)
except ValueError:
    print("invalid input")
#we put "a", program is broke.