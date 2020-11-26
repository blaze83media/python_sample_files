import numpy as np
#from numpy import genfromtxt                     #numpy read file
#mydata= genfromtxt('make.csv', delimeter=',')

a=[[2,4,6,8],
    [2,4,6,8]]

b=np.array(a)
print((b))
print(sum(np.array(a)))

y = np.array([55, 2, 3, 4])
print((y))
print(y.itemsize)


##########################
c=[3,4,5,6,2]
d=[6,2,6,3,6]
e=c+d+a
print(e)
print(c.index(5))   #position of a number in a list
print(d.count(6))  #count occurence of a number

c2=np.array(c)*0.025
d2=np.array(d)*0.045
e2=c2/d2**2
print(e2)
print(e2[2])   #print position 2
print(e2[-1])   #print position 1 from the end
print(e2[-2])   #print position 2 from the end
print(e2[1:3])   #print position 1 to 2
print(np.array(e2>1))


d.append(50)        #add data to list
print(d)

#ea=[["fname",tam],["lname",Ben],["DOB",Ths]] 
da=["fname",78455,"lname",458755,"DOB",310117]  #list wt key val pair
print(da)
print(type(da))


#e1=sorted(e, reverse=True)
#print(e1)

####### ndarray  ################
###  3 - dimensional array  ######
ax=[[[8,3,2,6],          #ensure to convert this list into an np.array bf working with it
    [2,4,6,8]],         #construct arrays wt array,zeros or empty
   [[3,4,5,6], 
    [6,2,6,6]],
   [[8,3,2,6],
    [4,3,2,6]]]

print(len(ax))      #length of list

ay=np.array(ax)    #list converted to nd array
print(ay)
print(ay.shape)
print(ay.sum(axis=1))
print(type(ax))
print(type(ay))
print(ay.dtype)
print(ay[1:2])

############## Range gives number 0 and above 

r1=np.arange(12)    # or np.arange(12, dtype=float)
print(r1.reshape((2,6)))


zs=np.zeros(6)      #displays only 0
zd=np.ones(6)       #displays only 1
zx=np.eye(4)        #matrix
print(zs,zd,zx)



vn=np.sin(ay)       #displays sin of all values in np.array
print(vn)

vn1=np.array([[5,1,3,4],[3,2,6,8]])
vn2=np.array([[3,2,6,5],[7,9,6,4]])
vn3=np.outer(vn1,vn2)    #each value in vn1 mulitplies the values in vn2
print(vn1,vn2)
print(vn3)

ya1=np.array([[7,2,8,4]])
ya=np.diag(ya1[0])
yb=np.diag(vn1[1])        #values along diagonal line in a matrix
print(ya)
print(yb)
#or use:
zq=np.matrix([3,5,2,6])
print(np.diag(zq.A1))

s1=np.array([[2,3,4,5],[4,2,3,5],[6,7,4,5]])
s2=np.array([2,4,6])

