from PIL import Image
import os

def convert_jpeg_to_webp(input_directory, output_directory):
    # 出力ディレクトリが存在しない場合は作成
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    # 指定ディレクトリ内のファイルを処理
    for filename in os.listdir(input_directory):
        if filename.lower().endswith(".jpg") or filename.lower().endswith(".jpeg"):
            # 画像ファイルのパスを作成
            img_path = os.path.join(input_directory, filename)
            # 画像を開く
            with Image.open(img_path) as img:
                # WebP形式のファイル名を設定
                webp_filename = f"{os.path.splitext(filename)[0]}.webp"
                webp_path = os.path.join(output_directory, webp_filename)
                # サイズを変更せずWebP形式で保存
                img.save(webp_path, "WEBP", quality=85)
                print(f"Converted {filename} to {webp_filename}")

# 使用例: inputディレクトリとoutputディレクトリを指定
convert_jpeg_to_webp("input", "output")
