# import required libraries
import json


# defining functions
def get_json(source):
    """
    get data from json file
    raise exception if file wasn't found
    :return: list of posts
    """
    try:
        with open(source, mode='r', encoding='utf-8') as file:
            return json.load(file)
    except FileNotFoundError as exception:
        return f"{exception} Json file with data not found"


def get_posts_all():
    """
    get posts from posts.json file using function get_json()
    :return: list of posts
    """
    return get_json('data/posts.json')


def get_comments_all():
    """
    get posts from posts.json file using function get_json()
    :return: list of posts
    """
    return get_json('data/comments.json')


def get_posts_by_user(user_name):
    """
    getting list of all posts, creating list of usernames from all posts,
    checking username correctness, if its correct - creating list of his posts,
    otherwise raise value error as wrong username was requested
    :param user_name:
    :return: list of posts fo required user
    """
    all_posts = get_posts_all()
    valid_users = list(set([post['poster_name'] for post in all_posts]))
    if user_name in valid_users:
        user_posts = [post for post in all_posts if post['poster_name'] == user_name]
        return user_posts
    raise ValueError("User was not found")


def get_comments_by_post_id(post_id: int):
    """
    getting all comments, all posts,checking type of requested post id,
    checking if post with requested id exists, raising errors for wrong type,
    :param post_id: requested number of post
    :return: list of comments for requested id
    or value error if id out of range of existing ids
    """
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


def search_for_posts(query):
    """
    getting all posts, checking if posts contains query, forming list of posts, which contains
    :param query: content to search in posts
    :return:list of posts, containing query
    """
    all_posts = get_posts_all()
    return [post for post in all_posts if query.lower() in post['content'].lower()]


def get_post_by_pk(pk):
    """
    getting all posts, searching for post with requested pk
    raising type error, if requested pk has wrong type, value errors for 0 and negative numbers,
    and if requested pk out of range of existing pk
    :param pk:
    :return:
    """
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
