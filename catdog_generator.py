from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, Flatten, Conv2D, MaxPooling2D
from tensorflow.keras.preprocessing.image import ImageDataGenerator

DATASET_DIR ="/home/pi/Desktop/opencv/data/cat_dog/train/"
BATCH_SIZE = 16

datagen = ImageDataGenerator(validation_split =0.1, rescale=1./255)

train_generator = datagen.flow_from_directory(
    DATASET_DIR,
    target_size = (150,150),
    batch_size = BATCH_SIZE,
    class_mode = "binary",
    subset = "training"
    )


test_generator = datagen.flow_from_directory(
    DATASET_DIR,
    target_size = (150,150),
    batch_size = BATCH_SIZE,
    class_mode = "binary",
    subset = "validation"
    )

#print(train_gen.class_indices)

model = Sequential()
model.add(Conv2D(filters=64,kernel_size=4,padding="same",activation="relu",input_shape=(150,150,3)))
model.add(MaxPooling2D(pool_size=4,strides=4))
model.add(Dropout(0.5))#perc nodi da spegnere
model.add(Conv2D(filters=32,kernel_size=2,padding="same",activation="relu"))
model.add(MaxPooling2D(pool_size=4,strides=4))
model.add(Dropout(0.5))#perc nodi da spegnere
model.add(Flatten())
model.add(Dense(256,activation="relu"))
model.add(Dropout(0.5))#perc nodi da spegnere
model.add(Dense(1,activation="sigmoid"))


model.compile(optimizer="adam",loss="binary_crossentropy",metrics=["accuracy"])

model.fit(train_generator, epochs=50)

metrics_train = model.evaluate(train_generator)
metrics_test = model.evaluate(test_generator)

print("Train Accuracy = %.4f - Train loss = %.4f" % metrics_train[1], metrics_train[0])
print("Test Accuracy = %.4f - Test loss = %.4f" % metrics_test[1], metrics_test[0])

model.save("mod_gen_cat_dog.h5")
