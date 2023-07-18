# Image Processing

This code is designed to enhance image quality by improving resolution, denoising, and sharpening. It requires the OpenCV library to perform image processing tasks. 

The script was created for the ERC project The Dawn of Tibetan Buddhist Scholasticism (11th-13th c.) (TibSchol). Cf. https://www.oeaw.ac.at/ikga/tibschol for more information.

This project has received funding from the European Research Council (ERC) under the European Union's Horizon 2020 research and innovation programme (grant agreement No. 101001002). See https://cordis.europa.eu/project/id/101001002.

# Functions
1. `improve_resolution(image, scale_percent)`: This function takes an image and a scale percentage as input and returns a high-resolution version of the image by scaling it up using the specified scale percentage.

2. `sharpen_image(image)`: This function takes an image as input and applies a sharpening filter to enhance the image details. It uses Gaussian blurring and weighted addition to achieve sharpening.

3. `denoise_image(image)`: This function takes an image as input and reduces the noise in the image using fast non-local means denoising algorithm. It preserves the image details while reducing the noise.

# Usage
1. Update the `directory` variable in the code with the path to the directory containing your images. By default, the processed images will be automatically saved to an output directory named "processed_images" within the input directory. If you want to specify a different output directory, you can update the output_directory variable in the code
2. Create an output directory to store the processed images 
3. Customise the image processing functions (`improve_resolution`, `sharpen_image`, and `denoise_image`) according to your requirements, if needed
4. If any errors occur during image processing, error messages will be printed to the console. After processing all images in the directory, a completion message will be displayed

# Notes 

The code currently supports processing PNG and JPG image files. If your images have a different file format, you can modify the condition in the for loop accordingly.
