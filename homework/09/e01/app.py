from flask import Flask
import json
from flask import jsonify, request, make_response


app = Flask(__name__)

id = 2
blog_posts = [{
    "id": 1, 
    "title": "jussin seikkailut tamkissa", 
    "body": "olipa kerran jussi joka opetti tamkissa"}, 
    {"id": 2, 
    "title": "jussin seikkailut yliopistossa", 
    "body": "olipa kerran jussi joka opetti yliopistossa"
    }]

@app.route('/blogs')
def get_blogs():
    return jsonify(blog_posts)

@app.route('/blogs/<int:the_id>', methods=['GET'])
def get_blog(the_id):
    for i in range(0, len(blog_posts)):
        if(blog_posts[i]["id"] == the_id):
            return make_response(jsonify(blog_posts[i]), 200)
    else:
        return make_response("", 404)

@app.route('/blogs', methods=['POST'])
def add_blogs():
    blogs = json.loads(request.data)
    global id
    id = id + 1
    blogs["id"] = id
    blog_posts.append(blogs)
    return make_response(jsonify(blogs), 201)

@app.route('/blogs/<int:the_id>', methods=['DELETE'])
def delete_blogs(the_id):
    if the_id == 0:
        global id
        id = 0
        global blog_posts
        blog_posts.clear()
        return make_response("", 204)
    index_to_be_deleted = -1
    for i in range(0, len(blog_posts)):
        if(blog_posts[i]["id"] == the_id):
            index_to_be_deleted = i
    if(index_to_be_deleted != -1):
        blog_posts.pop(index_to_be_deleted)
        return make_response("", 204)
    else:
        return make_response("", 404)

@app.route('/blogs/<int:the_id>', methods=['PUT'])
def add_or_mod_blogs(the_id):
    index_to_be_add_or_modded = -1
    for i in range(0, len(blog_posts)):
        if(blog_posts[i]["id"] == the_id):
            index_to_be_add_or_modded = i
    if(index_to_be_add_or_modded != -1):
        blogs = json.loads(request.data)
        id_copy = index_to_be_add_or_modded+1
        blogs["id"] = id_copy
        blog_posts.insert(index_to_be_add_or_modded, blogs)
        blog_posts.remove(blog_posts[index_to_be_add_or_modded+1])
        return make_response(jsonify(blogs), 200)
    else:
        return make_response("", 404)
if __name__ == "__main__":
    app.run(debug=True)