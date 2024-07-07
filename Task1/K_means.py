import numpy as np

class clustering:
    def __init__(self,location_coordinates,k):
        self.location_coordinates=location_coordinates
        self.k=k
        self.max_iters=100
        self.centroid = self.location_coordinates[np.random.choice(self.location_coordinates.shape[0], k, replace=False)]
        self.centroid = self.centroid.astype(float)
    def algo(self):
        for o in range(self.max_iters):
            dis = np.sqrt(((self.location_coordinates - self.centroid[:, np.newaxis]) ** 2).sum(axis=2))
            self.lab = dis.argmin(axis=0)
            self.new = [self.location_coordinates[self.lab == i].mean(axis=0) for i in range(self.k)]

            self.new = np.array(self.new)
            if np.all(self.centroid == self.new):
                break
            self.centroid = self.new
        self.inertia = 0
        for i in range(self.k):
            cluster_points = self.location_coordinates[self.lab == i]
            cluster_inertia = np.sum((cluster_points - self.centroid[i]) ** 2)
            self.inertia += cluster_inertia
        return self.centroid.tolist(), self.lab.tolist(),self.inertia

