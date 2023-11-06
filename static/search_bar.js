function redirigir() {
    var texto = document.getElementById("search-character-input").value;
    if (texto.trim() === "") {
        texto = "none";
    }
    window.location.href = "/search/q=" + texto;
}
