degree_first=float(input("enter the temperature:"))
x=input("enter your scientist: f / c ")
if x=="f":
    degree_second=round(((degree_first-32)/1.8),3)
    print(f"your degree is:{degree_second}")
elif x=="c":
     degree_second=round(((degree_first*1.8)+32),3)
     print(f"your degree is:{degree_second}")
else:
    print("I dont know.  Im just a calculator :) ")