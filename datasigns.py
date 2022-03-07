import csv
import plotly.express as px
rows = []
with open("main.csv","r") as f:
    csvreader = csv.reader(f)
    for row in csvreader:
        rows.append(row)
headers = rows[0]
planetdata = rows[1:]
headers[0] = "row_num"
##print(headers)
##print(planetdata[0])
solarSystemPlanetCount = {}
for data in planetdata:
    if solarSystemPlanetCount.get(data[11]):
        solarSystemPlanetCount[data[11]]+=1
    else:
        solarSystemPlanetCount[data[11]]=1
##print(solarSystemPlanetCount)
maxSolarSystem = max(solarSystemPlanetCount,key=solarSystemPlanetCount.get)
##print(solarSystemPlanetCount[maxSolarSystem],maxSolarSystem)
koi_351_planets = []
for data in planetdata:
    if maxSolarSystem == data[11]:
        koi_351_planets.append(data)
##print(koi_351_planets, len(koi_351_planets))

temp_planetdata = list(planetdata)
for planet_data in temp_planetdata:
  planet_mass = planet_data[3]
  if planet_mass.lower() == "unknown":
    planetdata.remove(planet_data)
    continue
  else:
    planet_mass_value = planet_mass.split(" ")[0]
    planet_mass_ref = planet_mass.split(" ")[1]
    if planet_mass_ref == "Jupiters":
      planet_mass_value = float(planet_mass_value) * 317.8
    planet_data[3] = planet_mass_value

  planet_radius = planet_data[7]
  if planet_radius.lower() == "unknown":
    planetdata.remove(planet_data)
    continue
  else:
    planet_radius_value = planet_radius.split(" ")[0]
    planet_radius_ref = planet_radius.split(" ")[2]
    if planet_radius_ref == "Jupiter":
      planet_radius_value = float(planet_radius_value) * 11.2
    planet_data[7] = planet_radius_value

print(len(planetdata))

hd_10180_planets = []
for planet_data in planetdata:
  if maxSolarSystem == planet_data[11]:
    hd_10180_planets.append(planet_data)

##print(len(hd_10180_planets))
##print(hd_10180_planets)

koi_351_mass = []
koi_351_name = []

for data in hd_10180_planets:
    koi_351_mass.append(data[3])
    koi_351_name.append(data[1])
 
    koi_351_mass.append(1)
    koi_351_name.append('Earth')

fig = px.bar(x = koi_351_name, y = koi_351_mass)
##fig.show()

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
