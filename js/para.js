function myFunction (rd){
var myElements = document.getElementsByTagName("div");
document.getElementById("demo").innerHTML = "The text in the first paragraph is: " + myElements[rd].innerHTML;
}
