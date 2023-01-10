let x = 1

getAllComments();
function addComment() {
  var comment_area = document.getElementById("CommentArea").value;
  localStorage.setItem(x.toString(), comment_area);
  getAllComments();
  comment_area.innerText = '';
  x += 1;
}

function getAllComments() {
  document.getElementById("Comments").innerHTML = '';
  const element = document.getElementById("Comments");

  for (let i = 0; i<localStorage.length; i++) {
    const para = document.createElement("p");
    para.innerText = localStorage.getItem(localStorage.key(i));
    element.append(para);
  }
}
