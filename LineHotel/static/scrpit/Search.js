

$(document).ready(function(){
    var Today=new Date();
    var _today=Today.getFullYear()+"-"+(Today.getMonth()+1).toString().padStart(2,'0')+"-"+Today.getDate().toString().padStart(2,'0');
    var maxday=DateAdd("m",8,Today);
    var dminday;
    var _maxday=maxday.getFullYear()+"-"+(maxday.getMonth()+1).toString().padStart(2,'0')+"-"+maxday.getDate().toString().padStart(2,'0');
    
    $("#hotel_pixel").val(poin);
    $("#date_s").attr({
        "value":data_s
    });

    $("#date_d").attr({
        "value":data_d
    });
    $("#man_Len").val(man_Len);


     $("#date_s").attr({
        "value":data_s,
        "min":_today,
        "max":_maxday});
                   
    $("#date_d").attr({
        "value":data_d,
        "min":_today,
        "max":_maxday});

    $("#date_s").change(function(){
        maxday=DateAdd("d",1,new Date($("#date_s").val()));

        _maxday=maxday.getFullYear()+"-"+(maxday.getMonth()+1).toString().padStart(2,'0')+"-"+maxday.getDate().toString().padStart(2,'0');
        $('#date_d').attr({
            "value":_maxday,
            "min":_maxday
            
        });
        });

    $("#gogo").click(function(){
        window.location.href="Search.html?&poin="+$("#hotel_pixel").val()+"&data_s="+$("#date_s").val()+"&data_d="+$("#date_d").val()+"&man_Len="+$("#man_Len").val();
    });
    });

function DateAdd(timeU,byMany,dateObj) {
    var millisecond=1;
    var second=millisecond*1000;
    var minute=second*60;
    var hour=minute*60;
    var day=hour*24;
    var year=day*365;
        
    var newDate;
    var dVal=dateObj.valueOf();
    var date=new Date(dateObj);  // For months
    switch(timeU) {
    case "ms": newDate=new Date(dVal+millisecond*byMany); break;
    case "s": newDate=new Date(dVal+second*byMany); break;    //秒
    case "mi": newDate=new Date(dVal+minute*byMany); break;   //分
    case "h": newDate=new Date(dVal+hour*byMany); break;     //時
    case "m": newDate=new Date(date.setMonth(date.getMonth() + byMany)); break;   //月
    case "d": newDate=new Date(dVal+day*byMany); break;    //日
    case "y": newDate=new Date(dVal+year*byMany); break;   //年
    }
    return newDate;
}