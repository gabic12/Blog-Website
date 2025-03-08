from flask import Flask, render_template
from post import Post
import requests

blog_posts = [] #List of Post classes
blog_url = "https://api.npoint.io/23fc9516960c06c50d50"
response = requests.get(blog_url)
all_posts = response.json()
for post in all_posts:
    blog_posts.append(Post(post["id"], post["title"], post["subtitle"], post["body"]))

app = Flask(__name__)

@app.route("/")
def home():
    """Returns all posts"""
    return render_template("index.html", posts=blog_posts)

@app.route("/blog/<int:number>")
def get_post(number):
    """Returns one blog post"""
    requested_blog = None
    for blog_post in blog_posts:
        if blog_post.id == number:
            requested_blog = blog_post
    return render_template("post.html", post=requested_blog)

if __name__ == "__main__":
    app.run(debug=True)
