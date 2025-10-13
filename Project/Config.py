#coding:utf-8

# 图片及视频检测结果保存路径
save_path = 'D:/基于深度学习的香蕉新鲜度等级识别系统/Project/results'

# 使用的模型路径
model_path = 'runs/detect/exp/weights/best.pt'


names = { 0:'freshripe',1: 'freshunripe', 2:'overripe',3: 'ripe',4: 'rotten',5: 'unripe'}

CH_names = ['新鲜成熟','新鲜未熟','过熟','成熟','腐烂','未熟']