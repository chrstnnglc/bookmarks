from flask import Flask, render_template, redirect, request
import pymysql

app = Flask(__name__)

# configure database using mysql
connection = pymysql.connect(host='localhost',
							user='christine',
							password='christine',
							db='bookmarks',
							charset='utf8',
							cursorclass=pymysql.cursors.DictCursor)


## VIEW ALL TASKS ##
@app.route('/')
def home():

	try:
		with connection.cursor() as cursor:
			cursor.execute('SELECT * FROM `bookmarks`')
			result = cursor.fetchall()

			cursor.execute('SELECT `category` FROM `bookmarks`')
			categories = cursor.fetchall()
			return render_template("index.html", bookmarks = result, categories = categories)
			
	finally:
		with connection.cursor() as cursor:
			cursor.close()

# ## ADD A TASK ##
# @app.route('/add',methods=['POST'])
# def add():
# 	try:
# 		_title = request.form['title']
# 		_notes = request.form['notes']

# 		with connection.cursor() as cursor:
# 			cursor.execute('INSERT INTO `tasks` (`title`, `notes`, `status`) VALUES (%s, %s, %s)', (_title, _notes, 'undone'))

# 		connection.commit()

# 		return redirect('/')

# 	# except Exception as e:
# 	# 	return

# 	finally:
# 		with connection.cursor() as cursor:
# 			cursor.close()

# ## EDIT A TASK ##
# @app.route('/edit/<int:edit_id>',methods=['POST'])
# def edit(edit_id):
# 	try:
# 		_title = request.form['title']
# 		_notes = request.form['notes']

# 		with connection.cursor() as cursor:
# 			cursor.execute('UPDATE `tasks` SET `title` = %s, `notes` = %s WHERE `id` = %s', (_title, _notes, edit_id))

# 		connection.commit()

# 		return redirect('/')

# 	# except Exception as e:
# 	# 	return

# 	finally:
# 		with connection.cursor() as cursor:
# 			cursor.close()

# ## ARCHIVE/DELETE A TASK ##
# @app.route('/delete/<int:del_id>')
# def delete(del_id):
# 	try:

# 		with connection.cursor() as cursor:
# 			cursor.execute('UPDATE `tasks` SET `status` = %s WHERE `id` = %s', ('trash', del_id))

# 		connection.commit()

# 		return redirect('/')

# 	# except Exception as e:
# 	# 	return

# 	finally:
# 		with connection.cursor() as cursor:
# 			cursor.close()

if __name__ == '__main__':
	app.run(
		host = 'localhost',
		debug = True
	)