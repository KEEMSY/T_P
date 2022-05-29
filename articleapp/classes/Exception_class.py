# Team 관련 에러
class TypeIsNotUser(Exception):
    def __init__(self):
        super().__init__('User Type이 아닙니다.')


class TypeIsNotSupporter(Exception):
    def __init__(self):
        super().__init__('Supporter Type이 아닙니다.')


class TypeIsNotDeveloper(Exception):
    def __init__(self):
        super().__init__('Developer Type이 아닙니다.')


class AlreadyMemberExist(Exception):
    def __init__(self):
        super().__init__('이미 유저가 존재 합니다.')


class MemberDoesNotExist(Exception):
    def __init__(self):
        super().__init__('유저가 존재 하지 않음.')


# DevelopProject Exceptions
class ProjectDataIsWrong(Exception):
    def __init__(self):
        super().__init__('프로젝트 데이터가 일정하지 않음')


class ProjectDataIsNotDict(Exception):
    def __init__(self):
        super().__init__('Dictionary 타입이 아닙니다.')


class StackDuplicated(Exception):
    def __init__(self):
        super().__init__('기술 스택이 중복입니다.')


class StackDoesNotExist(Exception):
    def __init__(self):
        super().__init__('기술 스택이 없습니다.')


class ToolDoesNotExist(Exception):
    def __init__(self):
        super().__init__('기술 스택이 없습니다.')
