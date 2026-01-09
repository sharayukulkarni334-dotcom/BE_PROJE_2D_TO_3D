import cv2

def is_image_good(image_path, threshold=100):
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    if img is None:
        return False

    sharpness = cv2.Laplacian(img, cv2.CV_64F).var()

    return sharpness >= threshold
