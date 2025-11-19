from flask import Flask, request, jsonify
from blog import Blog
from db import get_connection

app = Flask(__name__)


# ------------------------------
# Create a new blog
# ------------------------------
@app.route("/blogs", methods=["POST"])
def create_blog():
    data = request.json

    title = data.get("title")
    content = data.get("content")

    if not title or not content:
        return jsonify({"error": "title and content are required"}), 400

    blog = Blog(title=title, content=content)
    blog.save()

    return jsonify({
        "message": "Blog created",
        "id": blog.id
    }), 201


# ------------------------------
# Get all blogs
# ------------------------------
@app.route("/blogs", methods=["GET"])
def get_blogs():
    try:
        conn = get_connection()
        cur = conn.cursor()

        cur.execute("SELECT id, title, content, created_at, updated_at FROM public.blogs ORDER BY created_at DESC")
        rows = cur.fetchall()

        blogs = []
        for row in rows:
            blogs.append({
                "id": row[0],
                "title": row[1],
                "content": row[2],
                "created_at": row[3],
                "updated_at": row[4]
            })

        cur.close()
        conn.close()

        return jsonify(blogs)

    except Exception as e:
        return jsonify({"error": str(e)}), 500


# ------------------------------
# Get one blog by ID
# ------------------------------
@app.route("/blogs/<int:blog_id>", methods=["GET"])
def get_blog(blog_id):
    try:
        conn = get_connection()
        cur = conn.cursor()

        cur.execute(
            "SELECT id, title, content, created_at, updated_at FROM public.blogs WHERE id=%s",
            (blog_id,)
        )
        row = cur.fetchone()

        cur.close()
        conn.close()

        if not row:
            return jsonify({"error": "Blog not found"}), 404

        return jsonify({
            "id": row[0],
            "title": row[1],
            "content": row[2],
            "created_at": row[3],
            "updated_at": row[4]
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500


# ------------------------------
# Update a blog
# ------------------------------
@app.route("/blogs/<int:blog_id>", methods=["PUT"])
def update_blog(blog_id):
    data = request.json
    title = data.get("title")
    content = data.get("content")

    try:
        conn = get_connection()
        cur = conn.cursor()

        cur.execute("""
            UPDATE public.blogs
            SET title=%s, content=%s, updated_at=NOW()
            WHERE id=%s
            RETURNING id;
        """, (title, content, blog_id))

        result = cur.fetchone()
        conn.commit()
        cur.close()
        conn.close()

        if not result:
            return jsonify({"error": "Blog not found"}), 404

        return jsonify({"message": "Blog updated"})

    except Exception as e:
        return jsonify({"error": str(e)}), 500


# ------------------------------
# Delete a blog
# ------------------------------
@app.route("/blogs/<int:blog_id>", methods=["DELETE"])
def delete_blog(blog_id):
    try:
        conn = get_connection()
        cur = conn.cursor()

        cur.execute("DELETE FROM public.blogs WHERE id=%s RETURNING id", (blog_id,))
        result = cur.fetchone()

        conn.commit()
        cur.close()
        conn.close()

        if not result:
            return jsonify({"error": "Blog not found"}), 404

        return jsonify({"message": "Blog deleted"})

    except Exception as e:
        return jsonify({"error": str(e)}), 500


# API for translate_and_speak
@app.route("/blogs/<int:blog_id>/translate", methods=["GET"])
def translate_blog(blog_id):
    from blog import Blog

    source_lang = request.args.get("source")
    target_lang = request.args.get("target")
    if not source_lang or not target_lang:
        return jsonify({"error": "Missing source or target parameter"}), 400

    try:
        blog = Blog.get_by_id(blog_id)
        if not blog:
            return jsonify({"error": "Blog not found"}), 404

        result = blog.translate_and_speak(source_lang, target_lang)
        if "error" in result and result["error"]:
            return jsonify({"error": result["error"]}), 500

        response = {
            "id": blog.id,
            "original_title": blog.title,
            "original_content": blog.content,
            "translated_content": result.get("translated_text")
        }
        return jsonify(response)

    except Exception as e:
        return jsonify({"error": str(e)}), 500


# ------------------------------
# Run server
# ------------------------------
if __name__ == "__main__":
    app.run(debug=True)
