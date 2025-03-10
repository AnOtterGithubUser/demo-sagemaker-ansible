from sklearn.datasets import make_regression
import tensorflow as tf
from dclick import command_with_config
from click import option, argument


@command_with_config("/opt/ml/code/dclick_config.yml")
@argument("cmd")
@option("--epochs", type=int)
@option("--samples", type=int)
def run_training(cmd, epochs, samples):
    print("SageMaker specified cmd %s" % cmd)
    print("Number of epochs: %s" % epochs)
    print("Number of samples: %s" % samples)
    X, y = make_regression(n_samples=samples)

    model = tf.keras.Sequential()
    model.add(tf.keras.layers.Dense(64, input_dim=100, activation="relu"))
    model.add(tf.keras.layers.Dense(32, activation="relu"))
    model.add(tf.keras.layers.Dense(1))
    model.compile(loss="mean_squared_error", optimizer="Adam", metrics=["accuracy"])

    model.fit(X, y, epochs=epochs)

    model.save("/opt/ml/model/")


if __name__ == "__main__":
    run_training()
