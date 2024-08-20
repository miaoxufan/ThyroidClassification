from PIL import Image
import os


def count_image_modes(folder_path):
    rgb_count = 0
    grayscale_count = 0

    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp', '.tiff')):
                image_path = os.path.join(root, file)

                with Image.open(image_path) as img:
                    if img.mode == 'RGB':
                        rgb_count += 1
                    elif img.mode == 'L':
                        grayscale_count += 1

    return rgb_count, grayscale_count


# 使用示例
folder_path = r'D:\task\thyroid\0726建模测试组-第一批\negative'
rgb_count, grayscale_count = count_image_modes(folder_path)
print(f'RGB三通道图片数量: {rgb_count}')
print(f'灰度图数量: {grayscale_count}')
