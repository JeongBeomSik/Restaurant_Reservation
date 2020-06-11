from django import forms
from .models import Board, Img_board

class CreateBoard(forms.ModelForm):
    class Meta:
        model = Board
        fields = ['customer_id','title','body','reservation_date','reservation_time']   


class Img_Board(forms.ModelForm):
    class Meta:
        model = Img_board
        fields=['title','estimation','image','description']