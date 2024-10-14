

if (tipoUsuario && menuAdministrar) {
    const texto = tipoUsuario.textContent || tipoUsuario.innerText;
    if (!texto.includes('Administrador')) { 
        menuAdministrar.style.display = 'none'; 
    }
}

function confirmarGuardar() {
    return confirm('¿Estás seguro de que deseas guardar los cambios?');
}