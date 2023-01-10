
function addComment() {
  var x = document.getElementById("CommentArea").value;
  const element = document.getElementById("Comments");
  const para = document.createElement("p");
  para.innerText = x;
  element.append(para);
}
