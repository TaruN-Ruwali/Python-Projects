# Giving the lists to the user.
a=[1,4,7,10,13,16,19]
b=[2,5,8,11,14,17,20]
c=[3,6,9,12,15,18,21]
print('a.:-',a)
print('b.:-',b)
print('c.:-',c)
print("Choose a number from above's list.")
# Asking the user for the list.
l1=input('Enter the list in which your choosen number is present.:-')
ra=a[::-1] 
rb=b[::-1]
rc=c[::-1]
if l1=='a':
    rb.extend(ra)
    rb.extend(rc)
    t1=rb
elif l1=='b':
    rc.extend(rb)    
    rc.extend(ra)
    t1=rc
elif l1=='c':
    ra.extend(rc)
    ra.extend(rb)
    t1=ra
else:
    print('Sorry!! The list which you requested is not present.')    
a1=t1[::3]
b1=t1[1::3]
c1=t1[2::3]
print('a.:-',a1)
print('b.:-',b1)
print('c.:-',c1)
# Asking user for the 2nd time.
l2=input('Enter the list in which your choosen number is present.:-')
ra1=a1[::-1] 
rb1=b1[::-1]
rc1=c1[::-1]
if l2=='a':
    rb1.extend(ra1)
    rb1.extend(rc1)
    t2=rb1
elif l2=='b':
    rc1.extend(rb1)    
    rc1.extend(ra1)
    t2=rc1
elif l2=='c':
    ra1.extend(rc1)
    ra1.extend(rb1)
    t2=ra1
else:
    print('Sorry!! The list which you requested is not present.')
a2=t2[::3]
b2=t2[1::3]
c2=t2[2::3]
print('a.:-',a2)
print('b.:-',b2)
print('c.:-',c2)
# Asking the user for the 3rd time.
l3=input('Enter the list in which your choosen number is present.:-')
ra2=a2[::-1] 
rb2=b2[::-1]
rc2=c2[::-1]
if l3=='a':
    rb2.extend(ra2)
    rb2.extend(rc2)
    t3=rb2
elif l3=='b':
    rc2.extend(rb2)    
    rc2.extend(ra2)
    t3=rc2
elif l3=='c':
    ra2.extend(rc2)
    ra2.extend(rb2)
    t3=ra2
else:
    print('Sorry!! The list which you requested is not present.')    
z=t3[10:11]
print('Your choosen number was.:-',z)
k=input('Press to exit.')