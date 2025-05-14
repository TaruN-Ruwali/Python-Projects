#Area and Volume finder.
import math
# Important values needed while calculating
n=math.pi
#Area starts here!!!
A_V=input('What you want Area or Volume.:- ')
Shape=input('Shape of the diagram.: ')
if A_V=='area':
    if Shape=='square':
        side=float(input('Enter the side of square.:- '))
        print('Area of square.: ',side**2)
    elif Shape=='rectangle':
        length=float(input('Enter length of rectangle.: '))
        breadth=float(input('Enter breadth of rectangle.: '))
        print('Area of rectangle.: ',length*breadth)
    elif Shape=='circle':
        radius=float(input('Enter radius of circle.: '))
        print('Area of circle.: ',2*n*radius)
    elif Shape=='triangle':
        type=input('Which type of triangle you are having.: ')
        if type=='equilateral':
            side=float(input('Enter side of the triangle.: '))
            print('Area of equilateral triangle.: ',(3**0.5)/4*(side**2))
        elif type=='isosceles':
            base=float(input('Enter base of the triangle.: '))
            height=float(input('Enter height of the triangle.: '))
            print('Area of isosceles triangle.: ',1/2*base*height)
        else:
            type=='scalene'
            base=float(input('Enter base of the triangle.: '))
            height=float(input('Enter height of the triangle.: '))
            print('Area of triangle.: ',1/2*base*height)
    elif Shape=='rhombus':
        diagonal1=float(input('Enter 1st diagonal.: '))
        diagonal2=float(input('Enter 2nd diagonal.: '))
        print('Area of rhombus.: ',(diagonal1*diagonal2)/2)
    elif Shape=='cube':
        side=float(input('Enter the side of cube.: '))
        print('Area of cube.: ',6*side**2)
    elif Shape=='cubiod':
        length=float(input('Enter length of cubiod.: '))
        breadth=float(input('Enter breadth of cubiod.: '))
        height=float(input('Enter height of cubiod.: '))
        print('Area of cubiod.: ',2*length*breadth+2*breadth*height+2*height*length)
    elif Shape=='cylinder':
        radius=float(input('Enter radius of cylinder.: '))
        height=float(input('Enter height of cylinder.: '))
        print('Area of cylinder.: ',2*n*radius*(height+radius))
    elif Shape=='sphere':
        radius=float(input('Enter radius of sphere.: '))
        print('Area of sphere.: ',4*n*(radius**2))
    elif Shape=='hemisphere':
        radius=float(input('Enter radius of hemisphere.: '))
        print('Area of hemisphere.: ',2*n*(radius**2))
    else:
        radius=float(input('Enter radius of cone.: '))
        slant_height=float(input('Enter slant height of cone.: '))
        print('Area of cone.: ',n*radius*slant_height+(n*(radius**2)))
#Volumes starts here!!!
elif A_V=='volume':
    if Shape=='cube':
        side=float(input('Enter the side of cube.:- '))
        print('Volume of cube.: ',side**3)
    elif Shape=='cubiod':
        length=float(input('Enter length of cubiod.: '))
        breadth=float(input('Enter breadth of cubiod.: '))
        width=float(input('Enter width of cubiod.: '))
        print('Volume of cubiod.: ',length*breadth*width)
    elif Shape=='cone':
        radius=float(input('Enter radius of cone.: '))
        height=float(input('Enter height of cone.: '))
        print('Volume of cone.: ',n*(radius**2)*(height/3))
    elif Shape=='sphere':
        radius=float(input('Enter radius of sphere.: '))
        print('Volume of sphere.: ',(4/3)*n*(radius**3))
    elif Shape=='cylinder':
        radius=float(input('Enter radius of cylinder.: '))
        height=float(input('Enter height of cylinder.: '))
        print('Volume of cylinder.: ',n*(radius**2)*height)
    else:
        radius=float(input('Enter radius of hemisphere.: '))
        print('Volume of hemisphere.: ',(2*n*(radius**3))/3)
else:
    print('sorry!!! Not available right now.')
k=input('Press to exit')
