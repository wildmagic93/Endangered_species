import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

species = pd.read_csv('WILD_LIFE.csv')

countries = species.groupby(by = ['Country', 'Species']).Species.count()

endangered = species.groupby(by = ['Species'])

australia = species[species['Country'] == 'Australia']
endangered_australia = australia['Species']

list_species = np.array(endangered_australia)
unique_species = {}
for el in list_species:
  if el not in list(unique_species.keys()):
    unique_species[el] = 1
  else:
    unique_species[el] += 1

dangered_species = list(unique_species.keys())

ax = plt.subplot()
plt.scatter(x = range(len(dangered_species)), y = list(unique_species.values()))
plt.xlabel('Species')
plt.ylabel('Number of endangered species per category')
plt.title('Endangered species in Australia')
ax.set_xticks(range(len(dangered_species)))
ax.set_xticklabels(dangered_species, rotation = 'vertical')
plt.show()
