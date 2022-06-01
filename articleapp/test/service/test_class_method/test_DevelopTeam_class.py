from django.test import TestCase

from articleapp.classes.DevelopTeam_class import DevelopTeam
from articleapp.classes.Developer_class import Developer
from articleapp.classes.Exception_class import TypeIsNotUser, AlreadyMemberExist, MemberDoesNotExist, \
    TypeIsNotDeveloper, TypeIsNotSupporter
from articleapp.classes.Supporter_class import Supporter


class TestDevelopTeamClass(TestCase):
    # 개발팀 만들기 List 로 주어질 떄
    def test_develop_make_team_given_list(self):
        # Given
        m1 = Developer()
        m2 = Developer()
        m3 = Developer()
        team_list = [m1, m2, m3]

        # When
        team = DevelopTeam()
        team.make_team(team_list)

        # Then
        self.assertEqual(team_list, team.get_team_list())

    # 개발팀 만들기 - 단일 유저로 주어질 때
    def test_develop_make_team_given_string(self):
        # Given
        m1 = Developer()

        # When
        team = DevelopTeam()
        team.make_team(m1)

        # Then
        self.assertEqual([m1], team.get_team_list())

    # 개발팀 만들기 - 다른 클래스가 들어온다면??
    def test_develop_make_team_when_other_type_come(self):
        # Given
        team_list = ['m1', 'm2', 'm3']

        # When
        team = DevelopTeam()

        with self.assertRaises(TypeIsNotDeveloper):
            team.make_team(team_list)

    # 개발팀 만들기 - 리스트 멤버 중 다른 클래스가 있다면?
    def test_developer_make_team_when_data_is_list_and_other_class_into_data(self):
        # Given
        m1 = Developer()
        m2 = Developer()
        m3 = 'test_'
        team_list = [m1, m2, m3]

        # When
        team = DevelopTeam()

        # Then
        with self.assertRaises(TypeIsNotDeveloper):
            result = team.make_team(team_list)

    # 개발팀 멤버 추가 - 팀 리스트에 멤버가 제대로 추가 되었는가?
    def test_develop_team_add_member(self):
        # Given
        m1 = Developer()
        m2 = Developer()
        m3 = Developer()
        team_list = [m1, m2, m3]
        team = DevelopTeam()
        team.make_team(team_list)

        new_member = Developer()

        # When
        result = team.append_developer(new_member)

        # Then
        team_list.append(new_member)
        self.assertTrue(result)
        self.assertEqual(team_list, team.get_team_list())

    # 개발팀 멤버 추가 - 이미 있는 유저가 추가 된다면?
    def test_develop_team_append_member_when_already_member_exist(self):
        # Given
        m1 = Developer()
        m2 = Developer()
        m3 = Developer()
        team = DevelopTeam()
        team.make_team([m1, m2, m3])

        # Then
        with self.assertRaises(AlreadyMemberExist):
            # When
            team.append_developer(m1)

    # 개발팀 멤버 제거 - 리스트에서 멤버가 제대로 제거 되는가?
    def test_develop_team_delete_member(self):
        # Given
        m1 = Developer()
        m2 = Developer()
        m3 = Developer()
        team_list = [m1, m2, m3]
        team = DevelopTeam()
        team.make_team([m1, m2, m3])

        # When
        result = team.delete_developer(m1)

        # Then
        team_list.remove(m1)
        self.assertTrue(result)
        self.assertEqual(team_list, team.get_team_list())

    # 개발팀 멤버 제거 - 팀 리스트에서 없는 멤버를 제거할 경우
    def test_develop_team_delete_member_when_member_does_not_exist(self):
        # Given
        m1 = Developer()
        m2 = Developer()
        m3 = Developer()
        team_list = [m1, m2, m3]
        team = DevelopTeam()
        team.make_team(team_list)

        # When
        m4 = Developer()

        # Then
        with self.assertRaises(MemberDoesNotExist):
            result = team.delete_developer(m4)

    # 개발팀 리더 설정 - 리더 설정이 제대로 되는가?
    def test_develop_team_register_leader(self):
        # Given
        m1 = Developer()
        m2 = Developer()
        m3 = Developer()

        team = DevelopTeam()
        team.make_team([m1, m2, m3])

        # When
        result = team.register_leader(m1)

        # Then
        self.assertTrue(result)
        self.assertEqual(team.get_leader(), m1)

    # 개발팀 리더 변경 - 리더 변경이 제대로 되는가?
    def test_develop_team_change_leader(self):
        # Given
        m1 = Developer()
        m2 = Developer()
        m3 = Developer()

        team = DevelopTeam()
        team.make_team([m1, m2, m3])
        team.register_leader(m1)

        # When
        result = team.register_leader(m2)

        # Then
        self.assertTrue(result)
        self.assertEqual(m2, team.get_leader())

    # 개발팀 리더 변경 - data가 developer 객체가 아니라면?
    def test_develop_team_set_leader_when_data_type_is_not_developer(self):
        # Given
        m1 = Developer()
        m2 = Developer()
        m3 = Developer()

        team = DevelopTeam()
        team.make_team([m1, m2, m3])

        # Then
        with self.assertRaises(TypeIsNotDeveloper):
            # When
            result = team.register_leader('test_leader!')

    # 개발팀 리더 변경 - data 가 팀 리스트에 없다면?
    def test_develop_team_register_leader_when_data_not_in_team_list(self):
        # Given
        m1 = Developer()
        m2 = Developer()
        m3 = Developer()

        team = DevelopTeam()
        team.make_team([m1, m2, m3])

        # Then
        with self.assertRaises(MemberDoesNotExist):
            # When
            m4 = Developer()
            team.register_leader(m4)

    # 개발팀 서포터 등록 - 동작 확인
    def test_develop_team_append_supporter(self):
        # Given
        m1 = Developer()
        m2 = Developer()
        m3 = Developer()

        team = DevelopTeam()
        team.make_team([m1, m2, m3])

        # When
        s1 = Supporter()
        team.append_supporter(s1)

        # Then
        self.assertEqual(team.get_supporter_list(), [s1])

    # 개발팀 서포터 등록 - 리스트를 넣었을 때
    def test_develop_team_append_supporter_append_by_list(self):
        # Given
        m1 = Developer()
        m2 = Developer()
        m3 = Developer()

        team = DevelopTeam()
        team.make_team([m1, m2, m3])

        # When
        s1 = Supporter()
        s2 = Supporter()
        s3 = Supporter()
        s4 = Supporter()
        team.append_supporter(s1)
        team.append_supporter([s2, s3, s4])

        # Then
        self.assertEqual(team.get_supporter_list(), [s1, s2, s3, s4])

    # 개발팀 서포터 등록 - 리스트를 넣었을 때 중간에 중복이 있는 경우
    def test_develop_team_append_supporter_append_by_list_and_already_member_exist(self):
        # Given
        team = DevelopTeam()

        # When
        s1 = Supporter()
        s2 = Supporter()
        s3 = Supporter()
        team.append_supporter(s1)

        # Then
        with self.assertRaises(AlreadyMemberExist):
            team.append_supporter([s2, s1, s3])

    # 개발팀 서포터 등록 - 여러명 동작 확인
    def test_develop_team_append_supporter_append_when_supporter_many(self):
        # Given
        m1 = Developer()
        m2 = Developer()
        m3 = Developer()

        team = DevelopTeam()
        team.make_team([m1, m2, m3])

        # When
        s1 = Supporter()
        s2 = Supporter()
        s3 = Supporter()
        team.append_supporter(s1)
        team.append_supporter(s2)
        team.append_supporter(s3)

        # Then
        self.assertEqual(team.get_supporter_list(), [s1, s2, s3])

    # 개발팀 서포터 등록 - 개발자를 등록할 때
    def test_develop_team_append_supporter_when_developer_append_supporter(self):
        # Given
        m1 = Developer()
        m2 = Developer()
        m3 = Developer()

        team = DevelopTeam()
        team.make_team([m1, m2, m3])

        # When
        m4 = Developer()
        with self.assertRaises(TypeIsNotSupporter):
            # When
            team.append_supporter(m4)

    # 개발팀 서포터 등록 - 동일한 유저가 있을 경우
    def test_develop_team_append_supporter_when_develop_already_Exist(self):
        # Given
        m1 = Developer()
        m2 = Developer()
        m3 = Developer()

        team = DevelopTeam()
        team.make_team([m1, m2, m3])

        s1 = Supporter()
        team.append_supporter(s1)

        # When
        with self.assertRaises(AlreadyMemberExist):
            # When
            team.append_supporter(s1)

    # 개발팀 서포터 등록 해제 - 동작 확인
    def test_develop_team_delete_supporter(self):
        # Given
        m1 = Developer()
        m2 = Developer()
        m3 = Developer()

        team = DevelopTeam()
        team.make_team([m1, m2, m3])

        s1 = Supporter()
        team.append_supporter(s1)

        # When
        team.delete_supporter(s1)

        # Then
        self.assertEqual(team.get_supporter_list(), [])

    # 개발팀 서포터 등록 해제 - 없는 서포터를 삭제할 경우
    def test_develop_team_delete_supporter_when_supporter_is_not_exist(self):
        # Given
        team = DevelopTeam()
        s1 = Supporter()

        # Then
        with self.assertRaises(MemberDoesNotExist):
            # When
            team.delete_supporter(s1)

    