import os
import time
from email.mime import image
import cv2
import numpy as np
import matplotlib.pyplot as plt
from skimage.exposure import exposure
from skimage.feature import hog

def image_preprocessing_feature_extract(folderPath):
    file_list = os.listdir(folderPath)
    # 筛选出所有图像文件
    image_files = [file for file in file_list if file.endswith(('.jpg', '.jpeg', '.png'))]
    # 设置展示图像的数量
    num_images = len(image_files)
    for i, image_file in enumerate(image_files):
        image_path = os.path.join(folderPath, image_file)
        # 读取图像
        img = cv2.imread(image_path, 0)  # 0表示以灰度模式读取
        #快速非局部均值去噪
        denoised = cv2.fastNlMeansDenoising(img, h=10, templateWindowSize=7, searchWindowSize=28)
        # 将图像二值化
        _, binary_image = cv2.threshold(denoised, 128, 255, cv2.THRESH_BINARY)
        # 形态学开运算去小区域
        kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
        opening = cv2.morphologyEx(binary_image, cv2.MORPH_OPEN, kernel, iterations=1)
        #CLAHE图像增强
        clahe = cv2.createCLAHE(clipLimit=0.5, tileGridSize=(8, 8))
        enhanced = clahe.apply(opening)
        #展示图像 子图形式
        plt.subplot(1, 2, 1)
        plt.imshow(img, cmap='gray')  # 指定cmap='gray'
        plt.title('Original Image')
        plt.axis('off')
        plt.subplot(1, 2, 2)
        plt.imshow(enhanced, cmap='gray')  # 指定cmap='gray'
        plt.title('Preprocessing Image')
        plt.axis('off')
        plt.show()
        #feature extract
        features, hog_image = hog(enhanced, orientations=9, pixels_per_cell=(8, 8),
                                  cells_per_block=(2, 2), block_norm='L2-Hys', visualize=True)
        # 将线条的颜色更改为白色
        hog_image[hog_image > 0] = 1
        # 对HOG图像进行亮度调整，以改善可视化效果
        hog_image_rescaled = exposure.rescale_intensity(hog_image, in_range=(0, 10))
        # 创建 SIFT 对象
        sift = cv2.SIFT_create()
        # 检测关键点并计算特征描述子
        keypoints, descriptors = sift.detectAndCompute(opening, None)
        # 在图像上绘制关键点
        image_with_keypoints = cv2.drawKeypoints(opening, keypoints, None)
        # 显示原始图像和HOG特征图像
        plt.figure(figsize=(12, 6))
        plt.subplot(1, 3, 1)
        plt.imshow(cv2.cvtColor(opening, cv2.COLOR_BGR2RGB))
        #plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
        plt.title('Original Image')
        plt.axis('off')
        plt.subplot(1, 3, 2)
        plt.imshow(hog_image_rescaled, cmap='gray')
        plt.title('HOG Features')
        plt.axis('off')
        plt.subplot(1, 3, 3)
        plt.imshow(cv2.cvtColor(image_with_keypoints, cv2.COLOR_BGR2RGB))
        plt.title('SIFT Features')
        plt.axis('off')
        plt.show()
        print(image_file + "的特征描述子为" + str(features) + "\n")
# 主函数
if __name__ == '__main__':
    #start_time = time.time()
    folderPath = 'Original'
    image_preprocessing_feature_extract(folderPath)
