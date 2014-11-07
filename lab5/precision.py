import csv
import operator
import pandas
from pandas import DataFrame

data = []
data_a = []
data_g = []
with open('products_out.csv', 'rb') as f:
	for row in csv.reader(f):
		if row[1] == 'amazon':
			data_a.append(row)
		else:
			data_g.append(row)


truth_table = []
with open('product_mapping.csv', 'rb') as f:
	for row in csv.reader(f):
		truth_table.append(row)
	
df_a = DataFrame(data_a, columns = ['Cluster ID', 'source', 'id', 'title', 'description', 'manufacturer', 'price', 'canonical_description', 'canonical_title', 'canonical_price', 'canonical_source', 'canonical_id', 'canonical_manufacturer', 'confidence_score'])
df_g = DataFrame(data_g, columns = ['Cluster ID', 'source', 'id', 'title', 'description', 'manufacturer', 'price', 'canonical_description', 'canonical_title', 'canonical_price', 'canonical_source', 'canonical_id', 'canonical_manufacturer', 'confidence_score'])

df_truth = DataFrame(truth_table, columns = ['idAmazon', 'idGoogle'])

df_a = df_a.drop(['description','manufacturer','price','canonical_description','canonical_title', 'canonical_price', 'canonical_source', 'canonical_id', 'canonical_manufacturer', 'confidence_score'], axis=1)
df_g = df_g.drop(['description','manufacturer','price','canonical_description','canonical_title', 'canonical_price', 'canonical_source', 'canonical_id', 'canonical_manufacturer', 'confidence_score'], axis=1)

df_dups = DataFrame.merge(df_a, df_g, left_on='Cluster ID', right_on='Cluster ID', how='inner', sort=True)
df_match = DataFrame.merge(df_dups, df_truth, left_on='id_x', right_on='idAmazon', how='inner', sort=True)

positives = 0
for row in df_match.iterrows():
	if row[1]['id_y'] == row[1]['idGoogle']:
		positives += 1


precision = float(positives)/len(df_dups)
recall = float(positives)/len(df_truth)

print "Precision: " + str(precision)
print "Recall: " + str(recall)

