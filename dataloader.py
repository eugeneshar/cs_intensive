from sklearn.datasets import load_iris


def load_data(multiplier):
	train, target = load_iris()
	target = target / multiplier
	return train, target
