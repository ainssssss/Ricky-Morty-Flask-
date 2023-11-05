function redirigir() {
    var texto = document.getElementById("search-character-input").value;
    window.location.href = "/search/q=" + texto;
}