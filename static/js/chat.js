const id = JSON.parse(document.getElementById('json-username').textContent);
const message_username = JSON.parse(document.getElementById('json-message-username').textContent);

const socket = new WebSocket(
    'ws://'
    + window.location.host
    + '/ws/'
    + id
    + '/'
);


socket.onopen = function(e){
    console.log("CONNECTION ESTABLISHED");
}

socket.onclose = function(e){
    console.log("CONNECTION LOST");
}

socket.onerror = function(e){
    console.log("ERROR OCCURED");
}

socket.onmessage = function(e){
    const data = JSON.parse(e.data);
    let date = new Date();
    if(data.username == message_username){
        document.querySelector('#chat-body').innerHTML += `<tr>
                                                                <td>
                                                                <p class="bg-success p-2 mt-2 mr-5 shadow-sm text-white float-right rounded">${data.message}</p>
                                                                </td>
                                                                <td>
                                <p><small class="p-1 shadow-sm">${date.getHours()}:${date.getMinutes()}</small>
                                </p>
                            </td>
                                                            </tr>`
    }else{
    if(data.type_msg == 'file') {
                    document.querySelector('#chat-body').innerHTML += `<tr>
  <td>
    <a href='/static/${data.message}' download=''  class="bg-success p-2 mt-2 mr-5 shadow-sm text-white float-left rounded">
      <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-file-earmark" viewBox="0 0 16 16">
  <path d="M14 4.5V14a2 2 0 0 1-2 2H4a2 2 0 0 1-2-2V2a2 2 0 0 1 2-2h5.5L14 4.5zm-3 0A1.5 1.5 0 0 1 9.5 3V1H4a1 1 0 0 0-1 1v12a1 1 0 0 0 1 1h8a1 1 0 0 0 1-1V4.5h-2z"/>
</svg> ${data.message}</a>
  </td> <td><p><small class="p-1 shadow-sm">${date.getHours()}:${date.getMinutes()}</small></p></td></tr>`

    }else{
        document.querySelector('#chat-body').innerHTML += `<tr>
                                                                <td>
                                                                <p class="bg-primary p-2 mt-2 mr-5 shadow-sm text-white float-left rounded">${data.message}</p>
                                                                </td>
                                                                <td>
                                <p><small class="p-1 shadow-sm">${date.getHours()}:${date.getMinutes()}</small>
                                </p>
                            </td>
                                                            </tr>`
         }
    }
}





function isValidHttpUrl(string) {
  let url;
  try {
    url = new URL(string);
  } catch (_) {
    return false;
  }
  return url.protocol === "http:" || url.protocol === "https:";
}

const input = document.getElementById('message_input');
input.addEventListener('change', (event) => {
  if(isValidHttpUrl(input.value)){
  var sogl = confirm("Прикрепляя ссылку на сторонний ресурс вы полность несете ответственноть за любые возможные негативные последствия");
  if(sogl){}
  else{
  input.value = '';
  }
  }

})







document.querySelector('#chat-message-submit').onclick = function(e){
    const message_input = document.querySelector('#message_input');
    console.log('234')
    const message = message_input.value;

    socket.send(JSON.stringify({
        'type_msg':'text',
        'message':message,
        'username':message_username
    }));

    message_input.value = '';
}



input.addEventListener('change', (event) => {
  const target = event.target
  	if (target.files && target.files[0]) {

      /*Maximum allowed size in bytes
        5MB Example
        Change first operand(multiplier) for your needs*/
      const maxAllowedSize = 2 * 1024 * 1024;
      if (target.files[0].size > maxAllowedSize) {
      	alert('File size over 20MB, please select another');
       	target.value = ''
      }
  }
})


document.querySelector('#chat-file-submit').onclick = function(e){

    const message_input = document.querySelector('#id_file');


    const message = message_input.value;
    var new_str = message.split('\\').pop();

    socket.send(JSON.stringify({
        'type_msg':'file',
        'message': new_str,
        'username':message_username
    }));
    window.location.reload();
}