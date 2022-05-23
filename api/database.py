import psycopg2 as pg
from psycopg2.extras import RealDictCursor

def initialize_db():
    con = pg.connect("host=pgdatabase dbname=newsscraper port=5432 user=root password=root",cursor_factory=RealDictCursor)
    cur = con.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS articles(
                    sk SERIAL,
                    url TEXT,
                    title TEXT,
                    text TEXT,
                    tags TEXT,
                    summary TEXT,
                    count INT DEFAULT -1,
                    date DATE DEFAULT CURRENT_DATE,
                    CONSTRAINT unique_url UNIQUE (url),
                    CONSTRAINT unique_sk UNIQUE (sk)
                    )''')
    cur.execute('''CREATE TABLE IF NOT EXISTS users(
                    id INT GENERATED BY DEFAULT AS IDENTITY UNIQUE,
                    cookie_id VARCHAR(64)
                    )''')
    cur.execute('''CREATE TABLE IF NOT EXISTS users_ratings(
                    user_id INT,
                    article_id INT,
                    rating INT,
                    PRIMARY KEY (user_id,article_id),
                    FOREIGN KEY (user_id) REFERENCES users(id),
                    FOREIGN KEY (article_id) REFERENCES articles(sk)
                    )''')
    return con,cur