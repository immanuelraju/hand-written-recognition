import matplotlib.pyplot as plt
%matplotlib inline
import pylab as pl
from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
from sklearn import svm
digits = load_digits()
pl.gray()
pl.matshow(digits.images[5])
pl.show()
digits.images[14]
images_and_labels=list(zip(digits.images,digits.target))
plt.figure(figsize=(5,5))
for index, (image,label) in enumerate (images_and_labels[:12]):
    plt.subplot(3,5,index+1)
    pl.axis('off')
    plt.imshow(image,cmap=plt.cm.gray_r,interpolation='nearest')
    plt.title('%i' % label)
n_samples=len(digits.images)
print(n_samples)
X=digits.images.reshape(n_samples,-1)
Y=digits.target
X_train,X_test,Y_train,Y_test=train_test_split(X,Y)
print(X_train.shape)
print(X_test.shape)
model_linear=svm.SVC(kernel='linear',degree=3,gamma='scale')
model_linear.fit(X_train,Y_train)
Y_pred =model_linear.predict(X_test)
model_linear.score(X_test,Y_test)
model_RBF=svm.SVC(degree=3,gamma='scale',kernel='rbf')
model_RBF.fit(X_train,Y_train)
Y_pred2=model_RBF.predict(X_test)
model_RBF.score(X_test,Y_test)
from sklearn.metrics import classification_report
predictions=model_linear.predict(X_test)
print(classification_report(Y_test,predictions))
