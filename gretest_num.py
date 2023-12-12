while True:
    print("enter the 3 numbers  you want to see which is the greatest , 2nd greatest  ")
    x = int(input("enter the first number = "))
    y = int(input("enter the second number = "))
    z = int(input("enter thhe third number = "))
    if x>y>z:
        print("the greatest numbeer is = ",x,"\nthe second greatest number is = ",y,"\nand ", z," is the lowest nummber")
    elif x>z>y:
        print("the greatest numbeer is = ",x,"\nthe second greatest number is = ",z,"\nand ", y," is the lowest nummber")
    elif y>x>z:
        print("the greatest numbeer is = ",y,"\nthe second greatest number is = ",x,"\nand ", z," is the lowest nummber")
    elif y>z>x:
        print("the greatest numbeer is = ",y,"\nthe second greatest number is = ",z,"\nand ", x," is the lowest nummber")
    elif z>x>y:
        print("the greatest numbeer is = ",z,"\nthe second greatest number is = ",x,"\nand ", y," is the lowest nummber")
    elif z>y>x:
        print("the greatest numbeer is = ",z,"\nthe second greatest number is = ",y,"\nand ", x," is the lowest nummber")
    else:
        print("something went wrong")
    c = input("do you want to calcualte again (type y for yes and n for no  ) = ")
    if c == "n" or c == "N":
        break