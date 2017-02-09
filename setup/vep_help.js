// Script to create dxapp.json entries from the VEP options page (http://asia.ensembl.org/info/docs/tools/vep/script/vep_options.html)
// Execute this in a browser to print out the json data

let a = []
for (let x of document.querySelectorAll('table.ss tr')) {
    let rows = x.querySelectorAll('td');
    if (rows.length == 3)
        a.push({
            name: rows[0].innerText.trim(),
            label: rows[0].innerText.trim(),
            class: "boolean",
            optional: true,
            default: false,
            help: rows[2].innerText.trim()
        })
}

console.log(JSON.stringify(a, null, 4))