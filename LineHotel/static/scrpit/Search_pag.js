var index_n=0;
var jd;
var lk=["0","1","2"];
$(document).ready(function(){
    var data=$('#jdata').text().replaceAll("'","\"");
    jd=JSON.parse(data);
    $("#_Serch_len").text(jd.len);
    show_Search(jd);
}
)

function show_Search(_data){
    var max_n=index_n+2;
    var n=1;
    for(var key in _data){
        
        if(index_n>max_n |key=="len"){
            break;
        }
        $("#link"+n).attr({
            "href":"/hotel.html?&id="+_data[key].id+"&poin="+$("#hotel_pixel").val()+"&data_s="+$("#date_s").val()+"&data_d="+$("#date_d").val()+"&man_Len="+$("#man_Len").val()
        });
        $("#img"+n).attr({
            "src":_data[key].img
        });
        $("#t"+n).text(key);
        index_n++;
        n++;
      }
    for(var n=0;n<index_n;n++){

    }
}