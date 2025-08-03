document.title = "Aku suka java script"


const body = document.body
body.append("Java script adalah salah satu bahasa pemograman terfavorit")

body.style.fontSize = "25px"
body.style.backgroundColor = "skyblue"
body.style.fontFamily = "sans-serif"

const h1 = document.createElement("h1")
h1.textContent = "AKU SUKA KAMU"
body.append(h1)
h1.style.color = "pink"

const button = document.createElement("button")
button.textContent = "Klik aku jika anda suka❤️"
body.append(button)
button.style.backgroundColor = "pink"
button.style.width = "100px"
button.style.border = "none"
button.style.padding = "10px"
button.style.borderRadius = "22px"
button.style.boxShadow = "4px 10px 20px  black"

const btn = document.getElementById("btn")
const list = document.querySelector(".list")

btn.style.border = "none"
btn.style.padding = "10px"
btn.style.backgroundColor = "pink"
btn.style.fontSize = "20px"
btn.style.boxShadow = "4px 10px 20px  black"
btn.style.borderRadius = "22px"

list.style.color = "pink"

function gantiWarna() {
    btn.style.backgroundColor = "yellow"
    alert("Mantap anda telah mengubah warna tombol anda menjadi warna kuning")
}
  
function gantiText() {
    btn.textContent = "KLIK AKU TANTE"
}

function kembali() {
    btn.textContent = "KLIK AKU MAS"
}
