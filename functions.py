def calculate_velocity(distance, time):
    v = distance / time
    print('The velocity is', v)

def calculate_area(radius):
    a = 3.142 *radius *radius
    print('The area is', a)



choice = input("Enter v to calculate velocity or a to calculate area of a circle : ")

if choice == 'v':
    distance = float(input("Distance: "))
    time = int(input('Time: '))
    calculate_velocity(distance, time)
elif choice == 'a':
    radius = float(input('Radius: '))
    calculate_area(radius)
else:
    print('Choose between a or v')
    
