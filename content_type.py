from enum import Enum


def get_content_setting(content_type):
    if content_type is 'feature':
        return Content.FEATURE_TITLE.value
    elif content_type is 'bug':
        return Content.BUG_TITLE.value
    else:
        return Content.WEAPON_TITLE.value


class Content(Enum):
    FEATURE_TITLE = '새 기능 및 변경 사항'
    BUG_TITLE = '버그 수정'
    WEAPON_TITLE = '무기 변경점'
    TITLE_FONT = 'BMJUA_ttf.ttf'
    TITLE_SIZE = 110
    INFO_FONT = 'malgun.ttf'
    INFO_SIZE = 60
