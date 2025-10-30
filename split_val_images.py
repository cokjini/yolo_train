import os, random, shutil

# 데이터셋 경로
base_dir = "datasets"
train_img = os.path.join(base_dir, "train", "images")
train_lbl = os.path.join(base_dir, "train", "labels")
val_img = os.path.join(base_dir, "val", "images")
val_lbl = os.path.join(base_dir, "val", "labels")

# val 폴더 없으면 자동 생성
os.makedirs(val_img, exist_ok=True)
os.makedirs(val_lbl, exist_ok=True)

# 전체 train 이미지 목록 불러오기
images = [f for f in os.listdir(train_img) if f.endswith((".jpg", ".png", ".jpeg"))]

# 20% 정도를 val로 이동
val_count = max(1, int(len(images) * 0.2))
val_samples = random.sample(images, val_count)

for img_name in val_samples:
    label_name = os.path.splitext(img_name)[0] + ".txt"
    src_img = os.path.join(train_img, img_name)
    src_lbl = os.path.join(train_lbl, label_name)
    dst_img = os.path.join(val_img, img_name)
    dst_lbl = os.path.join(val_lbl, label_name)

    shutil.copy2(src_img, dst_img)
    if os.path.exists(src_lbl):
        shutil.copy2(src_lbl, dst_lbl)

print(f"✅ {val_count}개의 이미지를 train → val로 복사 완료!")
