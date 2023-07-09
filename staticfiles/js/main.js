

function login1(){
    var username = document.getElementById('loginusername').value
    var password = document.getElementById('loginpassword').value
    var csrf = document.getElementById('csrf').value

    if(username == '' && password == ''){
        alert('you must enter both')
    }

    var data = {
        'username' : username,
        'password' : password
       }
       fetch('/api/login1/', {
        method : 'POST',
        headers: {
            'content-type' : 'application/json',
            'x-CSRFToken':csrf,

        },
        'body' : JSON.stringify(data)
       }).then(result => result.json())
       .then(response => {
        console.log(response)
       })
}