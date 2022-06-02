message_card = document.getElementById('close');
console.log('success')
message_card.addEventListener('click', ()=>{
    console.log('add style')
    document.getElementById('success_message').style.display='none'
})