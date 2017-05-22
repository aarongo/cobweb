$(document).ready(function () {
  var trigger = $('.hamburger'),
      overlay = $('.overlay'),
     isClosed = false;

    trigger.click(function () {
      hamburger_cross();
    });

    function hamburger_cross() {

      if (isClosed === true) {
        overlay.hide();
        trigger.removeClass('is-open');
        trigger.addClass('is-closed');
        isClosed = false;
      } else {
        overlay.show();
        trigger.removeClass('is-closed');
        trigger.addClass('is-open');
        isClosed = true;
      }
  }
  // $('#toolbar').click(function(e) {
	// 	$.ajax({
  //         url:"/search/",//请求的url地址
  //         dataType:"json",//返回的格式为json
  //         async:true,//请求是否异步，默认true异步，这是ajax的特性
  //         data:{},//参数值
  //         type:"get",//请求的方式
  //         success:function(req){
  //             alert('sssss')
  //         }//请求成功的处理
  //       });
  // });

  $('[data-toggle="offcanvas"]').click(function () {
        $('#wrapper').toggleClass('toggled');
  });
});
