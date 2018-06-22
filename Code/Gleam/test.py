import rasterio
import numpy as np
import keras.models as models
import sys
from utils import preprocess

input_tile_size = 32
outputs_per_tile = 1

if len(sys.argv) < 2:
    print('Missing argument : use model name as argument ("2018-06-18_18-18-40.h5" for example)')
    exit(0)

print('loading model')
arg = sys.argv[1].strip('-\x93\x96')
cnn = models.load_model('models/' + arg)

print('opening raster')

testX, testY = preprocess(rasterio.open('../../Data/lightpop_merged/2005.tif'), input_tile_size, 8)
testX = np.expand_dims(testX, axis=3)

print('mean pop in tiles : ' + str(np.mean(testY)))
print('pop standard deviation in tiles : ' + str(np.std(testY)))

print('testing ...')

evaluation = cnn.evaluate(testX, testY, verbose=2, batch_size=1024)

print(dict(zip(cnn.metrics_names, evaluation)))

print('done !')
