heroku login
mkdir bottlesample
cd bottlesample
# bottleインストール(ローカルで動かす場合に必要)
pip install bottle
# ソース
cat << EOF > app.py
import os
from bottle import route, run

@route("/")
def hello_world():
    return "Hello World!";

run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
EOF
#pip freeze > requirements.txt
cat << EOF > requirements.txt
bottle==0.12.13
EOF
cat << EOF > Procfile
web: python app.py
EOF
# gitに登録
git init
git add -A
git commit -m init
# アプリケーションの作成
heroku apps:create
# デプロイ
git push heroku master
heroku open
#
# DB対応
#
cat << EOF > app.py
import os
import psycopg2
from bottle import route, run

@route("/")
def hello_world():
        DATABASE_URL = os.environ['DATABASE_URL']
        conn = psycopg2.connect(DATABASE_URL, sslmode='require')
        cur = conn.cursor()
        cur.execute("SELECT * FROM mytable;")
        data = cur.fetchone()
        name1 = data[1]
        return "Hello World2!" + str(name1);

run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
EOF
cat << EOF >> requirements.txt
psycopg2-binary
EOF
# アドオン
heroku addons
heroku addons:create heroku-postgresql:hobby-dev
heroku pg:info
#
# DBのセットアップ
# postgresをがインストールされているホストから実行
heroku pg:psql -a enigmatic-wildwood-49893
create table mytable (
	id integer,
	name1 varchar,
	name2 varchar,
	name3 varchar,
	num1 integer,
	num2 integer,
	num3 integer,
	primary key(id)
);
insert into mytable values (1, 'name1', 'name2', 'name3', 100, 200, 300);
insert into mytable values (2, 'name1', 'name2', 'name3', 400, 500, 600);
#
# デプロイ
#
git add -A
git commit -m db
git push heroku master
heroku open
