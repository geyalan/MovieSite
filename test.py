#coding=utf-8
import web
urls = (
	'/','index',
	'/movie/(\d+)','movie',
)

# dict实例
# movies = [
# 	{
# 		'title':'Forrset Gump',
# 		'year':1994
# 	},{
# 		'title':'Titanic',
# 		'year':1997
# 	}
# ]

# sqlite实例
db = web.database(dbn='sqlite',db='MovieSite.db')

render = web.template.render('templates/')

class index:
	def GET(self):
		# page = ''
		# for m in movies:
		# 	page +='%s(%d)\n'%(m['title'],m['year'])
		# return page
		
		movies = db.select('movie')
		# return movies
		return render.index(movies)

	def POST(self):
		data = web.input()
		condition = r'title like "%'+data.title+ r'%"'
		movies = db.select('movie',where=condition)
		return render.index(movies)

class movie:
	def GET(self,movie_id):
		movie_id = int(movie_id)
		movie = db.select('movie', where='id=$movie_id', vars=locals())[0]
		return render.movie(movie)

# class movie:
#     def GET(self, movie_id):
#         movie = db.select('movie', where='id=$int(movie_id)', vars=locals())[0]
#         return render.movie(movie)


if __name__ == "__main__":
	app = web.application(urls,globals())
	app.run()