# import libraries
import json
from json import JSONDecodeError

import pytest

def get_json(source):
    """
    get data from json file
    :return: list of posts
    """
    try:
        with open(source, mode='r', encoding='utf-8') as file:
            return json.load(file)
    except FileNotFoundError as exception:
        return f"{exception} Json file with data not found"

# print(get_json('data/posts.json'))

def get_posts_all():
    """
    get posts from posts.json file
    :return: list of posts
    """
    return get_json('data/posts.json')


# print(get_posts_all())

def get_comments_all():
    """
    get posts from posts.json file
    :return: list of posts
    """
    return get_json('data/comments.json')

def get_posts_by_user(user_name):
    """

    :param user_name:
    :return:
    """

    all_posts = get_posts_all()
    valid_users = list(set([post['poster_name'] for post in all_posts]))
    if user_name in valid_users:
        user_posts = [post for post in all_posts if post['poster_name'] == user_name]
        return user_posts
    raise ValueError("User was not found")


# print(get_posts_by_user('johnny'))

def get_comments_by_post_id(post_id: int):
    all_comments = get_comments_all()
    all_posts = get_posts_all()
    valid_post_pk = [post["pk"] for post in all_posts]
    if type(post_id) != int:
        raise TypeError('Input data should be integer')
    if post_id > len(all_comments):
        raise ValueError('Post_id number out of allowed range')
    if post_id in valid_post_pk:
        comments = [comment for comment in all_comments if comment["post_id"] == post_id]
        return comments
    raise ValueError("Post was not found")


# print(get_comments_by_post_id(13))
# print([post["post_id"] for post in get_comments_all()])
# print(10 in [post["post_id"] for post in get_comments_all()])

def search_for_posts(query):
    all_posts = get_posts_all()
    return [post for post in all_posts if query.lower() in post['content'].lower()]


# print(search_for_posts('mjcck.nvhcv'))
# print(search_for_posts('как'))


def get_post_by_pk(pk):
    all_posts = get_posts_all()
    if type(pk) != int:
        raise TypeError('Input data should be integer')
    if pk < 1:
        raise ValueError('Input number should be positive')
    if pk > len(all_posts):
        raise ValueError('Post number out of allowed range')
    for post in all_posts:
        if pk == post['pk']:
            return post
    # posts = [post for post in all_posts if pk == post['pk']]
    # return posts[0]

# print(get_post_by_pk(-1))
# print([post for post in get_posts_all() if 5== post['pk']][0])


