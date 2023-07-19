import cv2
import os

def improve_resolution(image, scale_percent):
    width = int(image.shape[1] * scale_percent / 100)
    height = int(image.shape[0] * scale_percent / 100)
    dim = (width, height)
    resized = cv2.resize(image, dim, interpolation=cv2.INTER_LINEAR)
    return resized

def sharpen_image(image):
    blurred = cv2.GaussianBlur(image, (0, 0), 3)
    sharpened = cv2.addWeighted(image, 1.5, blurred, -0.5, 0)
    return sharpened

def denoise_image(image):
    denoised = cv2.fastNlMeansDenoisingColored(image, None, 10, 10, 7, 21)
    return denoised

# Directory containing the images
directory = "path/to/your/images"

# Create a directory to store the processed images
output_directory = os.path.join(directory, "processed_images")
os.makedirs(output_directory, exist_ok=True)

# Iterate over each image in the directory
for filename in os.listdir(directory):
    if filename.endswith(".png") or filename.endswith(".jpg"):
        try:
            # Load the image
            image_path = os.path.join(directory, filename)
            image = cv2.imread(image_path)

            # Improve resolution by scaling
            scale_percent = 200  # Increase the resolution by 200%
            high_res_image = improve_resolution(image, scale_percent)

            # Denoise the high-resolution image
            denoised_image = denoise_image(high_res_image)

            # Sharpen the denoised image
            sharpened_image = sharpen_image(denoised_image)

            # Print the output path
            output_path = os.path.join(output_directory, filename)
            print(f"Processing image: {filename}")
            print(f"Output path: {output_path}")

            # Save the processed image
            cv2.imwrite(output_path, sharpened_image)
        except Exception as e:
            print(f"Error processing image {filename}: {str(e)}")

# Display a message after processing all images
print("Image processing completed.")

