


const formLogin = document.querySelector('#form-login');

formLogin.addEventListener('submit', function(e){

    e.preventDefault();

    const usuario = document.getElementById('usuario').value;
    const password = document.getElementById('password').value;
    const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;

    let fd = new FormData();
    fd.append("usuario",usuario);
    fd.append("password",password);

    fetch('',
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
              let url = '/marcaje/'
              window.location.href = url;
          }else if(data.status === 100){
              alert(`Usuario y/o contraseña incorrectos`);
          }else if(data.status === 500){
            alert(`error de servidor`);
        }
    })
    .catch( data => {
        alert(data);
    })

});



    

