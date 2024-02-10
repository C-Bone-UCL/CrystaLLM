Artifacts
=========

All trained models, training sets, and artifacts generated by the models have been uploaded to Zenodo. The files are 
publicly accessible at: [https://zenodo.org/records/10642388](https://zenodo.org/records/10642388). All files are 
released under the [CC-BY 4.0](https://creativecommons.org/licenses/by/4.0/) license.

Each file listed below can be downloaded using the `download.py` script. For example, to download `cifs_v1_val.pkl.gz`:
```shell
python bin/download.py cifs_v1_val.pkl.gz
```

### Main Dataset

| Name                       | Description                                                                                  |                                                                                           |
|----------------------------|----------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------|
| cifs_v1_orig.tar.gz        | The original CIF file dataset containing 3,551,492 symmetrized CIF files.                    | [download &#x2193;](https://zenodo.org/records/10642388/files/cifs_v1_orig.tar.gz)        |
| cifs_v1_orig.pkl.gz        | The contents of `cifs_v1_orig.tar.gz` as a serialized Python list of 2-tuples: (ID, CIF).    | [download &#x2193;](https://zenodo.org/records/10642388/files/cifs_v1_orig.pkl.gz)        |
| cifs_v1_dedup.tar.gz       | The deduplicated original CIF dataset, containing 2,285,914 symmetrized CIF files.           | [download &#x2193;](https://zenodo.org/records/10642388/files/cifs_v1_dedup.tar.gz)       |
| cifs_v1_dedup.pkl.gz       | The contents of `cifs_v1_dedup.tar.gz` as a serialized Python list of 2-tuples: (ID, CIF).   | [download &#x2193;](https://zenodo.org/records/10642388/files/cifs_v1_dedup.pkl.gz)       |
| cifs_v1_prep.tar.gz        | The deduplicated and pre-processed original CIF dataset, containing 2,285,719 CIF files.     | [download &#x2193;](https://zenodo.org/records/10642388/files/cifs_v1_prep.tar.gz)        |
| cifs_v1_prep.pkl.gz        | The contents of `cifs_v1_prep.tar.gz` as a serialized Python list of 2-tuples: (ID, CIF).    | [download &#x2193;](https://zenodo.org/records/10642388/files/cifs_v1_prep.pkl.gz)        |
| cifs_v1_train.tar.gz       | The training split of the main dataset, containing 2,047,889 CIF files.                      | [download &#x2193;](https://zenodo.org/records/10642388/files/cifs_v1_train.tar.gz)       |
| cifs_v1_train.pkl.gz       | The contents of `cifs_v1_train.tar.gz` as a serialized Python list of 2-tuples: (ID, CIF).   | [download &#x2193;](https://zenodo.org/records/10642388/files/cifs_v1_train.pkl.gz)       |
| cifs_v1_val.tar.gz         | The validation split of the main dataset, containing 227,544 CIF files.                      | [download &#x2193;](https://zenodo.org/records/10642388/files/cifs_v1_val.tar.gz)         |
| cifs_v1_val.pkl.gz         | The contents of `cifs_v1_val.tar.gz` as a serialized Python list of 2-tuples: (ID, CIF).     | [download &#x2193;](https://zenodo.org/records/10642388/files/cifs_v1_val.pkl.gz)         |
| cifs_v1_test.tar.gz        | The test split of the main dataset, containing 10,286 CIF files.                             | [download &#x2193;](https://zenodo.org/records/10642388/files/cifs_v1_test.tar.gz)        |
| cifs_v1_test.pkl.gz        | The contents of `cifs_v1_test.tar.gz` as a serialized Python list of 2-tuples: (ID, CIF).    | [download &#x2193;](https://zenodo.org/records/10642388/files/cifs_v1_test.pkl.gz)        |
| tokens_v1_all.tar.gz       | The tokens of the complete main dataset.                                                     | [download &#x2193;](https://zenodo.org/records/10642388/files/tokens_v1_all.tar.gz)       |
| tokens_v1_train_val.tar.gz | The tokens of the training and validation sets of the main dataset.                          | [download &#x2193;](https://zenodo.org/records/10642388/files/tokens_v1_train_val.tar.gz) |
| starts_v1_train.pkl        | The start indices for the tokenized training set structures of the main dataset.             | [download &#x2193;](https://zenodo.org/records/10642388/files/starts_v1_train.pkl)        |
| starts_v1_val.pkl          | The start indices for the tokenized validation set structures of the main dataset.           | [download &#x2193;](https://zenodo.org/records/10642388/files/starts_v1_val.pkl)          |
| challenge_set_v1.zip       | The structures of the challenge set.                                                         | [download &#x2193;](https://zenodo.org/records/10642388/files/challenge_set_v1.zip)       |