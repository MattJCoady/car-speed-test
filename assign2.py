obstacle = input('Is there an obstacle?')

if obstacle == 'N':
    print('Drive ahead')
            
    
if obstacle == 'Y':
    
    try:
        
        u0 = float(input('Enter the speed of the car in kmph'))
    
        d = float(input('Enter the distance to the obstacle in m'))
    
        if u0 < 0 or d < 0:
            print('Invalid response')
        
        s = ((u0/3.6)**2)/9
    
        if  s>=d:
    
            print('Brace for impact!!!')
    
        if  s<d:
    
            print('Brake!!!')
    
    except ValueError:
        print('Invalid response')
        
            
        
else: 
    print('Invalid response')