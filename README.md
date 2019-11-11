# NCTU_DeepLearning
Text Book: https://www.deeplearningbook.org

Mentioned software:
python, numpy, sklearn, tensorflow, keras

google colab


## Week01-Week02 Introduction and Feedforward networks
slides: 
* https://drive.google.com/a/nctu.edu.tw/file/d/1VTuiNdYzNJ6KRDWKPI6B-lVUNhZwKKF1/view?usp=sharing
* https://drive.google.com/a/nctu.edu.tw/file/d/1mQgQlqh2x3MgrOCBt7XMYG4nw29upGyR/view?usp=sharing
* https://drive.google.com/file/d/1gpG9-btRo0LyLn8r8aaOozo0eOvgPMKh/view?usp=sharing


### Coursework
 submit form: https://docs.google.com/forms/d/e/1FAIpQLScGgaTCzsXwxhuxizLduURIBNGlOgedYCOb5gkJYwsHoAouRA/viewform
 
 Please submit .ipynb files

* Use nearest neighbor method to do handwritten digit recognition
* (Optional) Use PCA to speed up the above method
* Handcraft a feedforward neural network that solves the problem of
    * input a binary representation of a number and classify by it's remainder when divided by 4 (with 100% accuracy)
    * input a binary representation of a number and classify by it's remainder when divided by 3 (with high accuracy)
    * input is a 3x3 board, each cell is either white or black. Check whether there are any 3 white cell are in a row (like the game tic-tac-toe)


See https://github.com/tjwei/CrashCourseML
* Basic_ML/01-From NumPy to MNIST.ipynb
* DIY_NN/01-FeedForward-Forward Propagation.ipynb



## Week03 Cost function and Gradient Descent
* ipynb: https://github.com/tjwei/CrashCourseML/blob/master/DIY_NN/02-FeedForward-Backpropagation.ipynb
* Ian Goodfellow's slides: http://www.deeplearningbook.org/slides/sgd_and_cost_structure.pdf
Coursework (use new E3 to submit your work)
* Use numpy to write simple neural networks and use a gradient descent algorithm to train it for classifying  digits in the MNIST dataset.
    * Using cross-entropy loss
    * Using mean-square-error loss

## Week04 CNN and Using tensorflow 2.0
* Train a neural network to classify digits in the MNIST dataset.
* Train a neural netowork to classify classes in the cifar10 dataset.

## Week05 Convolution and convolution transpose
* Handcraft a CNN network to generate the next step of the game of life.

## Week06 More Techniques
* gradient descent based optimizers: http://ruder.io/optimizing-gradient-descent/index.html
* Batch normalization: https://en.wikipedia.org/wiki/Batch_normalization   https://arxiv.org/pdf/1502.03167v3.pdf
* Overfitting
* Dropout: http://jmlr.org/papers/volume15/srivastava14a/srivastava14a.pdf
* network in network: https://arxiv.org/pdf/1312.4400.pdf
* Resnet: https://arxiv.org/pdf/1512.03385.pdf

# Week07 Optimization, RNN
* http://www.deeplearningbook.org/contents/optimization.html
* http://www.deeplearningbook.org/contents/rnn.html
* https://colah.github.io/posts/2015-08-Understanding-LSTMs/
* https://www.tensorflow.org/tutorials/text/text_classification_rnn

# Week09 Applications
* slides: [Deep Learning Week 09.pdf](Deep%20Learning%20Week%2009.pdf)


# Week12 Reinforcement Learning:
* Book: http://incompleteideas.net/book/bookdraft2017nov5.pdf
