import os
import shutil

def move_images(source_folder, destination_folder):
    # 遍历源文件夹中的每个子文件夹
    for root, dirs, files in os.walk(source_folder):
        for dir_name in dirs:
            source_subfolder = os.path.join(root, dir_name)
            destination_subfolder = os.path.join(destination_folder, dir_name)

            # 如果目标子文件夹不存在，创建它
            if not os.path.exists(destination_subfolder):
                os.makedirs(destination_subfolder)

            # 遍历每个子文件夹中的文件
            for file_name in os.listdir(source_subfolder):
                # 检查文件是否是图片格式 (你可以根据需要扩展这个列表)
                if file_name.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
                    source_file = os.path.join(source_subfolder, file_name)
                    destination_file = os.path.join(destination_subfolder, file_name)

                    # 将图片从源文件夹移动到目标文件夹
                    shutil.move(source_file, destination_file)
                    print(f'Moved {source_file} to {destination_file}')

# 示例使用
source_folder = "E:\\Dataset_rock\\data2\\val"
destination_folder = "E:\\Dataset_rock\\data2\\train"
move_images(source_folder, destination_folder)
