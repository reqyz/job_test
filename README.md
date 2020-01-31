##### Зависимости
```
pip install -r requirements.txt
```

##### Миграции
```
pgmigrate -d common -c "user=postgres password=secret dbname=job_test" -t latest migrate
```

##### Запуск
```
python3 main.py
```

##### env
```
DATABASE_URL = postgres://reqyz:12321@127.0.0.1:5432/job_test
HOST = 0.0.0.0
PORT = 8001
```

##### P.S.
```
За все что написано на js и вообще за фронт сильно извиняюсь
```