import os

# ⚙️ 경로 수정 (train, valid, test 각각 따로 실행 가능)
img_dir = r"C:\Users\user\Desktop\yolo_train\datasets\train\images"
label_dir = r"C:\Users\user\Desktop\yolo_train\datasets\train\labels"

# 🔢 새 파일명 prefix
prefix = "logo"

# 이미지 파일 목록 (jpg, png 등)
img_files = [f for f in os.listdir(img_dir) if f.lower().endswith(('.jpg', '.jpeg', '.png'))]
img_files.sort()

for i, img_file in enumerate(img_files, start=1):
    name, ext = os.path.splitext(img_file)
    new_name = f"{prefix}_{i:03d}{ext}"  # 예: logo_001.jpg
    old_img_path = os.path.join(img_dir, img_file)
    new_img_path = os.path.join(img_dir, new_name)

    # 🧩 이미지 중복 방지: 같은 이름 있으면 삭제
    if os.path.exists(new_img_path):
        os.remove(new_img_path)
    os.rename(old_img_path, new_img_path)

    # 🧩 라벨 파일도 동일하게 이름 변경
    old_label = os.path.join(label_dir, f"{name}.txt")
    new_label = os.path.join(label_dir, f"{prefix}_{i:03d}.txt")

    if os.path.exists(old_label):
        # 같은 이름의 라벨이 이미 있으면 삭제 후 진행
        if os.path.exists(new_label):
            os.remove(new_label)
        os.rename(old_label, new_label)

print("✅ 이미지 및 라벨 이름 정리 완료!")
