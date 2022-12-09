from GTFO_patch_note import GTFO_patch_note
from content_type import Content
import textwrap

if __name__ == '__main__':

    with open("translated contents/content_info.txt", "r", encoding='utf8') as file:
        lines = file.readlines()
        for line in lines:
            print(textwrap.fill(line, width=15, initial_indent='', subsequent_indent='      '))
    # content_info_full = open('translated contents/content_info.txt', 'r', encoding="utf8")
    # wrap_list = my_wrap.wrap(text=content_info_full)

    # new_patch_note = GTFO_patch_note(True, '2022-12-09')
    #
    # new_patch_note.save_patch_note()
