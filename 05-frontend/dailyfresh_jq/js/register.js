$(function(){

    var error_name = false;
    var error_pwd = false;
    var error_cpwd = false;
    var error_email = false;
    var error_allow = false;

    $('#user_name').blur(function () {
        check_username();
    });

    $('#user_name').focus(function () {
        $(this).next().hide();
    });

    $('#pwd').blur(function () {
        check_pwd();
    });

    $('#pwd').focus(function () {
        $(this).next().hide();
    });
    
    $('#cpwd').blur(function () {
        check_cpwd();
    });

    $('#cpwd').focus(function () {
        $(this).next().hide();
    });
    
    $('#email').blur(function () {
        check_email();
    });

    $('#email').focus(function () {
        $(this).next().hide();
    });
    
    $('#allow').click(function () {
        if($(this).prop('checked') == true){
            error_allow =false;
            $('.error_tip2').hide();
        }
        else{
            error_allow = true;
            $('.error_tip2').html('請勾選同意').show();
        }
        
    });

    function check_username() {

        var val = $('#user_name').val();
        var re = /^\w{5,15}$/i;

        if(val == ''){
            $('#user_name').next().html('用户名不能為空！')
            $('#user_name').next().show();
            error_name = true;
            return;
        }

        if(re.test(val)){
            error_name = false;
        }
        else{
            eror_name = true;
            $('#user_name').next().html('用户名包含5到15個英文,数字,"_"')
            $('#user_name').next().show();
            return;
        }
    }

    function check_pwd() {
        var val = $('#pwd').val();
        var re = /^[a-zA-Z0-9@\$\*\.\!\?]{6,16}$/;

        if(val == ''){
            $('#pwd').next().html('密碼不能為空！')
            $('#pwd').next().show();
            error_pwd = true;
            return;
        }

        if(re.test(val)){
            error_pwd = false;
        }
        else{
            eror_pwd = true;
            $('#pwd').next().html('密碼包含6到16的英文,数字,@$*.!?')
            $('#pwd').next().show();
            return;
        }

    }

    function check_cpwd() {
        var val = $('#pwd').val();
        var cval = $('#cpwd').val();

        if(val == cval){
            error_cpwd = false;
        }
        else{
            error_cpwd = true;
            $('#cpwd').next().html('兩次密碼不相同');
            $('#cpwd').next().show();
            return;
        }

    }

    function check_email(){
        var re = /^[a-z0-9A-z][\w\.\-]*@[a-z0-9\-]+(\.[a-z]{2,5}){1,2}$/;
        var val = $('#email').val();

        if(val==''){
            $('#email').next().html('郵箱不能為空！')
            $('#email').next().show();
            error_email = true;
            return;
        }

        if(re.test(val))
        {
            $('#email').next().hide();
            error_email = false;
        }
        else
        {
            $('#email').next().html('你输入的邮箱格式不正确')
            $('#email').next().show();
            error_email = true;
        }
    }

    $('.reg_form').submit(function () {
        check_username();
        check_pwd();
        check_cpwd();
        check_email();

        if(error_name == false && error_pwd == false && error_cpwd ==false && error_email == false && error_allow == false ){
            return true;
        }
        else{
            return false;
        }

    });

});