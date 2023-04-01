import os
import numpy as np
from tqdm import tqdm
try:
    import cPickle as pickle
except ImportError:
    import pickle

from lib import get_cif_tokenizer


if __name__ == '__main__':
    fname = "../out/matproj_all_2022_04_12.cif_nosymm.pkl"
    out_dir = "../out/mp_cifs_nosymm"
    symmetrized = False

    tokenizer = get_cif_tokenizer(symmetrized=symmetrized)

    if not os.path.exists(out_dir):
        os.makedirs(out_dir)

    with open(fname, "rb") as f:
        cifs_raw = pickle.load(f)

    # TODO shuffle the order of the cifs_raw; produce mp_oqmd_cifs_nosymm_v2

    cifs = []

    for cif in tqdm(cifs_raw):
        # filter out some lines in the CIF
        lines = cif.split('\n')
        cif_lines = []
        for line in lines:
            line = line.strip()
            if len(line) > 0 and not line.startswith("#") and "pymatgen" not in line:
                cif_lines.append(line)
        cif_lines.append("\n")
        cifs.append("\n".join(cif_lines))

    tokenized_cifs = []
    for cif in tqdm(cifs):
        tokenized_cifs.append(tokenizer.tokenize_cif(cif))

    lens = [len(t) for t in tokenized_cifs]
    unk_counts = [t.count("<unk>") for t in tokenized_cifs]

    # for i, t in enumerate(tokenized_cifs):
    #     if t.count("<unk>") > 0:
    #         print(cifs[i])

    print(f"mean tokenized length: {np.mean(lens):.2f} +/- {np.std(lens):.2f}")
    print(f"total unk counts: {np.sum(unk_counts)}")

    # create a single stream of tokens that will be the dataset
    data = []
    for t in tqdm(tokenized_cifs):
        data.extend(t)

    # create the train and test splits (90-10)
    n = len(data)
    train_data = data[:int(n * 0.9)]
    val_data = data[int(n * 0.9):]

    # encode both to integers
    train_ids = tokenizer.encode(train_data)
    val_ids = tokenizer.encode(val_data)
    print(f"train has {len(train_ids):,} tokens")
    print(f"val has {len(val_ids):,} tokens")
    print(f"vocab size: {len(tokenizer.token_to_id)}")

    # export to bin files
    train_ids = np.array(train_ids, dtype=np.uint16)
    val_ids = np.array(val_ids, dtype=np.uint16)
    train_ids.tofile(os.path.join(os.path.dirname(__file__), os.path.join(out_dir, 'train.bin')))
    val_ids.tofile(os.path.join(os.path.dirname(__file__), os.path.join(out_dir, 'val.bin')))

    # save the meta information as well, to help us encode/decode later
    meta = {
        'vocab_size': len(tokenizer.token_to_id),
        'itos': tokenizer.id_to_token,
        'stoi': tokenizer.token_to_id,
    }
    with open(os.path.join(os.path.dirname(__file__), os.path.join(out_dir, 'meta.pkl')), 'wb') as f:
        pickle.dump(meta, f)
