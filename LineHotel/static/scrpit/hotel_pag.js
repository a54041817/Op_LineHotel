var jd;
var img_index;
var img_t=1;
var img_title="";
var inx=0;
$(document).ready(function(){

    var data=$('#jdata').text().replaceAll("'","\"");
    var room=[];
    jd=JSON.parse(data);
    document.title=jd.name;
    img_title=jd.name;
    img_index=jd.img.main;
    $("#main").attr({
        "src":img_index
    })
    $("#img_title").text(img_title);
    addimg(img_index,jd.name);

    for(var img in jd.img.else){

        addimg(jd.img.else[img],img);
        img_t++;

    }
    $("#img_else>img").css("width",50/img_t+"vw");

    for(var n=0;n<img_t;n++){
        var keep=$("#img_else>img")[n];

        $(keep).click(function(){
            img_index=$(this).attr("src");
            img_title=$(this).attr("alt");
        });

        $(keep).hover(function(){
            $(this).css("border","1px #BEBEBE solid");
            $("#main").attr({
                "src":$(this).attr("src")
            });
            $("#img_title").text($(this).attr("alt"));
        },function(){
            $("#main").attr({
                "src":img_index
            })
            $(this).css("border","");
            $("#img_title").text(img_title);
        });

    }
    
    for(var data in jd.room){
        if(jd.room[data].room_Len==0)
            continue;
        var room_tit='<div class="room_data"> '+
        "<div>"+
        "<h2>"+data+"</h2>"+
        '<img src="'+jd.room[data].img+'"'+
        'style="display: block ; height: 18vh;">'+
        "</div>"+
        '<div style="width: 20vw;">';
        for(var tit in jd.room[data].conform){
            room_tit=room_tit+"<h3>"+tit+":"+jd.room[data].conform[tit]+"</h3>";
        }
        
        room_tit=room_tit+"</div>"+
                '<div style="position:relative;">'+'<h3 style="position: absolute;bottom: 0px;height: 5vh;width: 10vw;font-size:10px">剩下'+jd.room[data].room_Len+'間</h3>'+
                            '<button id="room'+inx+'"'+' style="position:absolute;bottom:0px;right:0px;width: 10vw;height: 5vh;"'+
                            '>訂此房</button></div></div>';
                            
 
        $('#indata').append(room_tit);

        $('#room'+inx).click(function(){
            chick('')
        });
        inx++;
        
    }


}



)

function addimg( src ,alt){
    $("#img_else").append('<img src="'+src+'" alt="'+alt+'">');
}

function chick(id){
    var S_Date=$("#date_s");
    var E_Date=$("#date_d");
    var Len_man=$("#man_Len");
    var _txt=$("#txt");

    if(_name.val()==""){
  
      alert("請至少輸入姓名");
      return 0;
    }
    $.ajax({
        async: false,
        url: '/cjick_hotel.html',  // url位置或請求路徑
        type: 'POST',   // post/get
        contentType: "application/json", //送出資料為 json
        data: JSON.stringify ({ "S_Date": S_Date.val(),
                                "E_Date":E_Date.val(),
                                "Len_man":_sname.val(),
                                "update":_update.val(),
                                "pers":_pers.val(),
                                "interest":_interest.val(),
                                "log":_txt.val(),
                                "gender":_gender,
                                "work":_work.val(),
                                "birthday":_birthday.val(),
                              "userID":liff_userID}),
                                  // 送出的 json 資料
        error: function (xhr) {
          
          return false;
         }, // 錯誤後執行的函數
        success: function (response) { 
          send_message(response.friendID);
          _data=response.friendID;
            return true;
           
        } // 成功後要執行的函數
    });
  }