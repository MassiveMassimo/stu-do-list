$(document).ready(function() {
    $.ajax({
        url: "/notes/data",
        success: function(response){
            var result = '';
            for(var i = 0; i < response.length; i++){
                var matkul = response[i].fields.matkul;
                result += '<tr>' +'<td style="width: 400px;">'+'<br>' + '<p style="text-align: center;">'+ nama + '</p>'  + '<br>' + '</td>' + '<br>' + '<td style="width: 500px;">' + '<a style="color: #555555;" href="/catatan/{{ i.matkul }}">' + '<br>' + '<p style="text-align: center;">' + matkul + '</p> ' + '<br>'+ '</a>' + '</td>' + '</tr>'
            }
            $('#result-bar').append(result);
        }
    })
})