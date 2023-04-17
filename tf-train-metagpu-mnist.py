import os
import tensorflow as tf

os.environ['METAGPU_MAX_MEM']
my_variable = os.environ.get('METAGPU_MAX_MEM')
memory_limit = int(my_variable)  # Convert the string to an integer

# Set the limit to GPU memory usage
gpus = tf.config.list_physical_devices('GPU')
if gpus:
    try:
        # Set the memory limit for each GPU
        for gpu in gpus:
            tf.config.set_logical_device_configuration(
                gpu,
                [tf.config.LogicalDeviceConfiguration(memory_limit=memory_limit)])
        print("GPU memory limit set successfully.")
    except RuntimeError as e:
        print("Error setting GPU memory limit:", e)

# Load MNIST dataset
mnist = tf.keras.datasets.mnist
(x_train, y_train), (x_test, y_test) = mnist.load_data()

# Normalize pixel values to [0, 1]
x_train, x_test = x_train / 255.0, x_test / 255.0

# Create TensorFlow model
with tf.device('/GPU:0'):  # Use GPU
    model = tf.keras.models.Sequential([
        tf.keras.layers.Flatten(input_shape=(28, 28)),
        tf.keras.layers.Dense(128, activation='relu'),
        tf.keras.layers.Dropout(0.2),
        tf.keras.layers.Dense(10, activation='softmax')
    ])

# Compile the model
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

# Train the model
model.fit(x_train, y_train, epochs=10, batch_size=4)

# Evaluate the model
model.evaluate(x_test, y_test)
