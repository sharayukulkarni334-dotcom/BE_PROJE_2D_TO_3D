import cv2
import os

def preprocess_image(input_path, output_path):
    # Read image
    img = cv2.imread(input_path)
    if img is None:
        raise ValueError("Image not found")

    # Resize
    img = cv2.resize(img, (512, 512))

    # Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Reduce noise
    blur = cv2.GaussianBlur(gray, (5, 5), 0)

    # Detect edges
    edges = cv2.Canny(blur, 50, 150)

    # Convert edges to 3 channels
    edges_color = cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR)

    # Combine edges with original image
    enhanced = cv2.addWeighted(img, 0.8, edges_color, 0.2, 0)

    # Create output folder if missing
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    # Save cleaned image
    cv2.imwrite(output_path, enhanced)

    return output_path
