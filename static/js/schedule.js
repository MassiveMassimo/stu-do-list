const userId = $("meta[name=user_id]").attr("content")

$.get(`/schedule-kuliah/get-jadwal/${userId}`, function (data) {

    // construct html
    let html = ""

    // data is a JS object (dict equivalent in python)
    // iterate object keys
    for (const matkul in data) {

        html += `
        <div class="d-flex justify-content-between align-items-center mb-3">
                <h1>${matkul}</h1>
                <a class="btn btn-primary" href="/schedule-kuliah/add-jadwal/${data[matkul].id}">Add Jadwal</a>
        </div>`

        html += `<div class="w-100 overflow-auto">`

        html += `<table class="table table-striped mb-5">`

        html += `
        <thead>
            <tr>
                <th scope="col">#</th>
                <th scope="col">Hari</th>
                <th scope="col">Waktu dimulai</th>
                <th scope="col">Waktu berakhir</th>
                <th scope="col">Action</th>
            </tr>
        </thead>
        `
        html += "<tbody>"
        const data_length = data[matkul].jadwal.length
        for (let i = 0; i < data_length; i++) {

            const jadwal = data[matkul].jadwal[i]

            html += `
            <tr>
                <th scope="row">${i+1}</th>
                <td>${jadwal.fields.hari}</td>
                <td>${jadwal.fields.start}</td>
                <td>${jadwal.fields.end}</td>
                <td>
                    <a class="btn btn-outline-danger" href="/schedule-kuliah/delete-jadwal/${jadwal.pk}">delete</a>
                </td>
            </tr>
            `
        }
        html += "</tbody>"
        html += `</table>`
        html += `<div>`
    }

    $("#table-jadwal").html(html)
})