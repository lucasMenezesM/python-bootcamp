import requests
from post import Post

def get_posts() -> list[Post]:
    response = requests.get("https://api.npoint.io/c51ff38d4f68ea3a024a")
    response.raise_for_status()
    data = response.json()

    posts = [
        Post(title=post["title"], subtitle=post["subtitle"], body=post["body"], id=post["id"]) 
        for post in data
    ]

    return posts


def get_post_by_id(id) -> Post:
    posts = get_posts()
    
    target_post: Post = None
    print("ids abaixo:")
    for post in posts:
        print(post.id)
        if post.id == id:
            target_post = post
            break

    return target_post


# posts = get_posts()
# for post in posts:
#     print(post.title)
# print(posts)

# post = get_post_by_id(1)
# print(post.body)