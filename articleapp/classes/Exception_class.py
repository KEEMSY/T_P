class TypeIsNotUser(Exception):
    def __init__(self):
        super().__init__('User Type이 아닙니다.')


class AlreadyMemberExist(Exception):
    def __init__(self):
        super().__init__('이미 유저가 존재 합니다.')


class MemberDoesNotExist(Exception):
    def __init__(self):
        super().__init__('유저가 존재 하지 않음.')