from sklearn import svm
from putInList import putInList
from GetLabels import get_labels
import numpy

def fit_with_kernel(inFeatures, inLabels, inKernel = "rbf", maxIter = -1):
	toReturn = svm.SVC(kernel = inKernel, max_iter = maxIter)
	toReturn.fit(inFeatures, inLabels)
	return toReturn

def create_machines(inFeatures, inLabels, maxIter = 20):
	linearSVM = fit_with_kernel(inFeatures, inLabels, "linear", maxIter)
	polySVM = fit_with_kernel(inFeatures, inLabels, "poly", maxIter)
	rbfSVM = fit_with_kernel(inFeatures, inLabels, "rbf", maxIter)
	sigmoidSVM = fit_with_kernel(inFeatures, inLabels, "sigmoid", maxIter)
	#precomputedSVM = fit_with_kernel(inFeatures, inLabels, "precomputed", maxIter)
	return linearSVM, polySVM, rbfSVM, sigmoidSVM

def test_SVM(inFeatures, inLabels, machineType, vectorMachine):
	successes = 0
	testData = list(vectorMachine.predict(inFeatures))
	for i in range(len(testData)):
		if testData[i] == inLabels[i]:
			successes += 1
	testError = 1 - float(successes) / float(len(testData))
	print("SVM of type: " + machineType + " gave a test error of: " + str(testError) + ".")
	return testError

def main():
	features = putInList("C:/Users/Cam/Dropbox/Carson and Wammy's Woefully Whimsical Waywardly Wank/final_project/cropped", int(0), int(2000))
	labels = get_labels("trainLabels.csv", int(0),int(2000))
	print("Got features and labels.")
	print("There were " + str(len(labels)) + " patients in the train data.")
	linearSVM, polySVM, rbfSVM, sigmoidSVM = create_machines(features, labels)
	testFeatures = putInList("C:/Users/Cam/Dropbox/Carson and Wammy's Woefully Whimsical Waywardly Wank/final_project/cropped", int(4000), int(5000))
	testLabels = get_labels("trainLabels.csv", int(4000),int(5000))
	print("There were " + str(len(testLabels)) + " patients in the test data.")
	test_SVM(testFeatures, testLabels, "linear", linearSVM)
	test_SVM(testFeatures, testLabels, "poly", polySVM)
	test_SVM(testFeatures, testLabels, "rbf", rbfSVM)
	test_SVM(testFeatures, testLabels, "sigmoid", sigmoidSVM)
	#testSVM(testFeatures, testLabels, "precomputed", precomputedSVM)

main()