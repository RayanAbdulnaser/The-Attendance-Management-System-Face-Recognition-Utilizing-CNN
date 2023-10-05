from PIL import ImageFont, ImageDraw, Image

def getFontSize(txt,top, right, bottom, left):
    ####test
    fontsize = 1  # starting font size
    W=abs(right-left)
    H=abs(bottom-top)
    font = ImageFont.truetype("cambria.ttc", fontsize)
    while (font.getsize(txt)[0] < W) and (font.getsize(txt)[1] < H):
        # iterate until the text size is just larger than the criteria
        fontsize += 1
        font = ImageFont.truetype("cambria.ttc", fontsize)
        
    # optionally de-increment to be sure it is less than criteria
    fontsize -= 1
    font = ImageFont.truetype("cambria.ttc", fontsize)

        ####
    return font
