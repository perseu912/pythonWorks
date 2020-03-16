#Reinan Br 10:09 25/02/2020
#remasterizando um exemplo de uma rede neural em python

import numpy as np
#from videoSupport import *
from scipy import optimize

class Neural_Network(object):
	def __init__(self):
		#definindo parametros
		self.inputLayerSize = 2
		self.outputLayerSize = 1
		self.hiddenLayerSize = 3
		self.lambd = 0.0001
		#pesos (weights)
		self.W1 = np.random.randn(self.inputLayerSize,self.hiddenLayerSize)
		self.W2 = np.random.randn(self.hiddenLayerSize,self.outputLayerSize)
				
	def forward(self, X):
		#propagação dos inputs na rede neural
		self.z2 = np.dot(X, self.W1)
		self.a2 = self.sigmoid(self.z2)
		self.z3 = np.dot(self.a2, self.W2)
		yHat = self.sigmoid(self.z3)
		return yHat
			
	def sigmoid(z):
		#funçao sigmoid para derivação da resposta
		return 1/(1+exp(-z))
		
	def sigmoidPrime(z):
		#derivada da função sigmoid
		return np.exp(z)/((1+np.exp(-z))**2)
		
	def costFunction(self,X,y):
		self.yHat = self.forward(X)
		J = 0.5*sum((y-self.yHat)**2)/X.shape[0]+(self.lambd/2)*(sum(self.W1**2)+sum(self.W2**2))
		return J
		
	def costFunctionPrime(self, X, y):
		#computando derivadas em respeito à W1 e W2
		self.yHat = self.forward(X)
		
		delta3 = np.multiply(-(y-self.yHat), self.sigmpidPrime(self.z3))
		dJdW2 = np.dot(self.a2.T, delta3) + self.lambd*self.W2
		
		delta2 = np.dot(delta3, self.W2.T)*self.sigmoidPrime(self.z2)
		dJdW1 = np.dot(X.T, delta2) + self.lambd*self.W1
		
		return dJdW1, dJdW2
	
	#funções auxiliares para interação usando outros metodos/classes	
	def getParams(self):
		#pega W1 i W2 e os transforma em vetores
		params = np.concatenate(self.W1.ravel(), self.W2.ravel())
		return params
		
	def setParams(self, params):
		#juntando W1 i W2 usando um unico parâmetro de vetor
		W1_start = 0
		W1_end = self.hiddenLayerSize*self.inputLayerSize
		self.W1 = np.reshape(params[W1_start:W1_end],(self.inputLayerSize,self.hiddenLayerSize))
		W2_end = W1_end + self.hiddenLayerSize*self.outputLayerSize
		self.W2 = np.reshape(params[W1_end:W2_end],(self.hiddenLayerSize,self.outputLayerSize))
		
	def computeGradient(self, X, y):
		dJdW1 , dJdW2 = self.costFunctionPrime(X,y)
		return np.concatenate((dJdW1.ravel(),dJdW2.ravel()))
			
			


class Trainer:
	def __init__(self, N):
		self.N = N
		
	def costFunctionWrapper(self, params, X, y):
		self.N.setParams(params)
		cost = self.N.costFunction(X,y)
		grad = self.N.computeGradients(X,y)
		return cost, grad
		
	def callbackF(self, params):
		self.N.setParams(params)
		self.J.append(self.N.costFunctions(self.X, self.y))
		
	def train(self,X,y):
		self.X = X
		self.y = y
		
		self.J = []
		
		params0 = self.N.getParams()
		
		options = {'maxiter':200, 'disp':True}
		_res = optimize.minimize(self.costFunctionWrapper,params0,jac=True,method='BFGS',args=(X,y),options=options,callback=self.callbackF)
		
		self.N.setParams(_res.x)
		self.optimizationResults = _res		
		
		