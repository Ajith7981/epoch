import matplotlib.pyplot as plt
import numpy as np
import geopandas as gpd
from shapely.geometry import Point
from K_means import clustering
from location import Location
loc=Location()
location_coordinates=loc.location_coordinate
ap=loc.ap
location_coordinates=ap[["Longitude","Latitude"]].values
location_coordinates=location_coordinates.astype(float)
number_of_clusters=5
kl=clustering(location_coordinates,number_of_clusters)
centroids,labels,inertia=kl.algo()
geometry = [Point(xy) for xy in zip(ap["Longitude"], ap["Latitude"])]
geo_df = gpd.GeoDataFrame(ap, geometry=geometry)

centroid_geometry = [Point(xy) for xy in centroids]
centroid_df = gpd.GeoDataFrame(geometry=centroid_geometry)
file_path="./Maps_with_python-master/Maps_with_python-master/india-polygon.shp"
india = gpd.read_file(file_path)
fig, ax = plt.subplots(figsize=(10, 10))
india.plot(ax=ax, color='white', edgecolor='black')

colors = ['blue', 'orange', 'green', 'purple', 'brown', 'pink', 'gray', 'olive', 'cyan', 'magenta']
for i in range(number_of_clusters):
    cluster_points = geo_df[np.array(labels) == i]
    cluster_points.plot(ax=ax, marker='o', color=colors[i],markersize=1, label=f'Cluster {i+1}', alpha=0.5)
plt.title('Clusters of Pincodes in Andhra Pradesh on India Map')
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.legend()
plt.grid(True)
plt.show()
import matplotlib.pyplot as plt
from location import Location
from K_means import clustering

ine = []
loc=Location()
for k in range(1, 12):
    ll = clustering(loc.location_coordinate, k)
    _, _, inertia = ll.algo()
    ine.append(inertia)

k_val = range(1, 12)
plt.figure(figsize=(8, 6))
plt.plot(k_val, ine)
plt.xlabel("Number of Clusters (k)")
plt.ylabel("Inertia")
plt.title("Finding the Elbow")
plt.grid(True)
plt.show()


















