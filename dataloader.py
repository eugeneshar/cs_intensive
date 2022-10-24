from sklearn.datasets import load_iris


def load_data():
	train, target = load_iris()
	target = target / max(target)
	return train, target
