"""
    Exceptions
"""

"""
------------------------------------------------------------------------------------------------------------------
                                            # Type 관련 에러
------------------------------------------------------------------------------------------------------------------
"""


class TypeIsNotUser(Exception):
    def __init__(self):
        super().__init__('User Type이 아닙니다.')


class TypeIsNotSupporter(Exception):
    def __init__(self):
        super().__init__('Supporter Type이 아닙니다.')


class TypeIsNotDeveloper(Exception):
    def __init__(self):
        super().__init__('Developer Type이 아닙니다.')


class TypeIsNotDevelopTeam(Exception):
    def __init__(self):
        super().__init__('Developer Type이 아닙니다.')


class ProjectDataIsWrong(Exception):
    def __init__(self):
        super().__init__('프로젝트 데이터가 일정하지 않음')


class ProjectDataIsNotDict(Exception):
    def __init__(self):
        super().__init__('Dictionary 타입이 아닙니다.')


"""
------------------------------------------------------------------------------------------------------------------
                                           # DoesNotExist 관련 에러
------------------------------------------------------------------------------------------------------------------
"""


class MemberDoesNotExist(Exception):
    def __init__(self):
        super().__init__('유저가 존재 하지 않음.')


class StackDoesNotExist(Exception):
    def __init__(self):
        super().__init__('기술 스택이 없습니다.')


class ToolDoesNotExist(Exception):
    def __init__(self):
        super().__init__('기술 스택이 없습니다.')


class TitleDoesNotExist(Exception):
    def __init__(self):
        super().__init__('Title Key가 없습니다.')


class WriterDoesNotExist(Exception):
    def __init__(self):
        super().__init__('Writer Key가 없습니다.')

"""
------------------------------------------------------------------------------------------------------------------
                                           # AlreadyExist
------------------------------------------------------------------------------------------------------------------
"""


class AlreadyMemberExist(Exception):
    def __init__(self):
        super().__init__('이미 유저가 존재 합니다.')


"""
------------------------------------------------------------------------------------------------------------------
                                           # Duplicated
------------------------------------------------------------------------------------------------------------------
"""


class StackDuplicated(Exception):
    def __init__(self):
        super().__init__('기술 스택이 중복입니다.')


"""
------------------------------------------------------------------------------------------------------------------
                                           # NotOkay
------------------------------------------------------------------------------------------------------------------
"""


class TeamIsNotOkay(Exception):
    def __init__(self):
        super().__init__('Team이 아직 갖춰지지 않았습니다.')


"""
------------------------------------------------------------------------------------------------------------------
                                           # Wrong Data
------------------------------------------------------------------------------------------------------------------
"""


class DateIsPasted(Exception):
    def __init__(self):
        super().__init__('지난 날짜입니다.')
