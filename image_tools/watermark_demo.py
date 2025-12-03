from PIL import Image, ImageFilter

def remove_watermark_demo(input_path="demo_input.jpg", output_path="demo_output.jpg"):
    img = Image.open(input_path)

    # Simple blur on bottom-right area (demo only)
    w, h = img.size
    crop = img.crop((w-200, h-60, w, h)).filter(ImageFilter.GaussianBlur(10))
    img.paste(crop, (w-200, h-60))

    img.save(output_path)
    print("Demo watermark removed!")

if __name__ == "__main__":
    remove_watermark_demo()
