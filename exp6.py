import pandas as pd
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.feature as cfeature

print("="*60)
print("GEOGRAPHIC DATA VISUALIZATION")
print("="*60)


cities = {
    'City': ['New York','London','Tokyo','Mumbai','Sydney'],
    'Latitude': [40.7,51.5,35.6,19.0,-33.8],
    'Longitude': [-74.0,-0.1,139.7,72.8,151.2],
    'Population': [8,9,13,20,5]
}

df = pd.DataFrame(cities)

earthquake = {
    'Latitude':[35,40,-23,19,38],
    'Longitude':[138,-112,-46,77,142],
    'Magnitude':[6.5,5.2,4.8,7.1,6.8]
}

df_eq = pd.DataFrame(earthquake)


plt.figure(figsize=(10,6))
ax = plt.axes(projection=ccrs.PlateCarree())

ax.add_feature(cfeature.LAND)
ax.add_feature(cfeature.OCEAN)
ax.add_feature(cfeature.COASTLINE)

ax.scatter(df['Longitude'], df['Latitude'],
           s=df['Population']*30,
           c=df['Population'],
           cmap='Reds',
           transform=ccrs.PlateCarree())

for i in range(len(df)):
    ax.text(df['Longitude'][i], df['Latitude'][i],
            df['City'][i],
            transform=ccrs.PlateCarree())

plt.title("World Map - Cities")
plt.show()


plt.figure(figsize=(8,6))
ax = plt.axes(projection=ccrs.PlateCarree())

ax.set_extent([-130,-60,20,55])
ax.add_feature(cfeature.LAND)
ax.add_feature(cfeature.COASTLINE)


ax.scatter([-74,-118],[40,-34],
           color='red',
           s=200,
           transform=ccrs.PlateCarree())

plt.title("North America Map")
plt.show()


plt.figure(figsize=(10,6))
ax = plt.axes(projection=ccrs.PlateCarree())

ax.add_feature(cfeature.LAND)
ax.add_feature(cfeature.COASTLINE)

ax.scatter(df_eq['Longitude'], df_eq['Latitude'],
           s=df_eq['Magnitude']*50,
           c=df_eq['Magnitude'],
           cmap='YlOrRd',
           transform=ccrs.PlateCarree())

plt.title("Earthquake Distribution")
plt.show()

print("\nVisualization Completed")