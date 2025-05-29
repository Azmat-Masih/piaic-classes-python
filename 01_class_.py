'''
Print hello world
'''
print("Hello world")


'''
printing hellow world 10 times using for loop
''' 
for i in range(10):
  print("hello world")
  
  
'''
Printing hello world 10 time using while loop
'''
i = 0
while(i <= 10):
  print(f"hello world, {i}")
  i+= 1
  
  
'''
# prompt: create a id card width 3 cm height 2cm, background color light green, now this is card content name= Azmat , gender= male, f_name = Sakhawat, 
# add image on the right conner of the card 1by1 card border slightly round. create this card according to the any country id card
'''
from PIL import Image, ImageDraw, ImageFont

def create_id_card(name, gender, f_name, image_path):
    # ID card dimensions (3 cm x 2 cm at 100 pixels/cm)
    width = 300
    height = 200

    # Create base card with light green background
    id_card = Image.new("RGB", (width, height), color="lightgreen")

    # Apply rounded corners
    mask = Image.new("L", (width, height), 0)
    draw_mask = ImageDraw.Draw(mask)
    draw_mask.rounded_rectangle([(0, 0), (width, height)], radius=15, fill=255)
    base = Image.new("RGB", (width, height), color="white")
    id_card = Image.composite(id_card, base, mask)

    # Draw text on the ID card
    draw = ImageDraw.Draw(id_card)
    font = ImageFont.load_default()
    text_color = "black"

    draw.text((10, 10), f"Name: {name}", fill=text_color, font=font)
    draw.text((10, 30), f"Gender: {gender}", fill=text_color, font=font)
    draw.text((10, 50), f"Father's Name: {f_name}", fill=text_color, font=font)

    # Add profile image on the right corner
    try:
        profile_image = Image.open(image_path).resize((80, 80))
        id_card.paste(profile_image, (width - 90, height - 90))
    except FileNotFoundError:
        print(f"❌ Error: Image file not found at path: {image_path}")

    # Save the final ID card
    id_card.save("id_card.png")
    print("✅ ID card created and saved as 'id_card.png'.")
    


'''
Creating ID card using Pakistani style...
'''
from PIL import Image, ImageDraw, ImageFont

def create_pakistani_id_card(name, gender, f_name, religion, cnic_number, image_path, logo_path):
    width, height = 300, 200  # 3cm x 2cm approx

    # Create card with light green background
    id_card = Image.new("RGB", (width, height), color="#d0f0c0")

    # Rounded border
    mask = Image.new("L", (width, height), 0)
    draw_mask = ImageDraw.Draw(mask)
    draw_mask.rounded_rectangle([(0, 0), (width, height)], radius=12, fill=255)
    white_bg = Image.new("RGB", (width, height), color="white")
    id_card = Image.composite(id_card, white_bg, mask)

    draw = ImageDraw.Draw(id_card)
    font = ImageFont.load_default()

    # Add watermark/logo
    try:
        logo = Image.open(logo_path).convert("RGBA")
        logo = logo.resize((100, 100))
        logo.putalpha(60)
        id_card.paste(logo, ((width - logo.width) // 2, (height - logo.height) // 2), logo)
    except FileNotFoundError:
        print("⚠️ Logo not found.")

    # Text: Government header centered
    gov_text_en = "Government of Pakistan"
    gov_text_ur = "حکومتِ پاکستان"

    # Get text size using textbbox
    bbox_en = draw.textbbox((0, 0), gov_text_en, font=font)
    bbox_ur = draw.textbbox((0, 0), gov_text_ur, font=font)

    en_width = bbox_en[2] - bbox_en[0]
    ur_width = bbox_ur[2] - bbox_ur[0]

    draw.text(((width - ur_width) // 2, 5), gov_text_ur, fill="darkgreen", font=font)
    draw.text(((width - en_width) // 2, 20), gov_text_en, fill="black", font=font)

    # Info Section
    draw.line([(10, 40), (width - 10, 40)], fill="green", width=1)
    draw.text((10, 50), f"Name: {name}", fill="black", font=font)
    draw.text((10, 65), f"CNIC: {cnic_number}", fill="black", font=font)
    draw.text((10, 80), f"Gender: {gender}", fill="black", font=font)
    draw.text((10, 95), f"Father's Name: {f_name}", fill="black", font=font)
    draw.text((10, 110), f"Religion: {religion}", fill="black", font=font)

    # Profile photo
    try:
        profile = Image.open(image_path).resize((80, 80))
        id_card.paste(profile, (width - 90, height - 90))
    except FileNotFoundError:
        print("⚠️ Profile image not found.")

    # Border
    draw.rounded_rectangle([(0, 0), (width - 1, height - 1)], radius=12, outline="darkgreen", width=2)

    # Save final card
    id_card.save("pakistani_id_card_final.png")
    print("✅ ID card saved as 'pakistani_id_card_final.png'")

# Example usage
create_pakistani_id_card(
    name="Azmat",
    gender="Male",
    f_name="Sakhawat",
    religion="Christian",
    cnic_number="12345-6789012-3",
    image_path="take3.PNG",     # Make sure this exists in your runtime
    logo_path="pak_logo.png"     # Upload this transparent PNG logo first
)
