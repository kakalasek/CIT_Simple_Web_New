let blogForm = document.getElementById('blogform')
const apiUrl = 'http://192.168.10.111/hello'

fetch(apiUrl).then(response => {
    if (!response.ok) {
        throw new Error('Network response was not ok')
    }
    return response.json()
}).then(data => {
    console.log(data)
})

blogForm.addEventListener("submit", (e) => {
    e.preventDefault();

    let text = document.getElementById("text").value;
    let user = document.getElementById("user").value;

    let comments = document.getElementById("comments")

    let comment = document.createElement("div")
    comment.classList.add("comment")

    let commentUser = document.createElement("div")
    commentUser.classList.add("comment-user")
    commentUser.innerHTML = user

    let commentContent = document.createElement("div")
    commentContent.classList.add("comment-content")
    commentContent.innerHTML = text

    comment.appendChild(commentUser)
    comment.appendChild(commentContent)

    comments.appendChild(comment)
});
