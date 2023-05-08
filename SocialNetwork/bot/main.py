import asyncio

from bot import Bot


async def main():
    bot = Bot()
    users = await bot.generate_users()
    posts = await bot.generate_posts(users)
    reactions = await bot.generate_likes(users, posts)


if __name__ == '__main__':
    print('Starting activities')
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    loop.close()
    print('Activities done')
