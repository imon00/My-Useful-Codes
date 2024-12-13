from PIL import Image, ImageDraw

def draw_lines_on_image(image_path, output_path, line_thickness=1.5):
    """
    Draws black horizontal and vertical lines (borders) on an image.

    Args:
        image_path (str): Path to the input image.
        output_path (str): Path to save the output image.
        line_thickness (int): Thickness of the border lines.
        num_lines (int): Number of horizontal and vertical lines to draw.
    """
    # Open the image
    image = Image.open(image_path)
    draw = ImageDraw.Draw(image)

    # Get image dimensions
    width, height = image.size

    # Calculate spacing for lines
    horizontal_spacing = height // 43
    vertical_spacing = width // 45

    # Draw horizontal lines
    for i in range(43):
        y = i * horizontal_spacing
        draw.rectangle([(0, y), (width, y + line_thickness)], fill="black")

    # Draw vertical lines
    for i in range(45):
        x = i * vertical_spacing
        draw.rectangle([(x, 0), (x + line_thickness, height)], fill="black")

    # Save the modified image
    image.save(output_path)
    print(f"Image saved with borders at: {output_path}")

# Example usage
input_image = "example.jpg"  # Replace with your input image path
output_image = "output_with_borders.jpg"  # Replace with desired output path
draw_lines_on_image(input_image, output_image)
