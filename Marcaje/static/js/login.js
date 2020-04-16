


const formLogin = document.querySelector('#form-login');

formLogin.addEventListener('submit', function(e){

    e.preventDefault();

    const usuario = document.getElementById('usuario').value;
    const password = document.getElementById('password').value;
    const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;

    let fd = new FormData();
    fd.append("usuario",usuario);
    fd.append("password",password);

    fetch('/login/',
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
          if (data.status === 200) {
              let url = '/marcaje/'
              window.location.href = url;
          }else{
              alert(`Usuario y/o contraseña incorrectos`);
          }
    })
    .catch( data => {
        console.log(data);
    })

});



    

