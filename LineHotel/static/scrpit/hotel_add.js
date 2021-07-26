/// <reference path="jquery.d.ts" />
var upImage ;// 页面上input框标签对应的id
var objImage; // 获取第一个文件的对象
var reader  ; // 实例化File对象
var base64String=[];
var _p_data;
var img={};
var key="";
$(document).ready(function() {

    buttADD();

var room=$('.room_list').html();
var imgList=$(".hotel_img_List").html();

    $("#addRoom").click(function(){
        $('#hotel_data_push').append('<div class="room_list">'+room+"</div>")
        $(".room_list").eq($(".room_list").length-1).find("button").click(function(){
            $(this).parent().find(".room_str").append('<input type="text">');
        });
        buttADD();
    });

    $("#addimg").click(function(){
        $('#hotel_data_push').append('<div class="hotel_img_List">'+imgList+"</div>")
        $('.hotel_img_List')[$('.hotel_img_List').length-1].children[0].innerHTML="環境照片"+($('.hotel_img_List').length-1)

            buttADD();

    });

    $("#_post").click(function(){

        input_file_to_base64($(".hotel_main_img> .file")[0]);
        setTimeout(function(){
            _p_data={
                'hotel_name':$("#hotel_name").val(),
                'hotel_address':$("#hotel_address").val(),
                'img':{'hotel_main_img':base64String},
                'room':[]
            }
            for(var j=1;j< $(".hotel_img_List").length;j++){

               _p_data.img.else[$(".hotel_img_List").eq(j).find("input").eq(1)]= $(".hotel_img_List").eq(j).find("input").eq(0)
             
            }

            

        },100);

    })
    
});

function buttADD(){
    for (var i=0 ;i<$(".file").length;i++){
        $(".file").eq(i).change(function (){
            img_print(this,$(this).parent().find("img"))
        })
        $(".remove_div").eq(i).click(function(){
            $(this).parent().remove();
        })
    }
    
    
}
function img_print(input,poin){

    if (input.files && input.files[0]) {

        var reader = new FileReader();

        // 當讀取完成後觸發

        reader.onload = function (e) {

            poin.attr('src', e.target.result);
           
            // 將讀取好檔案顯示在要顯示的Img標籤中。
      }
        reader.readAsDataURL(input.files[0]);
    }

}

function Getimg(){
    base64String=[]
    for(var j=1;j< $(".hotel_img_List").length;j++){
        input_file_to_base64($(".hotel_img_List").eq(j).find("input")[0])
        key=$(".hotel_img_List").eq(j).find("input").eq(1).val();
        setTimeout("img_save("+key+","+j-1+")",5000)
     }
}

function img_save (_kep,img_base){
    console.log(base64String[0]);
    img[_kep]=base64String[img_base];
}

function input_file_to_base64(input){

    upImage =input;
    objImage = upImage.files[0]; 
    reader = new FileReader(); 


    reader.onloadend = function (e) {
        base64String.push(e.target.result);
    }
    if (objImage) {
    //在load中返回一个base64编码
    reader.readAsDataURL(objImage);
    }
    
}