# sat-image-processing

This repository contains an early, in progress notebook and small scripts for exploring vegetation change using NASA NDVI raster data.

What the notebook does
- Load NDVI rasters for two dates and replace placeholder values with nodata.
- Compute the pixel wise NDVI difference and visualize maps and histograms.
- Define continent bounding boxes and extract per-continent NDVI difference windows. These are stored in variables such as `ndvi_Africa`, `ndvi_Asia`, and so on.
- Produce per-continent histograms and compute basic statistics including mean, skewness, and kurtosis.

Status
This project is early. The notebook is exploratory and shows initial data cleaning, global difference calculation, and simple per-continent analysis.

How to use
1. Open `main.ipynb` and run the cells in order. The notebook contains sections for reading the NDVI files, cleaning sentinel values, computing the difference, creating continent windows, plotting histograms, and computing simple statistics.
2. Typical Python packages used in the notebook include `rasterio`, `numpy`, `matplotlib`, `seaborn`, `scipy`, and `pandas`.

Notes and limitations
- The per-continent windows use simple lon/lat bounding boxes. Area estimates are approximate until the rasters are reprojected to an equal area CRS.
- Thresholds and basic cleaning are for exploration. Validate results before using them in any reporting.

Next steps (short list)
- Reproject difference rasters to an equal area CRS and compute accurate area lost or gained.
- Implement thresholding and morphological cleaning to produce robust loss and gain masks.
- Add per-polygon aggregation (for example country or protected area polygons) and export CSV summaries.
- Add a `requirements.txt` and a short usage note for reproducibility.

License
No license is included yet. Add one if you plan to publish or share the work.

