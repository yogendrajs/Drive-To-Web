## Images By Google Drive API

### About the Project

In this project, I have shown the images of the public folder **Images** of my Drive, to the web-browser using **Google-Drive-API**, without using any database in Django/Python. I have also attached image-slider in the html, so that everyone can view all the images by scrolling them.

### Requirements

If you're using Linux-based system, open your terminal, and follow the given commands.
To install python3 to your system, type

```
sudo apt-get update && sudo apt-get install python3
```
Now, you need to install `pip`, (Python-Installs-Package), python's package manager. <br />
To install necessary frameworks and libraries, type

```
pip3 install -r requirements.txt
```
If you want more knowledge and about its installation process, you can walk through the following link. <br />
https://docs.djangoproject.com/en/2.2/intro/tutorial01/

If you're using Windows, download Django from its official website <br />
https://www.djangoproject.com/download/

#### How To Run?

Open your Terminal and navigate to the directory where your `manage.py` file is located and, type the following command to start your localhost server.
Note: If you don't mention any port, it will automatically get started at port 8000.
```
python3 manage.py runserver
```

To kill the port, type <br />
```
netstat -ntlp
``` 
to get your port's process Id (PID)

To kill that process, type <br />
```
kill -9 PID
```

Now, open your browser, and type the following URL: <br />
http://localhost:8000/ to show all the images.