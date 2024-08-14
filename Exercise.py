#n = 5
#while n > 0:
   # print(n)
   # n = n - 1
#print('Blastoff!')
#print(n)

#while True:
    #value = input(["enter Integer, [q to quire]:"])
    #if value == 'q':
    # break
   # number = int(value)
    #if number % 2 == 0:
       #continue
    #print(number)

    #word = 'hello'
    #for letter in word:
       #if letter == 'o':
         # break
      # print(word)


from random import randint
play = 1
points = 0
while play == 1:
    a = randint(0,9)
    b = randint(0,9)
    print("What is " + str(a) + "x" + str(b) + "?")
    answer = int(input("What is your answer"))
    if answer == (a * b):
        print("You are correct!")
        points += 1
        print("Player has"  ,  str(points)  ,  "points")
    else:
        print("incorrect. The answer is", " " +  str(a * b))
    multiplication = (input("Would you like to play again? yes/no"))
else:
    print("Game ended. Your score is:" + str(points))

           