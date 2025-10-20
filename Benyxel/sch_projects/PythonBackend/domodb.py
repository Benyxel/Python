import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'GiftyNarh@2025'
)

cursorObject = dataBase.cursor()
cursorObject.execute('CREATE DATABASE demodb')
print('All done')