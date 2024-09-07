from PIL import Image
import os
import numpy as np

def resize_image(image_path, target_size):
    with Image.open(image_path) as img:
        img = img.resize(target_size)
        return img

def normalize_image(image):
    np_image = np.array(image) / 255.0  # Normalize pixel values to [0, 1]
    return np_image

def process_images(input_dir, output_dir, target_size):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for filename in os.listdir(input_dir):
        if filename.endswith(('.png', '.jpg', '.jpeg')):
            input_path = os.path.join(input_dir, filename)
            output_path = os.path.join(output_dir, filename)
            
            # Resize and normalize
            resized_img = resize_image(input_path, target_size)
            normalized_img = normalize_image(resized_img)
            
            # Save the processed image
            processed_img = Image.fromarray((normalized_img * 255).astype(np.uint8))
            processed_img = processed_img.convert('RGB')
            processed_img.save(output_path)

if __name__ == "__main__":
    input_directory = 'data/raw/'
    output_directory = 'data/processed/'
    target_dimensions = (256, 256)  # Example target size
    
    process_images(input_directory, output_directory, target_dimensions)
