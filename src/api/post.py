from client.dummy_service import dummy_service
from model.post import Post
from dataclasses import asdict


def get_post(post_id: int):
    post_dict = dummy_service.get_post(post_id)
    post = Post(title=post_dict.get('title'), body=post_dict.get('body'))
    return asdict(post)


def update_post(post_id: int, new_title: str, new_body: str):
    """
    Client may not send in all fields of a post.
    Fetch the original post data, and only update the fields client send
    """
    post_dict = dummy_service.get_post(post_id)

    title = new_title if new_title else post_dict['title']
    body = new_body if new_body else post_dict['body']

    updated_post = Post(title=title, body=body)
    dummy_service.update_post(post_id, updated_post)
    return {'success': True}
