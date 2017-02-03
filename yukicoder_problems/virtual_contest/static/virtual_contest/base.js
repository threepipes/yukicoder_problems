jQuery(function(){
    $('#add_problem').click(function(){
        var size = $('#added_problems').length;
        var form = $(':text#input_problem');
        var name = form.val();
        form.val('')
        $('#added_problems').append(
            '           <div id="problem_'+size+'">'+
            '               <input type="hidden" name="problem[]" value="116">'+
            '               <div class="col-sm-6">'+name+'</div>'+
            '               <div class="col-sm-6">'+
            '                   <button class="btn btn-default delete" type="button">削除</button>'+
            '                </div>'+
            '           </div>'
        );
    });

    $('#added_problems').on('click', '.delete', function(){
        $(this).parent().parent().remove();
    });
});
