$(function () {

	$(".btn-create").click(function(){
		$.ajax({
			url:'/blog/post/',
			data: $("#createblog-form").serialize(),
			type: 'post',
			cache: false,

		});

	});

	$(".panel-body").on("click", ".remove-blog", function (){
		var div = $(this).closest("div");
		var blog = $(div).attr("blog-id");
		var csrf = $(div).attr("csrf");

		$.ajax({
			url: '/blog/remove/',
			data: {
				'blog': blog,
				'csrfmiddlewaretoken': csrf
			},
			type: 'post',
			cache: false,

		});
	});

});
