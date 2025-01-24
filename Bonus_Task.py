import pandas as pd
from sklearn.metrics import precision_score, recall_score, f1_score
from sklearn.metrics import classification_report

clustered_data = pd.read_csv('Results/medlr_assignment_dataset_clustered.csv')

manual_labels = pd.read_csv('labelled_data/labelled_dataset_sample.csv')

merged_data = pd.merge(clustered_data, manual_labels, on='id', suffixes=('_clustered', '_manual'))

y_true = merged_data['cluster_manual']
y_pred = merged_data['cluster_clustered']

precision = precision_score(y_true, y_pred, average='weighted')
recall = recall_score(y_true, y_pred, average='weighted')
f1 = f1_score(y_true, y_pred, average='weighted')

print(f'Precision: {precision:.2f}')
print(f'Recall: {recall:.2f}')
print(f'F1-score: {f1:.2f}')

report = classification_report(y_true, y_pred)
print(report)
