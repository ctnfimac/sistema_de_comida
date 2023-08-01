window.onload = function () {
    const registroForm = document.getElementById('registroForm')
    const mensajeErrorRegistro = document.getElementById('mensajeErrorRegistro')
    const modalErrorRegistro = document.getElementById('modalErrorRegistro')

    modalErrorRegistro.style.display = 'none';

    registroForm.addEventListener('submit', (event) => {
        event.preventDefault()

        fetch(registroForm.action,{
            method: 'POST',
            body: new FormData(registroForm),
            headers:{
                'X-Requested-With': 'XMLHttpRequest',
                'X-CSRFToken': registroForm.elements.csrfmiddlewaretoken.value,
            }
        })
        .then( response => response.json())
        .then( data => {
            if(data.errors){
                if(data.errors.password2){
                    mensajeErrorRegistro.innerHTML = data.errors.password2[0];
                    modalErrorRegistro.style.display = 'block';
                }else if(data.errors.email){
                    mensajeErrorRegistro.innerHTML = 'Ya existe un usuario con el email ingresado';
                    modalErrorRegistro.style.display = 'block';
                }else{
                    console.log('error sin registrar')
                }               
            }else{
                location.href="./registroRealizado/" + data.email;
            }
        
        })
        .catch( error => {
            console.error(error)
        })
        

    })


    const closeBtn = document.querySelector('.close');
    closeBtn.addEventListener('click', () => {
        modalErrorRegistro.style.display = 'none';
        mensajeErrorRegistro.innerHTML = null;
    });
}