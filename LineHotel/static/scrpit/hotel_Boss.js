/// <reference path="jquery.d.ts" />
$(document).ready(function() {


    Auto();

    
});




function Auto(){
    var fs=setInterval(function(){
        if(typeof(userID)!="undefined"){
            GetHotel_data();
            
            clearInterval(fs);
        }
    },1000)
}


function GetHotel_data(){
    $.ajax({
        async: false,
        url: '../api/GetBossData',  // url位置或請求路徑
        type: 'POST',   // post/get
        contentType: "application/json", //送出資料為 json
        data: JSON.stringify ({ "userID": userID}),
                                  // 送出的 json 資料
        error: function (xhr) {
          
          return false;
         }, // 錯誤後執行的函數
        success: function (response) { 
            if(response.len==0){
                $("#nohotel").css("display","block");
                $("#hotel_list").css("display","none");
            }else{
                $("#nohotel").css("display","none");
                $("#hotel_list").css("display","block");
            }
            alert(response.len);
          //response.userID); 
            return true;
           
        } // 成功後要執行的函數
    });

}