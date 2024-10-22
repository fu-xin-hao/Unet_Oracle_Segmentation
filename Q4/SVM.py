import pandas as pd
import time
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.multiclass import OneVsRestClassifier

# retrieve data这是训练集
data_train = pd.read_csv(r"combined_train.csv")

# Segmentation characteristics and objectives
X_train = data_train.drop(columns=["class", "Filename"])  # characteristic column
y_train = data_train["class"]  # target column
#X_test是测试集
data_test = pd.read_csv(r"combined.csv")

X_test = data_test.drop(columns=[ "Filename"])
start = time.time()

# SVC using multi-category versions
clf = OneVsRestClassifier(SVC(kernel='rbf', C=10, decision_function_shape='ovr'))
clf.fit(X_train, y_train)
y_pred = clf.predict(X_test)
#data1采用测试集
data1 = pd.read_csv(r"combined.csv")
sample_names = data1.iloc[:, 1:]
results_df = pd.DataFrame({'File': sample_names, 'Prediction': y_pred})
output_csv_path = 'result.csv'
results_df.to_csv(output_csv_path, index=False)
print(f"Predictions saved to {output_csv_path}")
