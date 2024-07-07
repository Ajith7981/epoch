import matplotlib.pyplot as plt
from location import Location
from K_means import clustering

ine=[]
kk=Location()
for k in range(1,12):
    ll = clustering(kk.location_coordinate,k)
    _,_,inertia=ll.algo()
    ine.append(inertia)
k_val=range(1,12)
plt.figure(figsize=(8,6))
plt.plot(k_val,ine)
plt.xlabel("k values")
plt.ylabel("inertia")
plt.title("finding elbow")
plt.grid(True)
plt.show()
