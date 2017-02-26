from django.shortcuts import render
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.template.context_processors import csrf
from django.template.loader import render_to_string
from django.http import (HttpResponse, HttpResponseBadRequest,
                         HttpResponseForbidden)

from board.models import Board 
# Create your views here.

BOARDS_NUM_PAGES = 10

def boardhome(request, username):

	all_boards = Board.get_boards()
	all_boards = all_boards.filter(user=request.user)
	paginator = Paginator(all_boards, BOARDS_NUM_PAGES)
	boards = paginator.page(1)
	from_board = -1
	if boards:
		from_board = boards[0].id

	#import pdb; pdb.set_trace()
	return render(request, 'board.html', {
		'boards': boards, 
		'from_board': from_board,
		'page': 1,
		'username': username,
		})

def createboard(request, username):
	#import pdb; pdb.set_trace()
	last_board = request.POST.get('last_board')
	user = request.user
	csrf_token = (csrf(request)['csrf_token'])
	board = Board()
	board.user = user

	title = request.POST['title']
	board.title = title
	content = request.POST['content']
	content = content.strip()

	if len(content):
		board.content = content[:255]
	board.save()
	
	html = _html_feeds(last_board, user, csrf_token)
	
	return HttpResponse(html)

    
def remove(request):
	try:

		board_id = request.POST.get('board')
		board = board.objects.get(pk=board_id)
		board.delete()
		#import pdb; pdb.set_trace()
		return HttpResponse()

	except Exception:
		return HttpResponseBadRequest()


def _html_feeds(last_board, user, csrf_token, board_source='all'):

    boards = Board.get_board_after(last_board)

    #
    #if board_source != 'all':
    #    boards = boards.filter(user__id=board_source)
    html = ''
    for board in boards:
    	if board.user == user:
        	html = '{0}{1}'.format(html,
                               render_to_string('board_item.html',
                                                {
                                                    'board': board,
                                                    'user': user,
                                                    'csrf_token': csrf_token
                                                    }))

    #import pdb; pdb.set_trace()
    return html

def detailBoard(request, username, boardid):
	
	board = Board.objects.get(id=boardid)
	#import pdb; pdb.set_trace()
	return render(request, 'detailBoard.html', {
		'username': username, 
		'board':board,
		})
