import os
import shutil
from random import shuffle

# 源文件夹路径
source_dataset_dir = r'D:\task\thyroid\mmpretrain-main\mmpretrain\data/thyoid'

# 目标文件夹路径
target_dataset_dir = r'D:\task\thyroid\mmpretrain-main\mmpretrain\data/imagenet'

# 创建目标文件夹及其子文件夹
os.makedirs(os.path.join(target_dataset_dir, 'train', 'Positive'), exist_ok=True)
os.makedirs(os.path.join(target_dataset_dir, 'train', 'Negative'), exist_ok=True)
os.makedirs(os.path.join(target_dataset_dir, 'val', 'Positive'), exist_ok=True)
os.makedirs(os.path.join(target_dataset_dir, 'val', 'Negative'), exist_ok=True)


def split_data(source_folder, target_train_folder, target_val_folder, split_size=0.8):
    # 获取所有文件的路径
    files = [os.path.join(source_folder, f) for f in os.listdir(source_folder) if
             os.path.isfile(os.path.join(source_folder, f))]
    shuffle(files)  # 随机打乱文件顺序

    # 分割点计算
    split_point = int(len(files) * split_size)

    # 分配文件到训练集和验证集
    train_files = files[:split_point]
    val_files = files[split_point:]

    # 复制文件到目标文件夹
    for f in train_files:
        shutil.copy(f, target_train_folder)

    for f in val_files:
        shutil.copy(f, target_val_folder)

# 对Bike和Car文件夹执行数据集分割
split_data(os.path.join(source_dataset_dir, 'Positive'), os.path.join(target_dataset_dir, 'train', 'Positive'), os.path.join(target_dataset_dir, 'val', 'Positive'))
split_data(os.path.join(source_dataset_dir, 'Negative'), os.path.join(target_dataset_dir, 'train', 'Negative'), os.path.join(target_dataset_dir, 'val', 'Negative'))