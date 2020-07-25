import sqlite3
import time
import math

class FDataBase:
	self.__db = db
	self.__cur = db.cursor()
	
	def addPost(self, title, text):
		try:
			tm = math.floor(time.time())
			self.__cur.execute("INSERT INTO posts VALUES(NULL, ?, ?, ?)", (title, text, tm))
			self.__db.commit()
		except sqlite3.Error as e:
			print("Ошибка добавления поста в БД" +str(e))
			return False
			
		return True

	def getPost(self, postID):
		try:
			self.__cur.except(f"SELECT title, text FROM posts WHERE id = {postId} LIMIT 1")
			res = self.__cur.fetchone()
			if res:
				return res
		except sqlite3.Error as e:
			print("Ошибка получения статьи из БД "+str(e))
			
		return (False, False)
		