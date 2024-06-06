import cv2
import numpy as np

def apply_filter(image, filter_name):
    if filter_name == 'grayscale':
        return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    elif filter_name == 'sepia':
        sepia_filter = np.array([[0.393, 0.769, 0.189],
                                 [0.349, 0.686, 0.168],
                                 [0.272, 0.534, 0.131]])
        sepia_image = cv2.transform(image, sepia_filter)
        return sepia_image
    elif filter_name == 'blur':
        return cv2.GaussianBlur(image, (21, 21), 0)
    else:
        return image

def main():
    image_path = 'input_image.jpg'
    output_path = 'output_image.jpg'

    filter_name = 'sepia'  # Change this to apply different filters

    # Load image
    image = cv2.imread(image_path)

    # Apply filter
    filtered_image = apply_filter(image, filter_name)

    # Save output image
    cv2.imwrite(output_path, filtered_image)

if __name__ == "__main__":
    main()


