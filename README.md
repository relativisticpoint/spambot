# spambot
# mailbot
mailbot is a mail bot that has two functionnalities : **sending e-mails** and **spamming someone given their e-mail address**
## Using mailbot to send an e-mail :
Execute the following script and pass as a parameter in this order : **the content of the e-mail** and the **receiver's e-mail address** as shown in the following syntax :
```
$ python3 mailbot.py <message_to_send> <receivers_address>
```
for example
```
$ python3 mailbot.py this was sent from a bot lilywolf272@gmail.com
```
## Using mailbot to spam 
Execute the bash script and pass as a parameter the e-mail address that you want to spam as shown in the following syntax :
```
$ bash spam <receivers_address>
```
for example
```
$ bash spam lilywolf272@gmail.com
```
**NB** : To go faster, you can grant yourself the reading and executing permissions to execute the bash script faster by executing :
```
$ chmod 777 spam 
```
in this case, all you'll have to do to spam someone is the following :
```
$ ./spam <address_to_spam>
```
## Requirements :
- the [quick-mailer](https://pypi.org/project/quick-mailer/) library that can be installed using pip :
```
$ pip install quick-mailer
```

