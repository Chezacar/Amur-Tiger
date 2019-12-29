import os
import subprocess
import pickle
import json
import numpy as np

def cal_IOU(box, ref):
    inter = (np.minimum(ref[0]+ref[2], box[0]+box[2])-np.maximum(ref[0], box[0]))*(np.minimum(ref[1]+ref[3], box[1]+box[3])-np.maximum(ref[1], box[1]))
    union = ref[2]*ref[3] + box[2]*box[3] - inter
    return inter / union

with open('reid.pkl', 'rb') as f:
    reid = pickle.load(f, encoding='bytes')
    
files = os.listdir('./output')
entitis = dict()
for file in files:
    if file[:3] == 'MOT':
        continue
    entity = file.split('_')[0]
    if entity not in entitis:
        entitis[entity] = []
    entitis[entity].append('./output/'+file)

eff_traj = []
for entity in entitis:
    tmp = reid[int(entity)]
    files = entitis[entity]
    for file in files:
        trajs = dict()
        f = open(file, 'r')
        ref = json.load(open('./data/'+file.split('/')[-1].split('.')[0]+'/det.json'))
        start = ref[0]['image_id'].split('_')[-1]
        end = ref[-1]['image_id'].split('_')[-1]
        start = int(start)
        end = int(end)
        if (end-start) == 31:
            key = end - 15
        elif start == 0:
            key = end - 15
        else:
            key = start + 16
        for i in range(len(tmp[b'key'])):
            if tmp[b'key'] == key:
                break
        pos = i
        box = tmp[b'bbox'][i]
        while True:
            res = f.readline()
            if len(res) == 0:
                break
            res = res.split(',')
            traj = int(res[1])
            x, y, w, h = res[2:6]
            box = [float(x), float(y), float(w), float(h)]
            if traj not in trajs:
                trajs[traj] = dict()
                trajs[traj]['box'] = []
                trajs[traj]['video'] = file.split('/')[-1].split('.')[0]
            trajs[traj]['box'].append(box)
        for traj in trajs:
            trajs[traj]['box'] = np.array(trajs[traj]['box'])
            trajs[traj]['box'] = np.mean(trajs[traj]['box'], 0)
        max_iou = 0
        for traj in trajs:
            iou = cal_IOU(trajs[traj]['box'], np.array(box))
            if iou > max_iou:
                eff = traj
                max_iou = iou
        eff_traj.append(eff)