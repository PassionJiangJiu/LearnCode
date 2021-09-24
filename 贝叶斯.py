import sklearn
from sklearn import datasets
from sklearn.model_selection import train_test_split #对数据集进行切分

iris = sklearn.datasets.load_iris()
X = iris.data  # 数据集
Y = iris.target  # 相应类别标签
X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.2, random_state=0)

