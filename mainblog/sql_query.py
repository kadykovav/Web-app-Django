# from django.db import connection
#
# with connection.cursor() as cursor:
#     cursor.execute(
#         "select count(*),mt2.theme"
#         " from mainblog_blogpost mt"
#         " join mainblog_blogpost_themes mbt on mt.id = mbt.blogpost_id"
#         " join mainblog_themepost mt2 on mbt.themepost_id = mt2.id"
#         " group by mt2.theme;")
#
#     count_themes = cursor.fetchall()
