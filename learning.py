import yagmail
yag = yagmail.SMTP({'abitur.yolo@gmail.com' : 'SecretAliasName'}, '123456yolo')
yag.send('vasilegroza3@gmail.com', 'MySubject', 'You will never guess..')