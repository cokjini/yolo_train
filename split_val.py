import os
import random
import shutil

# ✅ 경로 설정
base_dir = "datasets"
train_img_dir = os.path.join(base_dir, "train", "images")
train_label_dir = os.path.join(base_dir, "train", "labels")
val_img_dir = os.path.join(base_dir, "val", "images")
val_label_dir = os.path.join(base_dir, "val", "labels")

# ✅ validation 데이터 비율 (예: 0.2 → 20%)
val_ratio = 0.2

# ✅ 기존 val 폴더 완전 초기화
if os.path.exists(val_img_dir):
    shutil.rmtree(val_img_dir)
if os.path.exists(val_label_dir):
    shutil.rmtree(val_label_dir)

os.makedirs(val_img_dir, exist_ok=True)
os.makedirs(val_label_dir, exist_ok=True)

# ✅ train/images 내 이미지 가져오기
image_files = [f for f in os.listdir(train_img_dir)
               if f.lower().endswith(('.jpg', '.jpeg', '.png'))]

# ✅ 무작위로 val_ratio 비율 추출
val_count = int(len(image_files) * val_ratio)
val_images = random.sample(image_files, val_count)

print(f"총 {len(image_files)}장 중 {val_count}장을 val 세트로 이동합니다.\n")

# ✅ 이미지 및 라벨 이동
for img_name in val_images:
    src_img = os.path.join(train_img_dir, img_name)
    dst_img = os.path.join(val_img_dir, img_name)

    label_name = os.path.splitext(img_name)[0] + ".txt"
    src_label = os.path.join(train_label_dir, label_name)
    dst_label = os.path.join(val_label_dir, label_name)

    if os.path.exists(src_img):
        shutil.move(src_img, dst_img)
    if os.path.exists(src_label):
        shutil.move(src_label, dst_label)

print("✅ 기존 val 삭제 후 랜덤 분할 완료!")
