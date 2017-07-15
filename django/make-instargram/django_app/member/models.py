from django.conf import settings
from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager as DefaultUserManager


# class User(AbstractUser):
#     relations = models.ManyToManyField(
#         through='Relation',
#         symmetrical=False,
#     )
#
#     #####################################################
#     # 로그인 한 User 를 기준으로 follow/unfollow 동작 구현하기
#     #####################################################
#
#     # 로그인 한 User = 나
#     # 나의 follow 행위를 통하여 following/follower 관계가 성립된다.
#     def follow(self, other):
#         # other : 내가 follow 하려는 상대방의 객체 정보
#
#         # 상대방이 User 테이블에 해당하지 않으면 예외를 발생시킨다.
#         if not isinstance(other, User):
#             raise ValueError('"user" argument must <User> class')
#
#         # 1. 내가 상대방을 팔로우 함
#         # 내 User 객체의 속성인 relations(객체 타입)의 속성인 following_relation 을 생성 혹은 조회
#         self.following_relation.get_or_create(
#             to_user=other
#         )
#
#         # 2. 내가 팔로우함으로써 내가 상대방의 팔로워가 됨
#         # 상대방 User 객체의 속성인 relations(객체 타입)의 속성인 follower_relation 을 생성 혹은 조회
#         self.follower_relation.get_or_create(
#             from_user=self
#         )
#
#         # 3. 팔로워, 팔로잉 관계에 대한 Relation 테이블의 raw 추가
#         Relation.objects.create(
#             to_user=other,
#             from_user=self
#         )
#
#     # 나(로그인 한 User)를 기준으로 상대방에 대한 follower/following 을 끊음 = Relation 테이블의 raw 삭제
#     def unfollow(self, other):
#         User.objects.filter(
#             to_user=other,
#             from_user=self
#         ).delete()
#
#     #######################################################
#     # 해당 User 기준으로 follower/following 관계 여부 나타내기
#     #######################################################
#
#     # 내(로그인 한 User)가 follow 를 한 other = following
#     def is_following(self, other):
#         return self.following_relation.filter(to_user=other).exists()
#
#     # 나(로그인 한 User)에게 follow 를 한 other = follower
#     def is_follower(self, other):
#         return self.follower_relation.filter(from_user=other).exists()
#
#
# class Relation(models.Model):
#     to_other = models.ForeignKey(User, related_name='following_relation')
#     from_me = models.ForeignKey(User, related_name='follower_relation')
#     created_date = models.DateTimeField(auto_now_add=True)

class UserManager(DefaultUserManager):
    def get_or_create_facebook_user(self, user_info):
        print(user_info)
        username = '{}_{}_{}'.format(
            self.model.USER_TYPE_FACEBOOK,
            settings.FACEBOOK_APP_ID,
            user_info['id'],
        )

        user, user_created = self.get_or_create(
            username=username,
            user_type=self.model.USER_TYPE_FACEBOOK,
            defaults={
                'email': user_info.get('email', ''),
            }
        )
        return user

    def get_or_create_kakao_user(self, user_info):
        print( 'id' in user_info)
        username = '{}_{}_{}'.format(
            self.model.USER_TYPE_KAKAO,
            settings.KAKAO_APP_ID,
            user_info['id'],
        )

        user, user_created = self.get_or_create(
            username=username,
            user_type=self.model.USER_TYPE_KAKAO,
            defaults={
                'email': user_info.get('kaccount_email', ''),
                # 'nickname': user_info.get('nickname', '')
            }
        )
        return user


class User(AbstractUser):
    USER_TYPE_DJANGO = 'd'
    USER_TYPE_FACEBOOK = 'f'
    USER_TYPE_KAKAO = 'k'
    USER_TYPE_CHOICES = (
        (USER_TYPE_DJANGO, 'Django'),
        (USER_TYPE_FACEBOOK, 'Facebook'),
        (USER_TYPE_KAKAO, 'kakao'),
    )

    objects = UserManager()

    # nickname = models.CharField(max_length=36)
    email = models.EmailField(null=True, unique=True)

    # 유저타입. 기본은 Django, 페이스북 로그인 시 USER_TYPE_FACEBOOK 값을 갖음
    user_type = models.CharField(max_length=1, choices=USER_TYPE_CHOICES, default=USER_TYPE_DJANGO)
