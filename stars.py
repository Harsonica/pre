import pandas as pd
import csv

df = pd.read_csv("final.csv")

del df["luminosity"]
del df["Nun"]

            }, axis='columns')

df.to_csv('main.csv') 

temp_planetdata = list(planetdata)
for planet_data in temp_planetdata:
  if planet_data[1].lower() == "hd 100546 b":
    planetdata.remove(planet_data)

planet_masses = []
planet_radiuses = []
planet_names = []
for planet_data in planetdata:
  planet_masses.append(planet_data[3])
  planet_radiuses.append(planet_data[7])
  planet_names.append(planet_data[1])
planet_gravity = []
for index, name in enumerate(planet_names):
  gravity = (float(planet_masses[index])*5.972e+24) / (float(planet_radiuses[index])*float(planet_radiuses[index])*6371000*6371000) * 6.674e-11
  planet_gravity.append(gravity)

fig = px.scatter(x=planet_radiuses, y=planet_masses, size=planet_gravity, hover_data=[planet_names])
##fig.show()

low_gravity_planets = []
for index, gravity in enumerate(planet_gravity):
  if gravity < 10:
    low_gravity_planets.append(planetdata[index])
    print(len(low_gravity_planets))


planet_type_values = []
for planet_data in planetdata:
    planet_type_values.append(planet_data[6])

##print(list(set(planet_type_values)))

planet_masses = []
planet_radiuses = []
for planet_data in low_gravity_planets:
    planet_masses.append(planet_data[3])
    planet_radiuses.append(planet_data[7])

fig = px.scatter(x=planet_radiuses,y=planet_masses)
##fig.show()

from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import seaborn as sns
x = []
for index, planet_mass in enumerate(planet_masses):
    temp_list = [planet_radiuses[index],planet_mass]
    x.append(temp_list)

wcss = []
for i in range(1,11):
    kmeans = KMeans(n_clusters = i, init = 'k-means++',random_state = 42)
    kmeans.fit(x)
    wcss.append(kmeans.inertia_)

plt.figure(figsize=(10,5))
sns.lineplot(range(1,11),wcss,marker = 'o',color = 'red')
plt.title('the elbow method')
plt.xlabel('number of clusters')
plt.ylabel('wcss')
##plt.show()

planet_masses = []
planet_radiuses = []

planet_types = []
for planet_data in low_gravity_planets:
    planet_masses.append(planet_data[3])
    planet_radiuses.append(planet_data[7])
    planet_types.append(planet_data[6])

fig = px.scatter(x=planet_radiuses,y=planet_masses, color = planet_types)
##fig.show()

suitable_planets_1 = []
for planet_data in low_gravity_planets:
    if planet_data[6].lower()=="terrestrial" or planet_data[6].lower()=="super earth":
        suitable_planets_1.append(planet_data)
print(len(suitable_planets_1))
