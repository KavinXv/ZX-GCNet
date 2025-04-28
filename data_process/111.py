import os
import shutil
import math

# 源文件夹路径
source_dir = "D:\\vscode_code\\Deep_learning\\ultralytics-main\\datasets\\data_nan\\train"  # 替换为你的源文件夹路径
# 目标文件夹路径
target_dir = "D:\\vscode_code\\Deep_learning\\ultralytics-main\\datasets\\data_nan\\test"  # 替换为你的目标文件夹路径
# 定义支持的图片文件扩展名
image_extensions = ['.jpg', '.jpeg', '.png', '.bmp', '.gif', '.tiff']

# 遍历源文件夹中的子文件夹
for folder_name in os.listdir(source_dir):
    source_folder_path = os.path.join(source_dir, folder_name)
    # 检查是否是文件夹
    if os.path.isdir(source_folder_path):
        # 获取该子文件夹中的所有图片文件
        images = [f for f in os.listdir(source_folder_path) if os.path.splitext(f)[1].lower() in image_extensions]
        
        # 如果该子文件夹没有图片，跳过
        if not images:
            continue
        
        # 统计图片数量
        image_count = len(images)
        print(f"{folder_name} 文件夹中有 {image_count} 张图片。")

        # 计算最后20%的图片数量
        num_images_to_move = math.ceil(image_count * 0.15)
        images_to_move = images[-num_images_to_move:]  # 取最后20%的图片

        # 在目标文件夹中创建相同名字的子文件夹
        target_folder_path = os.path.join(target_dir, folder_name)
        if not os.path.exists(target_folder_path):
            os.makedirs(target_folder_path)
            print(f"创建文件夹: {target_folder_path}")
        
        # 将最后20%的图片剪切到目标文件夹
        for image_name in images_to_move:
            source_image_path = os.path.join(source_folder_path, image_name)
            target_image_path = os.path.join(target_folder_path, image_name)
            shutil.move(source_image_path, target_image_path)
            print(f"已剪切 {image_name} 到 {target_folder_path}")
