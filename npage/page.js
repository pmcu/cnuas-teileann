var addrs= [
"page.html",
"next.html",
"2next.html",
"3next.html",
];

var x= 0;
function myFunction(x)
{ location= addrs[x];
}

function goBack() {
  window.history.back();
}
