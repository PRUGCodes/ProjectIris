![image](https://user-images.githubusercontent.com/61810022/109414638-82f48a00-7979-11eb-894a-02dd866f98e0.png)

## Team null's awesome project created for AngelHacks 2.0! 

For our AngelHacks 2.0 project "Notes of Kindness," we decided to create a django-based web-application dedicated to spreading kindness to our users.

Our (awesome) site allows users to input a kind message to an anonymous receiver, and once sent, they will receive an anonymous kind message in return!

### How do _I_ submit a kind note?!

All you have to do is go to our [website](http://notesofkindness.hmorin.com) and write your own positive note for someone else to read! <br/><br/>

### What if someone uses profane language in their message? :(

It's ok! By utilizing python's _better_profanity_ library, our app can determine whether or not a message includes negative words and deletes it before it can reach anyone. <br/><br/>


### Won't I get repeated messages? 

Sadly, there will be some repeated messages due to the nature of the site, but we tried our best to counteract this by deleting any messages that have been received by someone as long as the number of messages currently held in our database meets a certain threshold.
<br/><br/><br/>

![image](https://user-images.githubusercontent.com/61810022/109416725-a3c2dc80-7985-11eb-9019-321ce24258b0.png)
![image](https://user-images.githubusercontent.com/61810022/109416828-22b81500-7986-11eb-9d1b-5aa35f6abf53.png)


<br/><br/>Steps to deploy:
```
    pip install django
    pip install better-profanity
    python manage.py makemigrations
    python manage.py migrate
    python manage.py runserver
```
