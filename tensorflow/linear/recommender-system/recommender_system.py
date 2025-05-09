# %%
import tensorflow as tf
print(tf.__version__)


# %%
# More imports
from keras._tf_keras.keras.layers import Input, Dense, Embedding, Flatten, Concatenate
from keras._tf_keras.keras.models import Model
from keras._tf_keras.keras.optimizers import SGD, Adam

from sklearn.utils import shuffle

import numpy as np
import matplotlib.pyplot as plt

# %%
!wget -nc http://files.grouplens.org/datasets/movielens/ml-20m.zip

# %% 
!unzip -n ml-20m.zip

# %%
import pandas as pd

# %%
df = pd.read_csv('ml-20m/ratings.csv')
df.head()

# %%
df.userId = pd.Categorical(df.userId)
df['new_user_id'] = df.userId.cat.codes

# %%
df.movieId = pd.Categorical(df.movieId)
df['new_movie_id'] = df.movieId.cat.codes

# %%
user_ids = df['new_user_id'].values
movie_ids = df['new_movie_id'].values
ratings = df['rating'].values

# %%
n = len(set(user_ids))
m = len(set(movie_ids))

k = 10

# %%
# Make a neural network

# User input
u = Input(shape=(1,))

# Movie input
m = Input(shape=(1,))

# User embedding
u_emb = Embedding(n, k)(u) # output is (num_samples, 1, K)

# Movie embedding
m_emb = Embedding(m, k)(m) # output is (num_samples, 1, K)

# Flatten both embeddings
u_emb = Flatten()(u_emb) # now it's (num_samples, K)
m_emb = Flatten()(m_emb) # now it's (num_samples, K)

# Concatenate user-movie embeddings into a feature vector
x = Concatenate()([u_emb, m_emb]) # now it's (num_samples, 2K)

# Now that we have a feature vector, it's just a regular ANN
x = Dense(1024, activation='relu')(x)
# x = Dense(400, activation='relu')(x)
# x = Dense(400, activation='relu')(x)
x = Dense(1)(x)


# %%
# Build the model and compile
model = Model(inputs=[u, m], outputs=x)
model.compile(
  loss='mse',
  optimizer=SGD(learning_rate=0.08, momentum=0.9),
)

# %%
# split the data
user_ids, movie_ids, ratings = shuffle(user_ids, movie_ids, ratings)
Ntrain = int(0.8 * len(ratings))
train_user = user_ids[:Ntrain]
train_movie = movie_ids[:Ntrain]
train_ratings = ratings[:Ntrain]

test_user = user_ids[Ntrain:]
test_movie = movie_ids[Ntrain:]
test_ratings = ratings[Ntrain:]

# center the ratings
avg_rating = train_ratings.mean()
train_ratings = train_ratings - avg_rating
test_ratings = test_ratings - avg_rating


# %%
r = model.fit(
  x=[train_user, train_movie],
  y=train_ratings,
  epochs=25,
  batch_size=1024,
  verbose=2, # goes a little faster when you don't print the progress bar
  validation_data=([test_user, test_movie], test_ratings),
)

# %%
# plot losses
plt.plot(r.history['loss'], label="train loss")
plt.plot(r.history['val_loss'], label="val loss")
plt.legend()
plt.show()

# %%
# is this on par with other approaches?
# https://datascience.stackexchange.com/questions/29740/benchmark-result-for-movielens-dataset
np.sqrt(0.6259)
