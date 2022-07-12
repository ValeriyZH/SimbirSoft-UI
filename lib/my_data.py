import datetime
import os

class MyData:
   # Репозитарии
   Rep1 = "/home/gm/PycharmProjects/SimbirSoft/"
   # полный путь и имя файла логирования выполнения автотестов
   log_file_name = 'Autotesting_log' + str(datetime.datetime.today()) + '.txt'
   mail_login = 'autotesterovautotester'
   mail_password = 'Autotesterov_Autotester'
   start_url = 'https://knep.ru/tech/list-of-search-engines.html#%D0%A0%D0%BE%D1%81%D1%81%D0%B8%D0%B9%D1%81%D0%BA%D0%B8%D0%B5_%D0%BF%D0%BE%D0%B8%D1%81%D0%BA%D0%BE%D0%B2%D1%8B%D0%B5_%D1%81%D0%B8%D1%81%D1%82%D0%B5%D0%BC%D1%8B'
   url_yandex_disk = 'https://disk.yandex.ru/client/'
   name_Folder = 'SimbirSoft'
   url_new_Folder = url_yandex_disk + 'disk/' + name_Folder
   name_Document = 'SimbirSoft_Document'
   url_new_Document = 'https://disk.yandex.ru/edit/disk/disk%2FSimbirSoft%2FSimbirSoft_Document.docx'