#!/usr/bin/env python
# coding: utf-8

#%%
import numpy as np
import rasterio
import stac
from matplotlib import pyplot

#%%
s = stac.STAC('http://brazildatacube.dpi.inpe.br/bdc-stac/0.8.0/', True)

#%%
s.catalog

#%%
collection = s.collection('C4_64_16D_MED')
collection

#%%
items = collection.get_items()
items

#%%
items.features[0].assets

#%%
red = items.features[0].assets['red'].download()
green = items.features[0].assets['green'].download()
blue = items.features[0].assets['blue'].download()

red

#%%
r = rasterio.open(red).read(1)
g = rasterio.open(green).read(1)
b = rasterio.open(blue).read(1)


#%%
r.max()

#%%
def normalize(array):
    """Normalizes numpy arrays into scale 0.0 - 1.0"""
    array_min, array_max = array.min(), array.max()
    return ((array - array_min)/(array_max - array_min))

#%%
rgb = np.dstack((normalize(r), normalize(g), normalize(b)))
pyplot.imshow(rgb)
