from PIL import Image, ImageFont, ImageDraw
from content_type import Content, get_content_setting, is_contain_title
import textwrap

class GTFO_patch_note:

    def __init__(self, is_first_page: bool, date: str):
        patch_note_template = Image.open("template/gtfo_empy_patch_note.png")
        self.new_patch_note = patch_note_template.convert('RGB')
        self.patch_note = ImageDraw.Draw(self.new_patch_note)
        self.curr_height = 300
        self.curr_width = 150
        self.patch_note_date = date

        if is_first_page:
            self.add_content(content_type=Content.PATCH_TITLE, content_info=False)

    def add_content(self, content_type, content_info):

        global curr_height

        # Add a content title
        title_text = content_type.value
        title_size = Content.TITLE_SIZE.value
        title_space = 50
        if content_type == Content.PATCH_TITLE:
            title_size = Content.PATCH_TITLE_SIZE.value
            title_space = 150

        title_font = ImageFont.truetype(Content.TITLE_FONT.value, title_size)
        self.patch_note.text((self.curr_width, self.curr_height), title_text, fill='black', font=title_font)
        self.curr_height += title_size + title_space

        if content_info:
            # Add a content info
            info_font = ImageFont.truetype(Content.INFO_FONT.value, Content.INFO_SIZE.value)

            for info_text in content_info:
                self.patch_note.text((self.curr_width, self.curr_height), info_text, fill='black', font=info_font)
                new_line_number = info_text.count('\n') + 1
                self.curr_height += new_line_number * Content.INFO_SIZE.value + 20

            self.curr_height += 70
    def save_patch_note(self):
        self.new_patch_note.save('translated patch notes/{} 패치 노트.jpg'.format(self.patch_note_date))

    # # Main Title
    # main_title_font = ImageFont.truetype('BMJUA_ttf.ttf', 220)
    # main_title_text = "패치 노트"
    # image_editable.text((150,300), main_title_text, fill='black', font=main_title_font)
    #
    # content_info_full = open('content_info.txt', 'r', encoding="utf8")
    # content_info_each = content_info_full.read().split("\n\n")
    # print(content_info_each)
    # for paragraph in content_info_each:
    #     content_info = paragraph.split("\n")
    #     print(content_info)
    #     if is_contain_title(content_info[0]):
    #         add_content(content_info[0], content_info[1:])




