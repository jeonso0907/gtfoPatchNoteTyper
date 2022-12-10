from GTFO_patch_note import GTFO_patch_note
from content_type import Content, get_content_setting
import textwrap

if __name__ == '__main__':

    new_patch_note = GTFO_patch_note(True, '2022-12-09')
    content_info = []
    with open("translated contents/content_info.txt", "r", encoding='utf8') as file:
        lines = file.readlines()
        for line in lines:
            if len(line) == 1:
                content_type = get_content_setting(content_info[0])
                new_patch_note.add_content(content_type=content_type, content_info=content_info[1:])
                content_info.clear()
            else:
                content_info.append(textwrap.fill(line, width=45, initial_indent='', subsequent_indent='      '))




    new_patch_note.save_patch_note()
