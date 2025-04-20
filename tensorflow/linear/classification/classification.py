# %% 
import tensorflow as tf
print(tf.__version__)
                        
# %%
from sklearn.datasets  import load_breast_cancer

# %%
data = load_breast_cancer()

# %%
data.keys()

# %%
data.target # Since there are binary values, this is 2 dimentional classification.

# %%
data.feature_names

# %%
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(data.data, data.target, test_size=0.33)

# %%
N,D = x_train.shape
N,D  # Which means there are 381 samples in the train set.

# %%
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
x_train = scaler.fit_transform(x_train)
x_test = scaler.transform(x_test)

# %%
model = tf.keras.models.Sequential([
    tf.keras.layers.Input(shape=(D,)),
    tf.keras.layers.Dense(1, activation='sigmoid')
])

# Alternative step of above code
# model = tf.keras.models.Sequential()
# model.add(tf.keras.layers.Dense(1, input_shape=(D,), activation='sigmoid'))

# %%
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# %%
r = model.fit(x_train, y_train, validation_data=(x_test, y_test), epochs=100)

# %%
print("Test score", model.evaluate(x_test, y_test))

# %%
import matplotlib.pyplot as plt
plt.plot(r.history['loss'], label='loss')
plt.plot(r.history['val_loss'], label='val_loss')
plt.legend();

# %%
plt.plot(r.history['accuracy'], label='acc')
plt.plot(r.history['val_accuracy'], label='val_acc')
plt.legend();




