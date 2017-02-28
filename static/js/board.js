$(function () {

	$(".btn-create").click(function(){
		var last_board = $(".row :first-child").attr("board-id");
		if (last_board == undefined){
			last_board = "0";
		}
		var username = $("#user_name").val();
		username = document.getElementById('user_name').value 
		$("#createboard-form input[name='last_board']").val(last_board);
		var urlSend = '/'+ username + '/board/createboard/'

		$.ajax({
			url:urlSend,
			data: $("#createboard-form").serialize(),
			type: 'post',
			cache: false,
			success: function (data){
				$(".row").prepend(data);
			}
		});

	});

	$(".panel-body").on("click", ".remove-board", function (){
		var div = $(this).closest("div");
		var board = $(div).attr("board-id");
		var csrf = $(div).attr("csrf");

		$.ajax({
			url: '/board/remove/',
			data: {
				'board': board,
				'csrfmiddlewaretoken': csrf
			},
			type: 'post',
			cache: false,
			success: function (data){
				$(".row").prepend(data);
			}
		});
	});

});
