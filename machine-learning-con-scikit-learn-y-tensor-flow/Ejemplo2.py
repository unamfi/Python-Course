from sklearn.datasets import load_iris

iris = load_iris()

print(iris.feature_names)
print(iris.target_names)

print(iris.data[0])
print(iris.target[0])

# 0 -> Setosa
# 1 -> Versicolor
# 2 -> Virginica

for i in range(len(iris.target)):
    print("Dato %d: label %s, features %s"%(i, iris.target[i], iris.data[i]))
    
