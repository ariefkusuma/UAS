import cv2

def split_image(image_path):
    img = cv2.imread(image_path)

    height, width, _ = img.shape
    piece_width = width // 3
    piece_height = height // 3

    pieces = []
    for i in range(3):
        for j in range(3):
            left = j * piece_width
            top = i * piece_height
            right = (j + 1) * piece_width
            bottom = (i + 1) * piece_height
            piece = img[top:bottom, left:right]
            pieces.append(piece)

    return pieces

image_path = "images/image.jpg"
pieces = split_image(image_path)

for i, piece in enumerate(pieces):
    cv2.imshow(f"Piece {i}", piece)

cv2.waitKey(0)
cv2.destroyAllWindows()
