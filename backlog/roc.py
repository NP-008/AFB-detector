from keras.preprocessing.image import ImageDataGenerator
from keras.applications import Xception, InceptionV3
from keras.layers import Dense
from keras.models import Model
from PIL import Image

# test set for 32 = 241*2 and 64 = 179
BATCH_SIZE = 1
HEIGHT = 64
WIDTH = 64
STEP = 179

datagen = ImageDataGenerator(rescale=1./255)
validation_generator = datagen.flow_from_directory('tile/64/test',
                                                   target_size = (HEIGHT, WIDTH),
                                                   batch_size=BATCH_SIZE,
                                                   class_mode='binary'
                                                   shuffle=False)

validation_generator.class_indices
validation_generator.classes
validation_generator.filenames

base_model = Xception(include_top=False, pooling='avg')
for layer in base_model.layers:
  layer.trainable = True
output = Dense(1, activation = 'sigmoid')(base_model.output)
model = Model(base_model.input, output)

model.load_weights('model/64/Xception/xnception-07-0.89.h5')

pred_prob = model.predict(validation_generator, verbose=1)

for d in os.listdir('tile/32/test'):
    for
