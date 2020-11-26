import matplotlib.pyplot as plt

##plot #########
year = [1970,1980,1990,2000,2010,2020]
pay = [75,80,120,130,135,180]
plt.plot(year,pay)
plt.xlabel("year")
plt.ylabel("pay")
plt.title("New Graph")
plt.legend
plt.show()

##bar###########
year = [1970,1980,1990,2000,2010,2020]
pay = [75,80,120,130,135,180]
plt.bar(year,pay)
plt.xlabel("year")
plt.ylabel("pay")
plt.title("New Graph")
plt.legend
plt.show()


##scatter####
year = [1970,1980,1990,2000,2010,2020]
pay = [75,80,120,130,135,180]
plt.scatter(year,pay)
plt.boxplot(pay)
plt.figure()
plt.xlabel("year")
plt.ylabel("pay")
plt.title("New Graph")
plt.legend
plt.show()

##Histogram######
pay = [75,80,120,130,135,180,75,75,130,120]
plt.hist(pay,bins=7)       #histogram
plt.polar(pay)        #polar
plt.show()