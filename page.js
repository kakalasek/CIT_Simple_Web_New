let blogForm = document.getElementById('blogform')

let text = ""
let user = ""

blogForm.addEventListener("submit", (e) => {
    e.preventDefault();

    text = document.getElementById("text").value;
    user = document.getElementById("user").value;

});
