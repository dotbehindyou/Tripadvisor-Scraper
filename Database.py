from mysql import connector

db = connector.connect(host="localhost", user="root", password="")

def init():
    cursor = db.cursor()
    cursor.execute("CREATE DATABASE IF NOT EXISTS TripadvisorData;")

    #cursor.execute("CREATE TABLE tripadvisorabout ("+
    #        "id int(11) NOT NULL,"+
    #        "ratingAverage int(11) NOT NULL,"+
    #        "ratingCount int(11) NOT NULL,"+
    #        "isTravelersChoice bit(1) NOT NULL,"+
    #        "roomFeauters varchar(512) NOT NULL,"+
    #        "amenities varchar(512) NOT NULL,"+
    #        "roomTypes varchar(512) NOT NULL,"+
    #        "languages varchar(512) NOT NULL,"+
    #        "hotelClass int(11) NOT NULL,"+
    #        "hotelStyle varchar(512) NOT NULL,"+
    #        "description text NOT NULL"+
    #    ");")

    # ALTER TABLE `tripadvisorabout` ADD PRIMARY KEY( `id`);

def add_mysql

if __name__ == "__main__":
    init()