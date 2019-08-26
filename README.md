## Aldığım [django](https://www.udemy.com/the-ultimate-beginners-guide-to-django-django-2-python-web-dev-website/)   eğitimi ile birlikte kodlamış olduğum basit bir  ürün avı projesi

<hr>

 # Kurulum
 
 ### Sanal ortam oluşturma

```
python -m venv myvenv
```

### Sanal ortamı çalıştırma


* **git kullanarak**
```
source .\myvenv\Scripts\activate
```

* **powershell kullanarak**
```
.\myvenv\Scripts\activate
```

* **cmd kullanarak**
```
call .\myvenv\Scripts\activate
```
### Gerekli modüllerin kurulumu
```
pip install -r .\requirements.txt
```


### Veritabanı kurulumu
* [Postresql](https://www.postgresql.org/download/) kurulduktan sonra [settings.py](https://github.com/mustafadalga/producthunt/blob/master/producthunt/settings.py) içerisinden veritabanı bilgileri istenildiği gibi değiştirilebilip veritabanı oluşturulabilir.

* **Varsayılan isimle veritabanını oluşturma**
```
CREATE DATABASE producthunt;
```

### Veritabanı tablolarını oluşturma
```
python .\manage.py makemigrations
python .\manage.py migrate
```

### Statik dosyaları oluşturma

```
python manage.py collectstatic
```

### Projeyi çalıştırma

```
python manage.py runserver
```


