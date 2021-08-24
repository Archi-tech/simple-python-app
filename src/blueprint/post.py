from flask import Blueprint, request

from api.post import get_post, update_post
api = Blueprint('post', __name__)


@api.route('/post/<int:post_id>', methods=['GET'])
def get_post_route(post_id):
    return get_post(post_id)


@api.route('/post/<int:post_id>', methods=['PUT'])
def update_post_route(post_id):

    input = request.json
    new_title = input.get('title')
    new_body = input.get('body')
    # Here I think insight like to parse client input into a data model

    return update_post(post_id, new_title, new_body)
