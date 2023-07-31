window.onload = function () {
    const registroForm = document.getElementById('registroForm')
    const mensajeErrorRegistro = document.getElementById('mensajeErrorRegistro')

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
                //TODO: Mejorar para los mensajes de error
                console.log('Hay Error')
                console.log(JSON.stringify(data.errors))
                mensajeErrorRegistro.innerHTML = data.errors;
               
            }else{
                location.href="./registroRealizado/" + data.email;
            }
        
        })
        .catch( error => console.error(error))
        

    })


    const closeBtn = document.querySelector('.close');
    closeBtn.addEventListener('click', () => {
        mensajeErrorRegistro.innerHTML = null;
    });
}