text_dir='VCTK-Corpus/txt/'
wav_dir='VCTK-Corpus/wav48/'

train_txt='VCTK-Corpus/training.txt'
val_txt='VCTK-Corpus/validation.txt'
eval_txt='VCTK-Corpus/evaluation.txt'

import os

all_set=[]
train_set=[]
val_set=[]
eval_set=[]


spks=os.listdir(text_dir)
spks.sort()
for spk in spks:
    if spk in ['p360', 'p361', 'p362', 'p363']:
        continue
    #import pdb;pdb.set_trace()
    spk_dir=os.path.join(text_dir, spk)
    txts=os.listdir(spk_dir)
    txts.sort()
    for txt in txts[:-20]:
        iid=os.path.basename(txt).split('.')[0]
        txt=os.path.join(spk_dir, txt)
        with open(txt) as f:
            text=f.readline().strip()
        train_set.append((iid, text))
    for txt in txts[-20:-10]:
        iid=os.path.basename(txt).split('.')[0]
        txt=os.path.join(spk_dir, txt)
        with open(txt) as f:
            text=f.readline().strip()
        val_set.append((iid, text))
    for txt in txts[-10:]:
        iid=os.path.basename(txt).split('.')[0]
        txt=os.path.join(spk_dir, txt)
        with open(txt) as f:
            text=f.readline().strip()
        eval_set.append((iid, text))

with open(train_txt, 'w') as f:
    for iid, text in train_set:
        f.write(f'{iid}|{text}\n')
with open(val_txt, 'w') as f:
    for iid, text in val_set:
        f.write(f'{iid}|{text}\n')
with open(eval_txt, 'w') as f:
    for iid, text in eval_set:
        f.write(f'{iid}|{text}\n')
