import turtle
def seq3np1(n):
    """
        Print the 3n+1 sequence from n, terminating when it reaches 1.
        args: n (int) starting value for 3n+1 sequence
        return: None
    """
    count = 0
    while(n != 1):
        count += 1
        if(n % 2) == 0:        # n is even
            n = n // 2
        else:                 # n is odd
            n = n * 3 + 1
    return count                  # the last print is 1

def graphData(upperBound = 0):
  turtle.Screen()
  todd = turtle.Turtle()
  bob = turtle.Turtle()
  turtle.setworldcoordinates(0, 0, 10, 10)
  max_so_far = 0
  for start in range(1, upperBound+1):
    result = seq3np1(start)
    if result > max_so_far:
      max_so_far = result
    todd.goto(0, max_so_far)
    printString = ('Maximum so far: ', start, max_so_far)
    todd.clear()
    todd.write(printString, False)
    turtle.setworldcoordinates(0,0,start+10, max_so_far+10)
    bob.down
    bob.goto(start, result)
    bob.up
  turtle.exitonclick()

def main():
  upper_bound = int(input("Please input an upper bound: "))
  if upper_bound > 0:
    for start in range(1, upper_bound+1): 
      result = seq3np1(start)
      print('Loop iteration: ', start, ' || Result: ', result)
    graphData(upper_bound)
    
  return

main()
