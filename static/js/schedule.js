const userId = $("meta[name=user_id]").attr("content")

$.get(`/schedule-kuliah/get-jadwal/${userId}`, function(data) {

    // construct html
    let html = ""

    // data is a JS object (dict equivalent in python)
    // iterate object keys
    for (const matkul in data) {
        html += `
        <tr class="table-header">
            <th colspan="4">
                <h1>${matkul}</h1>
                <a href="/schedule-kuliah/add-jadwal/${data[matkul].id}">Add Jadwal</a>
            </th>
        </tr>`

        html += `
        <tr style="background-color: #C08F73;">
            <th style="width: 25%;">Hari</th>
            <th style="width: 25%;">Waktu dimulai</th>
            <th style="width: 25%;">Waktu berakhir</th>
            <th style="width: 25%;">Action</th>
        </tr>
        `
        const data_length = data[matkul].jadwal.length
        for (let i = 0; i < data_length; i++) {

            const jadwal = data[matkul].jadwal[i]
            
            html += `
            <tr style="background-color: #E8CAB3;">
                <td>${jadwal.fields.hari}</td>
                <td>${jadwal.fields.start}</td>
                <td>${jadwal.fields.end}</td>
                <td>
                    <a href="/schedule-kuliah/delete-jadwal/${jadwal.pk}"><button>delete</button></a>
                </td>
            </tr>
            `
        }
    }

    $("#table-jadwal").html(html)
})