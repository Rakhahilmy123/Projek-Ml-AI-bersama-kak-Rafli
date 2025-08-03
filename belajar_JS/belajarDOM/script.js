// belajar javascript DOM Selection bersama sandhika galih
const judul = document.getElementById("judul")
judul.style.backgroundColor = "skyblue"
judul.style.color = "white"
judul.innerHTML = "Rakha Hilmy"
judul.style.boxShadow = "10px 10px 5px  black"

const container = document.getElementById("container")
container.style.backgroundColor = "yellow"
container.style.fontSize = "20px"
container.style.fontFamily = "sans-serif"
container.style.boxShadow = "10px 10px 5px  black"

const p = document.getElementsByTagName("p")
for (i = 0;i < p.length; i++) {
    p[i].style.backgroundColor = "skyblue"
}

const p1 = document.getElementsByClassName("p1")
p1[0].innerHTML = "Aku suka banget coding"

const p2 = document.getElementsByClassName("p2")
p2[0].innerHTML = "Aku sayang kamu"

const p4 = document.querySelector("#b p")
p4.style.color = "red "
p4.style.fontSize = "30px"

const li2 = document.querySelector("section#b ul li:nth-child(2) ")
li2.style.backgroundColor = "orange"