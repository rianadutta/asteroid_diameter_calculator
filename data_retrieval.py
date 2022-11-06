import pandas as pd

asteroid=pd.read_csv('Asteroid.csv')

for p in asteroid:
    asteroid=asteroid[asteroid[p].notnull()]
print(len(asteroid))

asteroid.to_csv('processed.csv')