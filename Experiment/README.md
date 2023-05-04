**MNIST Convolutional Neural Network Example** <br>

**About the Model Mnist** <br>

This code trains a simple convolutional neural network (convnet) on the MNIST dataset. The goal of the model is to recognize handwritten digits from 0 to 9. The input images are 28x28 grayscale images of digits, and the output of the model is a probability distribution over the 10 classes (0 to 9). The convnet architecture consists of two 2D convolutional layers with ReLU activation, followed by max pooling and dropout layers. The output of the second convolutional layer is then flattened and passed through two dense layers with ReLU and softmax activations. The model is trained using the Adadelta optimizer and categorical cross-entropy loss. The final model achieves a test accuracy of 99.25% after 12 epochs. The frozen model is saved in a pb file and the trained Keras model is saved as an H5 file.

This is an example of training a simple Convolutional Neural Network on the MNIST dataset using Keras. 
The model achieves a test accuracy of 99.25% after 12 epochs, but there is still room for parameter tuning.

**Requirements**<br>

- Python 3.x
- Keras
- TensorFlow

To train the model, run the following command: <br>

`python train.py --epochs 12 --batch_size 128`


