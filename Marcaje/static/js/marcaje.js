

const marcaje = document.querySelector('#form-marcaje');

marcaje.addEventListener("submit",function(e){
    
    e.preventDefault();

    let check_tipo = document.getElementsByName('tipo');
    const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;

    let tipo;

    console.log(check_tipo);

    for (let i = 0; i < check_tipo.length; i++) {

        if(check_tipo[i].checked){
            tipo = check_tipo[i].value;
        }
    }
    console.log(tipo);
    
    let fd = new FormData();
    fd.append('tipo', tipo);
    
    fetch('/marcaje/',
    {
        method: 'POST',
        body: fd,
        headers: {
            'X-CSRFToken': csrftoken
        }
    })
    .then(function(res){
        return res.json();
    })
    .then(data => {
        console.log(data);
          if (data.status === 200) {
              const mostrar_marcas = document.getElementById('contenedor-marcaje');
              let card_hora = document.createElement('div');
              card_hora.setAttribute('class','card');
              let card_hora_body = document.createElement('div');
              card_hora_body.setAttribute('class','card-body');
              card_hora_body.innerHTML = `<label>Marca: ${data.tipo} Hora: ${data.hora}</label>`;
              mostrar_marcas.append(card_hora);
              card_hora.append(card_hora_body);

          }else if(data.status === 300){
              alert(data.message);
          }else if(data.status === 500){
            alert(`error de servidor`);
        }
    })
    .catch( data => {
        alert(data);
    })

});