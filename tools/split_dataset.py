import os
import shutil

def extract_images(source_folder, destination_folder):
    # 创建目标文件夹（如果不存在）
    os.makedirs(destination_folder, exist_ok=True)

    # 遍历源文件夹下的所有子文件夹
    for root, dirs, files in os.walk(source_folder):
        for file in files:
            # 检查文件是否为图片（根据扩展名）
            if file.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp', '.tiff')):
                # 源文件的完整路径
                source_file = os.path.join(root, file)
                # 目标文件的完整路径
                destination_file = os.path.join(destination_folder, file)

                # 复制文件到目标文件夹
                shutil.copy2(source_file, destination_file)
                print(f'Copied: {source_file} to {destination_file}')

# 使用示例
source_folder = r'D:\task\thyroid\0812验证组-第二批\验证组-转移-发送格式-第二批'
destination_folder = r'D:\task\thyroid\0812验证组-第二批\Malignant'
extract_images(source_folder, destination_folder)
