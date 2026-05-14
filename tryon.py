from PIL import Image

def virtual_tryon(user_image, cloth_image):
    user = user_image.resize((400,600))
    cloth = cloth_image.resize((200,200))
    user.paste(cloth, (100,200))
    return user
