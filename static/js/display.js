function test(obj){

    var div1=document.getElementById("div2");
    if(div1.style.display=="block"){
        div1.style.display="none";
        obj.src="/static/image/up.ico";
    }else{
        div1.style.display="block";
        obj.src="/static/image/down.ico";
    }
}