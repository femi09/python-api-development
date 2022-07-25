# # path operation (route in node js)
# @app.get('/')
# async def root():
#     return {"message": "welcome to my api"}


# @app.get('/posts', status_code=status.HTTP_200_OK)
# async def get_posts():
#     cursor.execute("""SELECT * FROM posts""")
#     posts = cursor.fetchall()
#     return posts

# @app.get('/posts/{id}', status_code=status.HTTP_200_OK)
# async def get_post(id: int):
#     cursor.execute("""SELECT * FROM posts WHERE id = %s """, (str(id)))
#     post = cursor.fetchone()
#     if not post:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="post not found")

#     return post

# @app.post('/posts', status_code=status.HTTP_201_CREATED)
# async def create_post(post: Post):
#     cursor.execute("""INSERT INTO posts (title, content, published) VALUES (%s, %s, %s) RETURNING * """, (post.title, post.content, post.published))
#     new_post = cursor.fetchone()
#     conn.commit()
#     return new_post

# @app.put('/posts/{id}')
# async def update_post(id: int, post:Post):
#     cursor.execute("""UPDATE posts SET title = %s, content =%s, published = %s WHERE id = 1 RETURNING * """, (post.title, post.content, post.published))
#     updated_post = cursor.fetchone()
#     conn.commit()
#     if updated_post == None:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="post not found")
#     return updated_post


# @app.delete('/posts/{id}')
# async def delete_post(id: int):
#     cursor.execute("""DELETE FROM posts WHERE id = %s """, (str(id)))
#     deleted_post = cursor.fetchone()
#     conn.commit()
#     if deleted_post == None:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="post not found")
#     return delete_post

