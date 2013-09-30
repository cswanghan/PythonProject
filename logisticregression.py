#Logistic Regression classifier class
import numpy as np

'''
Here goes for comment block.
'''

global weights #array initialization
weights=[0 for i in range(3)] #array initialization

class logistic:

	LEARNING_RATE=0.001
	def sigmoid(self, data):
				l = self.classify(data, weights)
				sigmoid = 1.0 / (1.0 + np.exp(-l))	
				return sigmoid
				
	def classify(self, featureVector, weights):
				'''
					Generate the probability of each row and return the binary classification.
				'''
				logit = 0.0
				for i in range(len(featureVector)):
					#logit += weights[i] * logistic.sigmoid(self,featureVector[i])
					logit += weights[i] * featureVector[i]
				if(logit > 0):
					return 1
				return 0		
							
	def train(self, weights, num_features, featureMatrix, labelVector):
				'''
					Training, based on featureVector to get weight array
				'''
				for i in range(3):
					for j in range(num_features):
						featureVector = featureMatrix[i]
						weights[j] += self.LEARNING_RATE * (featureMatrix[i][j] * labelVector[i] - self.sigmoid(self, featureVector))
						print weights[j]
					
				

class main:				
	if __name__ == '__main__':
				l = logistic()
				print l.sigmoid(8)
				featureVector=[1,2,3]
				for i in range(len(featureVector)):
					print featureVector[i],",",l.sigmoid(featureVector[i])
				
				weights=[[] for i in range(3)] #array initialization
				for i in range(3):
					weights[i] = 1
					
				print l.classify(l.sigmoid, featureVector, weights)
				
				featureMatrix = [[0 for x in range(3)] for x in range(3)] 
				for i in range(3):
					for j in range(3):
						featureMatrix[i][j] = 2
						
				labelVector = [0 for x in range(3)]
						
				print l.train(weights,3, featureMatrix, labelVector)
