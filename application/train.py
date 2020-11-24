from sklearn.datasets import make_regression
import tensorflow as tf

X, y = make_regression(n_samples=1000)

model = tf.keras.Sequential()
model.add(tf.keras.layers.Dense(64, input_dim=100, activation="relu"))
model.add(tf.keras.layers.Dense(32, activation="relu"))
model.add(tf.keras.layers.Dense(1))
model.compile(loss="mean_squared_error", optimizer="Adam", metrics=["accuracy"])

model.fit(X, y, epochs=3)
