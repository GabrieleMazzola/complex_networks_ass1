import pandas as pd
import json, codecs

df = pd.read_excel("..\manufacturing_emails_temporal_network.xlsx")

edges_list = []

for timestamp, sub_df in df.groupby("timestamp"):
    edges = list(zip(list(sub_df['node1']), list(sub_df['node2'])))
    edges_list.append(edges)

with open('network.json', 'wb') as f:
    json.dump(edges_list, codecs.getwriter('utf-8')(f), ensure_ascii=False)