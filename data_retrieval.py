import pandas as pd

# retrieve data
asteroid=pd.read_csv('Asteroid.csv')

# preliminarily data processing
for p in asteroid:
    asteroid=asteroid[asteroid[p].notnull()]
print(len(asteroid))

asteroid.to_csv('processed.csv')