from django.db import models

# Create your models here.

class Board(models.Model):
    customer_id = models.CharField('아이디',max_length=20)
    title = models.CharField('인원수',max_length=200)
    pub_date = models.DateTimeField(auto_now_add=True)
    body = models.TextField('요청사항')
    reservation_date = models.DateField('예약날자')
    reservation_time = models.TimeField('예약시간')
    author = models.CharField('승인여부',max_length=20, blank=True)

    def __str__(self):
        return self.title


class Img_board(models.Model):
    title = models.CharField('제목', max_length=200)
    estimation = models.CharField('평점',max_length=10)
    image = models.ImageField('사진',upload_to='images/')
    description = models.TextField('내용')

    def __str__(self):
        return self.title