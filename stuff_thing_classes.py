stuff_classes = ['banner', 'blanket', 'branch', 'bridge', 'building-other', 
		'bush', 'cabinet', 'cage', 'cardboard', 'carpet', 'ceiling-other', 
		'ceiling-tile', 'cloth', 'clothes', 'clouds', 'counter', 'cupboard', 
		'curtain', 'desk-stuff', 'dirt', 'door-stuff', 'fence', 'floor-marble', 
		'floor-other', 'floor-stone', 'floor-tile', 'floor-wood', 'flower', 
		'fog', 'food-other', 'fruit', 'furniture-other', 'grass', 'gravel', 
		'ground-other', 'hill', 'house', 'leaves', 'light', 'mat', 'metal', 
		'mirror-stuff', 'moss', 'mountain', 'mud', 'napkin', 'net', 'paper', 
		'pavement', 'pillow', 'plant-other', 'plastic', 'platform', 'playingfield', 
		'railing', 'railroad', 'river', 'road', 'rock', 'roof', 'rug', 'salad', 
		'sand', 'sea', 'shelf', 'sky-other', 'skyscraper', 'snow', 'solid-other', 
		'stairs', 'stone', 'straw', 'structural-other', 'table', 'tent', 
		'textile-other', 'towel', 'tree', 'vegetable', 'wall-brick', 
		'wall-concrete', 'wall-other', 'wall-panel', 'wall-stone', 'wall-tile', 
		'wall-wood', 'water-other', 'waterdrops', 'window-blind', 'window-other', 
		'wood', 'other']

thing_classes = ['BG', 'person', 'bicycle', 'car', 'motorcycle', 'airplane',
               'bus', 'train', 'truck', 'boat', 'traffic light',
               'fire hydrant', 'stop sign', 'parking meter', 'bench', 'bird',
               'cat', 'dog', 'horse', 'sheep', 'cow', 'elephant', 'bear',
               'zebra', 'giraffe', 'backpack', 'umbrella', 'handbag', 'tie',
               'suitcase', 'frisbee', 'skis', 'snowboard', 'sports ball',
               'kite', 'baseball bat', 'baseball glove', 'skateboard',
               'surfboard', 'tennis racket', 'bottle', 'wine glass', 'cup',
               'fork', 'knife', 'spoon', 'bowl', 'banana', 'apple',
               'sandwich', 'orange', 'broccoli', 'carrot', 'hot dog', 'pizza',
               'donut', 'cake', 'chair', 'couch', 'potted plant', 'bed',
               'dining table', 'toilet', 'tv', 'laptop', 'mouse', 'remote',
               'keyboard', 'cell phone', 'microwave', 'oven', 'toaster',
               'sink', 'refrigerator', 'book', 'clock', 'vase', 'scissors',
               'teddy bear', 'hair drier', 'toothbrush']


count = 0

for cat in stuff_classes:
	count+=1

print(count)


count = 0

for cat in thing_classes:
	count+=1

print(count)