import board
from django.shortcuts import redirect, render
from .models import Board
from .forms import BoardForm
from gesiuser.models import Gsuser
# Create your views here.

def board_detail(request, pk):
    board = Board.objects.get(pk = pk)

    return render(request,'board_detail.html', {'board' : board})

def board_list(request):
    boards = Board.objects.all().order_by("-id")
    return render(request,'board_list.html', {'boards':boards})


def board_write(request):
    if request.method == 'POST':
        form = BoardForm(request.POST)
        if form.is_valid():
            user_id = request.session.get('user')
            gsuser = Gsuser.objects.get(pk=user_id)
            board = Board()
            board.title = form.cleaned_data['title']
            board.contents = form.cleaned_data['contents']
            board.writer = gsuser
            board.save()

            return redirect('/board/list/')
    
    else:
        form = BoardForm()
    return render(request,'board_write.html',{'form' : form})