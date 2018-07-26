# Gleam

![Prediction of the population density in Colombia in 2017 as generated by a neural network](https://i.imgur.com/Sx5v52M.png "Prediction of the population density in Colombia in 2017 as generated by a neural network")

This project was done as part of a bachelor's thesis at HEIG-VD.
It is a collection of notebooks that were used to explore different types of geographical data. They also enable the user
to train a convolutional neural network that predicts the population density of a region with a high level of detail (250-1000m)
from nightime satellite imagery.

# Requirements

- python 3.7

# Installation

On Windows, some scientific packages have some compatibility issues. Those are `shapely`, `gdal`, `fiona`, and `rasterio`.
Download them from [Christoph Gohlke's website](https://www.lfd.uci.edu/~gohlke/pythonlibs/) and manually install them
(use `pip install packagename.whl`).

Then, on both Windows and Linux, use the command line `pip install -r requirements.txt` from the project's root folder.

(optional) In order to enable training on the GPU, follow the [TensorFlow tutorial](https://www.tensorflow.org/install/)
of your platform under "Requirements to run TensorFlow with GPU support".

# Usage

Use the command `python -m notebook` to browse notebooks on Windows, or `jupyter notebook` on Linux.

# Notebooks
Each notebook can be found in the folder with the notebook's name.

## country_stats
This set of scripts computes the sum of light perceived from space for each country, and compares these values with 
other miscellaneous per country data. This was only useful for data exploration.

## gleam
This notebook preprocesses a raster with two bands : nighttime satellite picture and population density raster. It is
then used to train a convolutional neural network that makes high resolution predictions for population density from another
satellite picture.

## rastercomparator
This notebook compares two rasters to either compile a scatterplots of the values of each pixel, or compile the difference
between two rasters in order to visualize the evolution from one year to the next for example.

## scraper
This notebook downloads and assembles tiles from [NASA's GIBS API](https://wiki.earthdata.nasa.gov/display/GIBS/GIBS+API+for+Developers). There really is no point in using this now.

## viirs_extractor
This notebook answers to the specific need to extract the huge quantity of
[nighttime data from the NOAA](https://ngdc.noaa.gov/eog/viirs/download_dnb_composites.html) and compile yearly rasters
from monthly rasters.
