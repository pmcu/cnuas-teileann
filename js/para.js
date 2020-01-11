function myFunction (rd){
var myElements = document.getElementsByTagName("p");
document.getElementById("demo").innerHTML = "The text in the first paragraph is: " + myElements[rd].innerHTML;
}
