#create a program that helps us calculate how many cans of paint we need to buy for a given surface area of wall to be painted
#INstructions:1can of paint can cover 5square meters of wall.Given a random height and a width of wall, calculate how many cans of paint you will need to buy
#number of cans=(wall height X wall width) + coverage per can.
#e.g height= 2,width= 4, coverage 5   number of cans=(2x4)/5=1.6
#but because you can't use 0.6 of a can of paint, the result be rounded up to 2 cans.
import math

def paint_calc(Height, width, cover):
    area = Height * width
    num_of_can = math.ceil(area/ cover) #to roundoff number, import math and use math.ceil
    print((f'You will need {num_of_can} cans of paint.'))

test_h = int(input('Height of wall:'))
test_w = int(input('Width of wall:'))
coverage = 5
paint_calc(Height = test_h, width = test_w, cover = coverage)