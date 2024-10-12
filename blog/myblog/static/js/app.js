elemento = document.getElementsByClassName('card');
            console.log(elemento)



const esAdministrador = false; // Cambia esto según la lógica de tu aplicación

// Selecciona el elemento del menú
const menuAdministrar = document.querySelector('#administrar');

// Verifica si el usuario no es administrador y oculta el menú
if (!esAdministrador) {
    if (menuAdministrar) {
        menuAdministrar.style.display = 'none';
    }
}