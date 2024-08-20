import os

def rename_files(folder_path):
    # 遍历文件夹中的所有文件
    for root, dirs, files in os.walk(folder_path):
        for index, element in enumerate(files):
            index += 1
            new_name = "Malignant(" + str(index) + ").jpg"
            old_file = os.path.join(folder_path, element)
            new_file = os.path.join(folder_path, new_name)
            os.rename(old_file, new_file)
            print(f'Renamed: {old_file} -> {new_file}')

# 文件夹路径
folder_path = r'D:\task\thyroid\mmpretrain-main\mmpretrain\data\imagenet\total_data\Malignant'  # 替换为实际的文件夹路径
rename_files(folder_path)
