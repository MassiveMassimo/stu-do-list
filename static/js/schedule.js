const userId = $("meta[name=user_id]").attr("content")

$.get(`/schedule-kuliah/get-jadwal/${userId}`, function (data) {

    // construct html
    let html = ""

    // data is a JS object (dict equivalent in python)
    // iterate object keys
    for (const matkul in data) {

        html += `
        <div class="d-flex align-items-end mb-3">
                <h1 style="font-size:32px;" class="fw-bold text-center mr-4">${matkul}</h1>
                <a class=text-sm text-gray-500 whitespace-no-wrap border-b border-gray-200" href = "/schedule-kuliah/add-jadwal/${data[matkul].id}">
                    <svg xmlns="http://www.w3.org/2000/svg" class="w-6 h-6 text-blue-400 mb-0.5" fill="none"
                            viewBox="0 0 24 24" stroke="currentColor">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                            d="M11 5H6a2 2 0 00-2 2v11a2 2 0 002 2h11a2 2 0 002-2v-5m-1.414-9.414a2 2 0 112.828 2.828L11.828 15H9v-2.828l8.586-8.586z" />
                    </svg>
                </a>
                <a class="y-0 e-0 s-0 text-sm text-gray-500 whitespace-no-wrap" href = "/schedule-kuliah/delete-matkul/${data[matkul].id}" style="margin-bottom: 2.8px">
                        <svg xmlns="http://www.w3.org/2000/svg" class="w-6 h-6 text-red-400 m-auto" fill="none"
                        viewBox="0 0 24 24" stroke="currentColor">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                        d="M19 7l-.867 12.142A2 2 0 0116.138 21H7.862a2 2 0 01-1.995-1.858L5 7m5 4v6m4-6v6m1-10V4a1 1 0 00-1-1h-4a1 1 0 00-1 1v3M4 7h16" />
                        </svg>
                    </a>
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
                <td style="width:2%;">
                    <a class="y-0 e-0 s-0 text-sm text-gray-500 whitespace-no-wrap border-b border-gray-200" href = "/schedule-kuliah/delete-jadwal/${jadwal.pk}">
                        <svg xmlns="http://www.w3.org/2000/svg" class="w-6 h-6 text-red-400 m-auto" fill="none"
                        viewBox="0 0 24 24" stroke="currentColor">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                        d="M19 7l-.867 12.142A2 2 0 0116.138 21H7.862a2 2 0 01-1.995-1.858L5 7m5 4v6m4-6v6m1-10V4a1 1 0 00-1-1h-4a1 1 0 00-1 1v3M4 7h16" />
                        </svg>
                    </a>
                </td>
            </tr>
            `
        }
        html += "</tbody>"
        html += `</table>`
        html += `</div>`
    }

    $("#table-jadwal").html(html)
})

{/* <td>
                    <a class="btn btn-outline-danger" href="/schedule-kuliah/delete-jadwal/${jadwal.pk}">delete</a>
                </td> */}