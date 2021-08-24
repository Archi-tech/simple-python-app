import requests

from model.post import Post
from dataclasses import asdict

url = 'https://jsonplaceholder.typicode.com'


class DummyService:

    def get_post(self, post_id):
        resp = requests.get(f'{url}/posts/{post_id}')
        post_dict = resp.json()
        # TBD maybe client should always return defined models
        # instead of raw dict from upsteam
        # I like how insight has two sets of models
        #   1. models for parsing other team's response
        #   2. models for returning to client
        # not sure if people feel it's unnessary extra work
        return post_dict

    def update_post(self, post_id, post: Post):
        resp = requests.post(f'{url}/posts/{post_id}', json=asdict(post))
        if not resp.ok:
            print('error')
            # TODO: raise exception


dummy_service = DummyService()
