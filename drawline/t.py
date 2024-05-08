import cv2
import numpy as np

# 讀取圖片
image = cv2.imread('right.jpg')  # 確保路徑和圖片名稱是正確的

# 確認圖片是否成功加載
if image is None:
    print("圖片加載失敗，請檢查路徑是否正確")
else:
    # 圖片的尺寸
    height, width = image.shape[:2]

    # 設定盲點標示區域的參數，這些參數可能需要根據實際情況調整
    blind_spot_width_ratio = 0.15  # 假設盲點區域佔車寬的15%
    blind_spot_height_start_ratio = 0.5  # 從車窗一半高度開始
    blind_spot_height_end_ratio = 0.95  # 到車窗95%的高度結束

    # 計算盲點區域的左右邊界
    left_blind_spot_end = int(width * (0.5 - blind_spot_width_ratio))
    left_blind_spot_start = int(width * 0.5)
    right_blind_spot_end = int(width * (0.5 + blind_spot_width_ratio))
    right_blind_spot_start = int(width * 0.5)

    # 計算盲點區域的上下邊界
    top_blind_spot = int(height * blind_spot_height_start_ratio)
    bottom_blind_spot = int(height * blind_spot_height_end_ratio)

    # 畫一條斜線來表示左側的盲點範圍
    cv2.line(image, (left_blind_spot_start, top_blind_spot), (0, bottom_blind_spot), (0, 255, 0), 2)

    # 顯示圖像
    cv2.imshow('Left Blind Spot Areas with Diagonal Line', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
