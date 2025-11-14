import rasterio

with rasterio.open("2015/p126r060_TC_2015.tif") as src:
    data_2015 = src.read(1)  

with rasterio.open("2000/p126r060_TC_2000.tif") as src:
    data_2000 = src.read(1)

import numpy as np

data_2000 = data_2000.astype(float)
data_2015 = data_2015.astype(float) 

data_2000[data_2000 == 255] = np.nan
data_2015[data_2015 == 255] = np.nan

forest_mask_2000 = data_2000 > 30 
forest_mast_2015 = data_2015 > 30

min_height = min(data_2000.shape[0], data_2015.shape[0])
min_width  = min(data_2000.shape[1], data_2015.shape[1])

# Crop both arrays
data_2000_cropped = data_2000[:min_height, :min_width]
data_2015_cropped = data_2015[:min_height, :min_width]

# Now subtraction works
change_map = data_2015_cropped - data_2000_cropped

import matplotlib.pyplot as plt

plt.imshow(change_map, cmap='RdYlGn')
plt.colorbar(label='Change in tree cover %')
plt.show()

plt.figure(figsize=(10, 8))
plt.imshow(data_2000, cmap='RdYlGn', vmin=0, vmax=100)  # 0=red, 100=green
plt.colorbar(label='Tree cover %')
plt.title("Tree Cover 2000")
plt.show()

# Plot 2015
plt.figure(figsize=(10, 8))
plt.imshow(data_2015, cmap='RdYlGn', vmin=0, vmax=100)  # 0=red, 100=green
plt.colorbar(label='Tree cover %')
plt.title("Tree Cover 2015")
plt.show()
