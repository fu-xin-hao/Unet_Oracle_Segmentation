import os
import cv2
import numpy as np

# 设置输入和输出文件夹
input_folder = 'miou_out/detection-results/'
original_folder = 'VOCdevkit/VOC2007/JPEGImages/'
output_folder = 'out'

# 创建输出文件夹
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# 遍历输入文件夹中的所有图片文件
for filename in os.listdir(input_folder):
    if filename.endswith('.jpg') or filename.endswith('.png'):
        # 加载二值化图像和原始图像
        binary_path = os.path.join(input_folder, filename)
        binary_img = cv2.imread(binary_path, cv2.IMREAD_GRAYSCALE)
        original_path = os.path.join(original_folder, filename)
        orig_img = cv2.imread(original_path)
        
        # 对二值化图像进行连通区域分析
        nb_components, output, stats, centroids = cv2.connectedComponentsWithStats(binary_img, connectivity=4)
        sizes = stats[1:, -1]  # 获取每个区域的面积
        min_size = 20  # 设置最小面积阈值
        
        # 创建对应的输出文件夹
        output_dir = os.path.join(output_folder, os.path.splitext(filename)[0])
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
        
        # 遍历每个连通区域
        for i in range(nb_components):
            if sizes[i] >= min_size:
                x, y, w, h = stats[i + 1, :4]  # 获取外接矩形坐标
                x1, y1, x2, y2 = x, y, x + w, y + h  # 计算边界框坐标
                
                # 从原始图像中裁剪子图像
                img_char = orig_img[y1:y2, x1:x2]
                
                # 保存裁剪出的子图像
                output_filename = os.path.join(output_dir, f'{os.path.splitext(filename)[0]}_{i}.jpg')
                cv2.imwrite(output_filename, img_char)

print('处理完成!')
