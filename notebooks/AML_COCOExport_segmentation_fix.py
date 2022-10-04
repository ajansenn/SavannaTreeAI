import os
import json


image_width=8192
image_height=5460
file="<insert AML export coco file>.json"
# Copy metadata.json to local folder
with open(file) as f:
  dataset= json.load(f)


annotations=dataset["annotations"]

for i in range(len(annotations)):
    annotation=annotations[i]
    segments=annotation["segmentation"]
    for j in range(len(segments)):
        points=segments[j]
        for k in range(len(points)):
            # evens 0,2,4 etc are x values -- odds are y values
            if (k % 2) == 0:
                #even
                points[k]=points[k]*image_width
            else:
                # odd
                points[k]=points[k]*image_height
            
    
for i in range(len(annotations)):
    annotation=annotations[i]
    bbox=annotation["bbox"]


    bbox[0]=bbox[0]*image_width
    bbox[1]=bbox[1]*image_height
    bbox[2]=bbox[2]*image_width
    bbox[3]=bbox[3]*image_height



#overwrite coco file with updated version
with open(file, 'w', encoding ='utf8') as json_file:
    json.dump(dataset, json_file, ensure_ascii = False)