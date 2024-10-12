

if (tipoUsuario && menuAdministrar) {
    const texto = tipoUsuario.textContent || tipoUsuario.innerText;
    if (!texto.includes('Administrador')) { 
        menuAdministrar.style.display = 'none'; 
    }
}