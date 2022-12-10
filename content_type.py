from enum import Enum


def get_content_setting(content_type):
    if content_type == Content.FEATURE_TITLE.value:
        return Content.FEATURE_TITLE
    elif content_type == Content.BUG_TITLE.value:
        return Content.BUG_TITLE
    else:
        return Content.WEAPON_TITLE

def is_contain_title(content_info):
    if content_info in (Content.FEATURE_TITLE.value, Content.WEAPON_TITLE.value, Content.BUG_TITLE.value):
        return True
    return False

class Content(Enum):
    PATCH_TITLE = '패치 노트'
    FEATURE_TITLE = '새 기능 및 변경 사항'
    BUG_TITLE = '버그 수정'
    WEAPON_TITLE = '무기 변경점'
    TITLE_FONT = 'fonts/BMJUA_ttf.ttf'
    PATCH_TITLE_SIZE = 220
    TITLE_SIZE = 110
    INFO_FONT = 'fonts/malgunbd.ttf'
    INFO_SIZE = 60
