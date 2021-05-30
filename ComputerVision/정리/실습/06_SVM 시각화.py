import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.svm import SVC

# %%
# Part 1
# 1번
from sklearn.datasets import make_blobs
# two group을 위해 centers = 2
X, y = make_blobs(n_samples = 100, centers = 2, cluster_std = 1.2, random_state = 40)

plt.scatter(X[:, 0], X[:, 1], c = y, edgecolor = 'k')
plt.show()

# %%
# 2번
from sklearn.model_selection import train_test_split

# Train
model = SVC(kernel = 'linear', C = 10)  
model.fit(X, y)

def SVC_decision_plot(model, ax = None, plot_support = True):
    if ax is None:
        ax = plt.gca()
    xlim = ax.get_xlim()
    ylim = ax.get_ylim()
    
    # grid 표시
    x = np.linspace(xlim[0], xlim[1], 30)
    y = np.linspace(ylim[0], ylim[1], 30)
    Y, X = np.meshgrid(y, x)
    xy = np.vstack([X.ravel(), Y.ravel()]).T
    Z = model.decision_function(xy).reshape(X.shape)
    
    # margin에 따른 decision boundary 표시
    ax.contour(X, Y, Z, colors='k',
               levels = [-1, 0, 1], alpha = 0.5,
               linestyles = ['--', '-', '--'])
    
    ax.set_xlim(xlim)
    ax.set_ylim(ylim)
    
plt.scatter(X[:, 0], X[:, 1], c = y, edgecolor = 'k')
# 해당하는 것들 표시
plt.scatter(model.support_vectors_[:, 0], model.support_vectors_[:, 1], 
            edgecolor = 'r', facecolors = 'b')

SVC_decision_plot(model)

# %%
# Part 2
# 1번
from sklearn.datasets import make_circles
# make_circle, noise, factor 인자 전달.
X, y = make_circles(n_samples = 100, noise = 0.1, factor = 0.1, random_state = 40)

model = SVC(kernel = 'rbf').fit(X, y)


plt.scatter(X[:, 0], X[:, 1], c = y, edgecolor = 'k')
plt.show()

# %%
# 2번
from mpl_toolkits import mplot3d
from ipywidgets import interact, fixed

# RBF 식 표현
Z = np.exp(-(abs(X)**2).sum(1))

# grid, 시각화를 통해 각도 표현
def plot3D(elev = 45, azim = 45, X = X, y = y):
    ax = plt.subplot(projection = '3d')
    ax.scatter3D(X[:, 0], X[:, 1], Z, c = y, cmap = 'autumn')
    ax.view_init(elev = elev, azim = azim)
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('Z')

# interact, plot3D 함수 이용한 시각화
interact(plot3D, elev = [45, 45], X = fixed(X), y = fixed(y));
# %%
# 3번

model = SVC(kernel = 'rbf', C = 10)
model.fit(X, y)

def SVC_decision_plot(model, ax = None, plot_support = True):
    if ax is None:
        ax = plt.gca()
    xlim = ax.get_xlim()
    ylim = ax.get_ylim()
    
    # grid 표시
    x = np.linspace(xlim[0], xlim[1], 30)
    y = np.linspace(ylim[0], ylim[1], 30)
    Y, X = np.meshgrid(y, x)
    xy = np.vstack([X.ravel(), Y.ravel()]).T
    Z = model.decision_function(xy).reshape(X.shape)
    
    # margin에 따른 decision boundary 표시
    ax.contour(X, Y, Z, colors = 'k',
               levels = [-1, 0, 1], alpha = 0.5,
               linestyles = ['--', '-', '--'])
    
    ax.set_xlim(xlim)
    ax.set_ylim(ylim)
    
plt.scatter(X[:, 0], X[:, 1], c = y, edgecolor = 'k')
# 해당하는 것들 표시
plt.scatter(model.support_vectors_[:, 0], model.support_vectors_[:, 1], 
            edgecolor = 'r', facecolors = 'b')

SVC_decision_plot(model)
