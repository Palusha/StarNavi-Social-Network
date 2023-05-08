import configparser
import random

from faker import Faker

from data import Post, User
from manager import RequestManager


class Bot:
    def __init__(self):
        self.config = configparser.ConfigParser()
        self.config.read('bot.ini')

        self.number_of_users = int(self.config['DEFAULT']['number_of_users']) or 0
        self.max_posts_per_user = int(self.config['DEFAULT']['max_posts_per_user']) or 0
        self.max_likes_per_user = int(self.config['DEFAULT']['max_likes_per_user']) or 0

        self.faker = Faker()
        self.request_manager = RequestManager()

    async def generate_users(self) -> list[User]:
        users = []

        for _ in range(self.number_of_users):
            password = self.faker.password()
            payload = {
                'first_name': self.faker.first_name(),
                'last_name': self.faker.last_name(),
                'username': self.faker.user_name(),
                'email': self.faker.email(),
                'password': password,
                'confirm_password': password,
            }

            _, response_status = await self.request_manager.post(
                url='users/sign_up/',
                payload=payload,
            )

            if response_status == 201:
                users.append(User(**payload))

        return users

    async def generate_posts(self, users: list[User]) -> list[Post]:
        posts = []

        for user in users:
            user_post = []
            post_count = random.randint(0, self.max_posts_per_user)
            auth_data, _ = await self.request_manager.auth(user)

            while len(user_post) != post_count:
                response_data, response_status = await self.request_manager.post(
                    url='posts/',
                    payload={
                        'title': self.faker.text(max_nb_chars=10),
                        'content': self.faker.paragraph(nb_sentences=random.randint(5, 15))
                        },
                    headers={'Authorization': f'Bearer {auth_data["access"]}'}
                )

                if response_status == 201:
                    user_post.append(Post(**response_data))
                else:
                    break

            posts.extend(user_post)

        return posts

    async def generate_likes(self, users: list[User], posts: list[Post]) -> None:
        actions = ['like', 'unlike', 'like', 'unlike', 'like']

        for user in users:
            likes_count = random.randint(0, self.max_likes_per_user)
            auth_data, _ = await self.request_manager.auth(user)
            shuffled_posts = random.sample(posts, k=len(posts))

            for _ in range(likes_count):
                try:
                    post = shuffled_posts.pop()
                except IndexError:
                    break

                await self.request_manager.post(
                    url=f'posts/{post.pk}/{random.choice(actions)}/',
                    headers={'Authorization': f'Bearer {auth_data["access"]}'}
                )
