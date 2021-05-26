"use strict";

fetch("./ranking.json").then(function(resp){
    return resp.json();
}).then(function(data){
    var rank = document.getElementById("ranks");
    var contenttop = document.getElementById("contenttop3");
    console.log(data.fetch)
    contenttop.innerHTML += "<span id=\"ranktop2\"><img src="+data[1].url_avatar+" id=\"round2\" /><h1>#2</h1> </span>"
    contenttop.innerHTML += "<span id=\"ranktop3\"><img src="+data[2].url_avatar+" id=\"round3\" /> <h1>#3</h1> <span></span> </span>"
    contenttop.innerHTML += "<span id=\"ranktop1\"><img src="+data[0].url_avatar+" id=\"round1\" /><img id=\"crown\" src=\"img/crown.png\"><h1>#1</h1> </span>"

    for (var key in data) {
        var ranking = parseInt(key)+1;
        rank.innerHTML += "<div class=\"rank\"><div class=\"user_level\"><p>"+ranking+"</p></div><img src="+data[key].url_avatar +" class=\"user_pp\"></img><span class=\"user_name\">"+data[key].username+"</span><span class=\"user_experience\"><span class=\"user_experience_level\">lvl</span>"+data[key].level+"</span><hr></div>";        
    }


    console.log(data["0"].username);
});
