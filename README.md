BREAD: Better Regressive Estimation of Asteroid Diameter

What happens if an asteroid hits the earth? Well, the damage it would do heavily depends on the size of said asteroid. However, determining the diameter of an asteroid turns out to be harder than you would expect; they are typically not perfectly round and way too far away and large to measure manually. NASA currently has an exponential formula to determine asteroid diameter using the measured albedo and absolute magnitude of an asteroid, but there are several issues that arise with this formula. It assumes the asteroid is a spherical object with a uniform surface (i.e., no albedo variation)​ and since it is only dependent on two values, errors in measurement can lead to significant inaccuracy in diameter (often a factor of 2+)​.

We set out to create a machine learning algorithm to better predict the diameter of an asteroid based on additional measured parameters. We used a dataset from NASA’s Jet Propulsion Laboratory maintained by the California Institute of Technology that includes twenty-seven different parameters (i.e., name, diameter, eccentricity, etc.) of almost 800,000 different asteroids.

We noticed that there were certain parameters that were missing values for the majority of the asteroids. Similarly, there were certain asteroids that had barely any data. We decided to take out the missing data points and cut our dataset down to 11 features for 126,713 asteroids, all of which had a known diameter so they could be used to train our algorithm.

After processing the data to exclude outliers and parameters with little correlation, we created four machine learning models: a multilayer perceptron neural network, a random forest algorithm, a linear regression, and a k-Nearest Neighbours algorithm. In order to have the test data be a random sample of the dataset, we shuffled the data before splitting it into train and test data. As a result, the test data is a different set of data points each time the program is run and, therefore, the accuracy metrics of each model vary slightly with each run. Overall, however, the values are relatively consistent. After displaying the metrics for each model as well as plotting the real output values against the predicted outputs, we can conclude that the multilayer perceptron provides the most accurate predictions. The average values of accuracy metrics for each of our machine learning models can be viewed in the data analysis file.

As can be observed by the accuracy metrics, our best model was the multilayer perceptron neural network with a coefficient of determination of 0.96. To compare our model’s accuracy to that of NASA’s formula, we used NASA’s formula to calculate the diameter of each asteroid in our dataset (given albedo and absolute magnitude) and compared those values to the measured diameters. We then compared the accuracy of NASA’s formula to that of our machine learning model. Those accuracy metrics can be viewed in the data analysis file.

Overall, our model’s performance and accuracy is on par with NASA’s formula for diameter (i.e., our coefficient of determination is slightly higher) and uses more features, so it is less prone to being skewed by unreliable measurements.