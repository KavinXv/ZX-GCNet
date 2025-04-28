import cv2
import os
import random

def rotate_image(image, angle):
    """
    对图像进行指定角度的旋转
    :param image: 输入图像
    :param angle: 旋转角度
    :return: 旋转后的图像
    """
    (h, w) = image.shape[:2]
    # 获取旋转矩阵，中心为图像中心
    center = (w // 2, h // 2)
    rotation_matrix = cv2.getRotationMatrix2D(center, angle, 1.0)
    
    # 进行仿射变换，旋转图像
    rotated_image = cv2.warpAffine(image, rotation_matrix, (w, h))
    return rotated_image

def process_images_with_random_rotation(input_folder, output_folder):
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

                # 生成30到90度之间的随机旋转角度
                random_angle = random.uniform(10, 45)

                # 对图像进行随机旋转处理
                rotated_img = rotate_image(img, random_angle)

                # 构建输出文件夹路径
                relative_path = os.path.relpath(root, input_folder)
                output_dir = os.path.join(output_folder, relative_path)

                # 如果输出文件夹不存在，创建它
                os.makedirs(output_dir, exist_ok=True)

                # 构建输出图像路径，并在文件名后加上 "1"
                file_name, file_ext = os.path.splitext(file)
                output_file_name = f"{file_name}_4{file_ext}"
                output_img_path = os.path.join(output_dir, output_file_name)

                # 保存旋转后的图像
                cv2.imwrite(output_img_path, rotated_img)

                print(f"图像保存到: {output_img_path}")

if __name__ == "__main__":
    # 输入大文件夹路径（原始图像所在位置）
    input_folder = r'D:\vscode_code\Deep_learning\DATASET\data2_2\test'  # 替换为你输入的大文件夹路径

    # 输出大文件夹路径（处理后的图像保存位置）
    output_folder = r'D:\vscode_code\Deep_learning\DATASET\data2_2_4\test'  # 替换为你输出的大文件夹路径

    # 调用函数进行遍历和处理
    process_images_with_random_rotation(input_folder, output_folder)
