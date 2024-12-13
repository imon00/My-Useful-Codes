from PIL import Image
import qrcode

# Function to generate and save a QR code with a border
def generate_qr_code_with_border(data, filename='qrcode_with_border.png', border_size=20):
    # Create a QR code instance
    qr = qrcode.QRCode(
        version=1,  # QR code size (1 is the smallest)
        error_correction=qrcode.constants.ERROR_CORRECT_L,  # Error correction level
        box_size=10,  # Size of each box in the QR code
        border=4,  # Internal border (default QR code border)
    )
    
    # Add data to the QR code
    qr.add_data(data)
    qr.make(fit=True)
    
    # Create an image from the QR code with custom fill and background color
    img = qr.make_image(fill_color='#ac1f25', back_color='white').convert('RGB')
    
    # Calculate the new size for the image with the border
    border_color = (0, 0, 0)  # Black border
    width, height = img.size
    new_width = width + 2 * border_size
    new_height = height + 2 * border_size
    
    # Create a new image with the border size and fill it with the border color
    bordered_img = Image.new('RGB', (new_width, new_height), border_color)
    
    # Paste the original QR code in the center of the new image (bordered image)
    bordered_img.paste(img, (border_size, border_size))
    
    # Save the final image with the border
    bordered_img.save(filename)
    print(f"QR code with border saved as {filename}")

# Example usage
data = "https://drive.google.com/drive/folders/1zuRB1UWy4KgvwYNEtluHqqFo46cd93aO?usp=drive_link"
generate_qr_code_with_border(data, "qr_with_black_border.png", border_size=10)

Computational Fluid Mechanics, Machine Learning, Renewable Energy, Ship Hydrodynamics

Undergraduate student, Bangladesh University of Engineering and Technology