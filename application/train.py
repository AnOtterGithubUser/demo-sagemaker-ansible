from sklearn.datasets import make_regression
import tensorflow as tf
from dclick import command_with_config
from click import option


@command_with_config('dclick_config.yml')
@option('--epochs', type=int)
@option('--samples', type=int)
def run_training(epochs, samples):

    X, y = make_regression(n_samples=samples)

    model = tf.keras.Sequential()
    model.add(tf.keras.layers.Dense(64, input_dim=100, activation="relu"))
    model.add(tf.keras.layers.Dense(32, activation="relu"))
    model.add(tf.keras.layers.Dense(1))
    model.compile(loss="mean_squared_error", optimizer="Adam", metrics=["accuracy"])

    model.fit(X, y, epochs=epochs)

    model.save("/opt/ml/model/")

if __name__ == '__main__':
    run_training()
