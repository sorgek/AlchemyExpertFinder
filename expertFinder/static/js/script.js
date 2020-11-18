var contract = document.getElementsByClassName("caret");
var i;

for (i = 0; i < contract.length; i++) {
  contract[i].addEventListener("click", function() {
    this.parentElement.querySelector(".nested").classList.toggle("active");
    this.classList.toggle("caret-down");
  });
}