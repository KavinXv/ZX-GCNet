import cv2
import os
import random

def random_zoom(image, scale_min=1.15, scale_max=1.2):
    """
    随机放大图像，放大比例在 scale_min 到 scale_max 之间。
    放大后的图像会居中裁剪回原始尺寸。
    
    :param image: 输入图像
    :param scale_min: 最小缩放比例
    :param scale_max: 最大缩放比例
    :return: 放大并裁剪后的图像
    """
    h, w = image.shape[:2]
    
    # 生成随机缩放比例
    scale = random.uniform(scale_min, scale_max)
    
    # 计算新的尺寸
    new_w = int(w * scale)
    new_h = int(h * scale)
    
    # 进行图像缩放
    resized_image = cv2.resize(image, (new_w, new_h))
    
    # 计算居中裁剪的位置
    start_x = (new_w - w) // 2
    start_y = (new_h - h) // 2
    
    # 裁剪回原始大小
    cropped_image = resized_image[start_y:start_y + h, start_x:start_x + w]
    
    return cropped_image

def process_images_with_random_zoom(input_folder, output_folder):
    # 遍历输入文件夹下的所有子文件夹和文件
    for root, dirs, files in os.walk(input_folder):
        for file in files:
            if file.endswith((".png", ".jpg", ".jpeg", ".bmp")):  # 检查图像文件格式
                # 构建原始图像路径
                img_path = os.path.join(root, file)

                # 读取彩色图像
                img = cv2.imread(img_path)

                if img is None:
                    print(f"无法加载图像: {img_path}")
                    continue

                # 对图像进行随机放大处理
                zoomed_img = random_zoom(img)

                # 构建输出文件夹路径
                relative_path = os.path.relpath(root, input_folder)
                output_dir = os.path.join(output_folder, relative_path)

                # 如果输出文件夹不存在，创建它
                os.makedirs(output_dir, exist_ok=True)

                # 构建输出图像路径，并在文件名后加上 "1"
                file_name, file_ext = os.path.splitext(file)
                output_file_name = f"{file_name}_6{file_ext}"
                output_img_path = os.path.join(output_dir, output_file_name)

                # 保存放大后的图像
                cv2.imwrite(output_img_path, zoomed_img)

                print(f"图像保存到: {output_img_path}")

if __name__ == "__main__":
    # 输入大文件夹路径（原始图像所在位置）
    input_folder = r'D:\vscode_code\Deep_learning\DATASET\data2_2\test'  # 替换为你输入的大文件夹路径

    # 输出大文件夹路径（处理后的图像保存位置）
    output_folder = r'D:\vscode_code\Deep_learning\DATASET\data2_2_6\test'  # 替换为你输出的大文件夹路径

    # 调用函数进行遍历和处理
    process_images_with_random_zoom(input_folder, output_folder)
