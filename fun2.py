
def draw_1d(number, a):
    for i in range(5):
        print(number * stars)
def draw_2d(number, stars, range1):
    for i in range(range1):
        print(number * stars)
def draw_3d(number, lines, char1, char2):
    for i in range(lines):
        for i in range(lines[0], lines[int(line)]):
            print(char1 * number)
        for i in range(lines[1], lines[int(lines) - 1]):
            print(char2 * number)

def special_draw_2d(number, lines, c1, c2):
   first_line = c1 * lines
   fill_line = c1 +((lines-2) * c2) + c1
   for num in range(number):
        if num == 0 or num == number-1:
           print(first_line)
        else:
            print(fill_line)
       
        
