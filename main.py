from PIL import Image, ImageFont, ImageDraw
from content_type import Content, get_content_setting


my_image = Image.open("gtfo_empy_patch_note.png")
my_image = my_image.convert('RGB')
image_editable = ImageDraw.Draw(my_image)

curr_height = 300


def add_content(content_type, content_info):

    global curr_height
    title_text = get_content_setting(content_type)
    title_font = ImageFont.truetype(Content.TITLE_FONT.value, Content.TITLE_SIZE.value)
    image_editable.text((150, curr_height + 300), title_text, fill='black', font=title_font)
    curr_height += Content.TITLE_SIZE.value + 300
    print(curr_height)


# Main Title
main_title_font = ImageFont.truetype('BMJUA_ttf.ttf', 220)
main_title_text = "패치 노트"

# Sub Titles
feature_title_font = ImageFont.truetype('BMJUA_ttf.ttf', 110)
feature_title_text = "새 기능 및 변경 사항"

bug_title_font = ImageFont.truetype('BMJUA_ttf.ttf', 110)
bug_title_text = "버그 수정"

weapon_title_font = ImageFont.truetype('BMJUA_ttf.ttf', 110)
weapon_title_text = "무기 변경점"

# Patch Contents
feature_content_font = ImageFont.truetype('malgun.ttf', 60)
feature_content_text = "- ALT://런다운 2 감염과 10개의 탐사 구역 추가"

# Save
image_editable = ImageDraw.Draw(my_image)
image_editable.text((150,300), main_title_text, fill='black', font=main_title_font)
add_content('feature', '')

#image_editable.text((150,600), feature_title_text, fill='black', font=feature_title_font)
image_editable.text((150,900), bug_title_text, fill='black', font=bug_title_font)
image_editable.text((150,1200), weapon_title_text, fill='black', font=weapon_title_font)
image_editable.text((150,700), feature_content_text, fill='black', font=feature_content_font)
my_image.save("result.jpg")


