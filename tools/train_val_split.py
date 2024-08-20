import os
import shutil
from sklearn.model_selection import KFold


def split_data_into_folds(data_dir, n_splits=10, random_state=None):
    # 获取所有文件的完整路径
    all_files = [os.path.join(data_dir, f) for f in os.listdir(data_dir) if os.path.isfile(os.path.join(data_dir, f))]

    # 初始化KFold
    kf = KFold(n_splits=n_splits, shuffle=True, random_state=random_state)

    folds = list(kf.split(all_files))
    return all_files, folds


def get_train_val_split(all_files, folds, fold_index):
    # 获取指定折的训练集和验证集
    train_indices, val_indices = folds[fold_index]
    train_files = [all_files[i] for i in train_indices]
    val_files = [all_files[i] for i in val_indices]
    return train_files, val_files


def save_files(files, output_dir):
    # 创建输出目录，如果不存在
    os.makedirs(output_dir, exist_ok=True)

    for file in files:
        # 复制文件到输出目录
        shutil.copy(file, output_dir)


# 使用示例
data_directory = r'D:\task\thyroid\mmpretrain-main\mmpretrain\data\imagenet\total_data\Malignant'  # 替换成你的数据目录
output_base_dir = r'D:\task\thyroid\mmpretrain-main\mmpretrain\data\imagenet\total_data\Malignant_split'  # 替换成你的输出目录

all_files, folds = split_data_into_folds(data_directory, n_splits=5, random_state=42)

# 遍历每个折，将训练集和验证集保存到指定路径
for fold_index in range(5):
    train_files, val_files = get_train_val_split(all_files, folds, fold_index=fold_index)

    train_output_dir = os.path.join(output_base_dir, f'fold_{fold_index + 1}', 'train')
    val_output_dir = os.path.join(output_base_dir, f'fold_{fold_index + 1}', 'val')

    save_files(train_files, train_output_dir)
    save_files(val_files, val_output_dir)

    print(f"Fold {fold_index + 1}:")
    print(f"  训练集文件数量: {len(train_files)} - 保存路径: {train_output_dir}")
    print(f"  验证集文件数量: {len(val_files)} - 保存路径: {val_output_dir}\n")
