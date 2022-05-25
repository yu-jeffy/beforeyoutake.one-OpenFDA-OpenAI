$(function(){
	$('button').click(function(){
		var userAddress = $('#inputAddress').val();
		$.ajax({
			url: '/searchFood/',
			data: $('userForm').val(),
			type: 'POST',
			success: function(output){
        $('#outputText').val(output);
				console.log(output);
			},
			error: function(error){
				console.log(error);
			}
		});
	});
});

//
// $('#form').on('submit', function(e){
// 				var number = $('#num').val();
// 				e.preventDefault();
// 				$.ajax({
// 					url: 'http://127.0.0.1:5000/square/',
// 					data: {'number': number},
// 					method: 'POST',
// 					success: function(data) {
// 						$('#num').val('');
// 						$('#square').html('Square of ' + number + ' is ' + data['square'])
// 					}
// 				});
// 			});
