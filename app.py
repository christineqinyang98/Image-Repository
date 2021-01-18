from flask import Flask, render_template
import mysql.connector

app = Flask(__name__)

def getDB():
    db = mysql.connector.connect(host="localhost",
                         user="cqyang",
                         password="BeelTail#9812",
                         db="imageRepo")
    cursor = db.cursor()
    return (cursor, db)

def iniDB():
    cursor, db = getDB()

    cursor.execute("DROP TABLE IF EXISTS images;")
    cursor.execute("CREATE TABLE images(name VARCHAR(50), id INT, price float, imgLoc VARCHAR(50), type VARCHAR(50), stock INT, PRIMARY KEY (id));")
    cursor.execute("INSERT INTO images VALUES('Magenta Bomber Jacket', 1, 34.99, 'images/bomber-magenta.jpg', 'jacket', 3);")
    cursor.execute("INSERT INTO images VALUES('Black Long Coat', 2, 74.99, 'images/coat-black.jpg', 'jacket', 1);")
    cursor.execute("INSERT INTO images VALUES('Tan Long Coat', 3, 74.99, 'images/coat-tan.jpg', 'jacket', 2);")
    cursor.execute("INSERT INTO images VALUES('Blue Jeans', 4, 54.99, 'images/jeans-blue.jpg', 'pants', 4);")
    cursor.execute("INSERT INTO images VALUES('Black Sweatpants', 5, 44.99, 'images/sweatpants-black.jpg', 'pants', 4);")
    cursor.execute("INSERT INTO images VALUES('Pink Sweatpants', 6, 44.99, 'images/sweatpants-pink.jpg', 'pants', 4);")
    cursor.execute("INSERT INTO images VALUES('White Tee', 7, 14.99, 'images/tee-white.jpg', 'shirt', 5);")
    cursor.execute("INSERT INTO images VALUES('Print Tee', 8, 14.99, 'images/tee-print.jpg', 'shirt', 5);")

    db.commit()
    print("Database Successfully Created")
    #for row in cursor.fetchall():
    #    print row[0]

@app.route('/')
def home():
    (cursor, db) = getDB()
    cursor.execute("SELECT * FROM images;")

    items = []
    for row in cursor.fetchall():
        if row[5] > 0:
            stock = "Available"
        else:
            stock = "Out of Stock"
        items.append({
            "id":    row[1],
            "name":  row[0],
            "price": "$%.2f" % (row[2]),
            "src":   "/static/%s" % (row[3]),
            "type": "%s" % (row[4]),
            "stock": "%s" % (stock),
        })
   
    return render_template("index.html", items=items)

#@app.route("/reset")
#def reset():
#    initialize_db()
#    return render_template("message.html", message="Database reset.")

if __name__ == '__main__':
    iniDB()
    app.run(debug = True)