const user_id = $("meta[name=user_id]").attr("content")

$.ajax({
  url: "/agenda/get/${user_id}",
  type: "GET",
  beforeSend: () => { 
    let html = "";
    html += `
    <div class="card">
      <div class="card-body">
        <h2>Loading...</h2>
      </div>
    </div>
    `;

    $("#agenda").html(html);
  },
}).done((data) => {
    let html = "";
    // data = list of todo
    
    for (let i = 0; i < data.length; i++) {
        html += `
        <div class="card" style="width: 18rem;">
          <div class="card-body">
            <h3 class="card-title">${data[i].fields.judul}</h5>
            <h6 class="card-subtitle mb-2">${data[i].fields.matkul}</h6>
            <h6 class="card-subtitle mb-2" style="color:red;">${data[i].fields.tanggal} ${data[i].fields.waktu}</h6>
            <p class="card-text">${data[i].fields.keterangan}</p>
            <a href="/agenda/delete/${data[i].pk}" class="btn btn-danger bottom">Hapus</a>
          </div>
        </div>
        `;
      }
      
      // document.getElementById("agenda").innerHTML = html;
      $("#agenda").html(html);
});