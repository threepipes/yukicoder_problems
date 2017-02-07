// csrfで弾かれるのを防ぐ
$(document).ajaxSend(function(event, xhr, settings) {

	function getCookie(name) {
		var cookieValue = null;
		if (document.cookie && document.cookie != '') {
			var cookies = document.cookie.split(';');
			for (var i = 0; i < cookies.length; i++) {
				var cookie = $.trim(cookies[i]);
				if (cookie.substring(0, name.length + 1) == (name + '=')) {
					cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
					break;
				}
			}
		}
		return cookieValue;
	}

	function sameOrigin(url) {
		var host = document.location.host;
		var protocol = document.location.protocol;
		var sr_origin = '//' + host;
		var origin = protocol + sr_origin;
		return (url == origin || url.slice(0, origin.length + 1) == origin + '/') ||
			(url == sr_origin || url.slice(0, sr_origin.length + 1) == sr_origin + '/') ||
			!(/^(\/\/|http:|https:).*/.test(url));
	}

	function safeMethod(method) {
		return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
	}

	if (!safeMethod(settings.type) && sameOrigin(settings.url)) {
		xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
	}
});

jQuery(function(){
    $('.btn-add').click(function(){
        var add_type = this.id;
        var content_name = '#'+add_type+'_content';
        var content_type = add_type.slice(4);
        var size = $('#'+content_type).length;
        var form = $(':text#input_'+add_type);
        var name = form.val();

        $.ajax({
            'url': add_type+'/',
            'type': 'POST',
            'data': {
                'id': name,
            },
            'dataType': 'json',
            'success':function(response){
                content = response.name;
                if(content == ''){
                    alert(content_type+' ID: '+name+'は存在しません');
                }else{
                    form.val('');
                    display_name = content;
                    // 文字列じゃなくてjQueryの記法に直す TODO
                    $(content_name).append(
                        '           <div class="'+ content_type +'">'+
                        '               <input type="hidden" name="'+ content_type +'[]" value="'+ name +'">'+
                        '               <div class="col-sm-6">'+ display_name +'</div>'+
                        '               <div class="col-sm-6">'+
                        '                   <button class="btn btn-default delete" type="button">削除</button>'+
                        '                </div>'+
                        '           </div>'
                    );
                }
            },
        });
    });

    $('.added_content').on('click', '.delete', function(){
        $(this).parent().parent().remove();
    });

    $('#submit').click(function(){
        var users = $('.user').length;
        var probs = $('.problem').length;
        var contest_name = $(':text#input_name');
        if(probs == 0){
            alert('問題を追加してください．')
            return;
        }
        if(users == 0){
            alert('参加者を追加してください．')
            return;
        }
        $('#create').submit();
    });

    $('.date').datetimepicker({
        locale: 'ja',
        format : 'YYYY-MM-DD HH:mm:ss'
    });
});
