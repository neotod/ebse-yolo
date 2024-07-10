import os
from utils import dataset
import yaml


# download dataset
print(f'current dir: {os.getcwd()}')
dataset.download_dataset()
print(f'after download_datasets - ./artifacts', os.listdir('./artifacts'))


zip_file_path = "./artifacts/dataset_r_full.zip"
extract_path = "./artifacts/"

dataset.extract_zip(zip_file_path, extract_path)

print()
print('after unzipping dataset')
print(f"./artifacts/: {os.listdir('./artifacts/')}")


# prep dataset + make .yaml files
cur_dir = os.getcwd()

# Define the YAML content as a dictionary
dota_1_5_yaml = {
    'train': f'{cur_dir}/artifacts/content/unzipped/images/train/',
    'val': f'{cur_dir}/artifacts/content/unzipped/images/val/',
    'test': f'{cur_dir}/artifacts/content/unzipped/images/test/',

    'train_labels': f'{cur_dir}/artifacts/content/unzipped/labes/train/',
    'val_labels': f'{cur_dir}/artifacts/content/unzipped/labes/val/',

    'nc': 16,
    'names': ['plane',
 'ship',
 'storage tank',
 'baseball diamond',
 'tennis court',
 'basketball court',
 'ground track field',
 'harbor',
 'bridge',
 'large vehicle',
 'small vehicle',
 'helicopter',
 'roundabout',
 'soccer ball field',
 'swimming pool',
  'container crane']
}

# Create a YAML file and write the content
with open(f'{cur_dir}/dota_1_5.yaml', 'w') as file:
    yaml.dump(dota_1_5_yaml, file)

print("YAML file 'dota_1_5.yaml' has been created successfully.")

# train the model
print('training the model')
os.system(f'python3 train.py --data dota_1_5.yaml --cfg ./models/yolov5s__spd_conv__eca_net__bifpn.yaml --weights '' --batch-size 64 --epochs 3 --sync-bn --project yolov5s__spd_conv__eca_net --name yolov5s__spd_conv__eca_net --hyp hyp.scratch_s.yaml')