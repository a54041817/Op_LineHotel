function post(url,data){
    $.ajax({
        type: 'POST',                     //GET or POST
        url: url,               //請求的頁面
        cache: false,                     //防止抓到快取的回應
        data: data,      //要傳送到頁面的參數
        success: functionSucceed,         //當請求成功後此事件會被呼叫
        error: functionFailed,            //當請求失敗後此事件會被呼叫
        statusCode: {                     //狀態碼處理
          404: function() {
            alert("page not found");
          }
        }
    });
}