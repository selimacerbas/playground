# %%
  import tensorflow as tf

# %%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams["figure.figsize"] = (10, 6)
plt.rcParams["figure.dpi"] = 600

# %%
!wget https://raw.githubusercontent.com/lazyprogrammer/machine_learning_examples/master/tf2.0/moore.csv

# %%
!head moore.csv

# %%
data = pd.read_csv('moore.csv', header=None).to_numpy()

# %%
data

# %%
x = data[:,0].reshape(-1,1) # making an N x D
y = data[:,1]

# %%
plt.scatter(x, y);


# %% 
y = np.log(y)
plt.scatter(x,y);

# %%
x = x - x.mean()

# %%
import keras

# %%
model = keras.models.Sequential([
    keras.layers.Input(shape=(1,)),
    keras.layers.Dense(1),
])

# %%
model.compile(
    optimizer= keras.optimizers.SGD(0.001,0.9),
        loss='mse',
)

# %%
def scheduler(epoch, lr):
    if epoch >= 50:
        return 0.0001
    return 0.001
scheduler = keras.callbacks.LearningRateScheduler(scheduler)

# %%
r = model.fit(x, y, epochs=200, callbacks=[scheduler])

# %%
plt.plot(r.history['loss'], label='loss')
plt.legend();

# %%
model.layers

# %%
model.layers[0].get_weights()

# %%
a = model.layers[0].get_weights()[0][0,0]

# From here Math starts.

# %%
print("Time to double:", np.log(2) / a)

# %%
# If you know the analytical solution
x = np.array(x).flatten()
y = np.array(y)
denominator = x.dot(x) - x.mean() * x.sum()
a = ( x.dot(y) - y.mean()*x.sum() ) / denominator
b = ( y.mean() * x.dot(x) - x.mean() * x.dot(y) ) / denominator
print(a, b)
print("Time to double:", np.log(2) / a)

# %%
# Make sure the line fits our data
yhat = model.predict(x).flatten()
plt.scatter(x, y)
plt.plot(x, yhat)

# %%
# Manual calculation
# Get the weights
w, b = model.layers[0].get_weights()

# Reshape X because we flattened it again earlier
x = x.reshape(-1, 1)

# (N x 1) x (1 x 1) + (1) --> (N x 1)
yhat2 = (x.dot(w) + b).flatten()

# Don't use == for floating points
np.allclose(yhat, yhat2)
