from sklearn.linear_model import linearRegression
from sklearn.datasets import load_diabetes

# loading of data
data = load_diabetes()
X = data.data
y = data.target

#train a regression model
model = LinearRegresssion()
model.fit(X,y)

#predict on the first 5 samples
print(model.predict(x[:5]))

