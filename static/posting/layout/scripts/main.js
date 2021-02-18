window.addEventListener("load", e=>{
    var content = document.querySelector("#top")
    content.style.opacity = 1;


})
function toggle_term(){
  if (localStorage.accept_term === 'true'){
    document.querySelector(".cookies").style.opacity = 0
  }else{
    document.querySelector(".cookies").style.display = 1
  }
}
toggle_term()
const accept = document.querySelector(".accept")
const rejuse = accept.nextElementSibling

accept.addEventListener("click", (e)=>{
  //hide cookie and set localstorage to true
  localStorage.accept_term = 'true'
  console.log("use")
  toggle_term()
})
rejuse.addEventListener("click", (e)=>{
  //hide cookie and set localstorage to false
  localStorage.accept_term = 'false'
  document.querySelector(".cookies").style.opacity = 0
})

if (document.querySelector("#id_comments")){
    btns = document.querySelectorAll(".replay")
    btns.forEach(btn => {
        btn.addEventListener("click", (e)=>{
        ids = e.target.id
        var seletor = "."+"form"+ids;
        forms = document.querySelector(seletor);
  
        if(forms.parentNode.style.display == "none"){
          forms.parentNode.style.display =  "block"
          e.target.textContent= "Cacher"
        }else{
          forms.parentNode.style.display = "none"
          e.target.textContent= "Répondre"
        }
        })
    });
  
    function createComment(uniqueClass, action){
       let Ajaxrequest = new XMLHttpRequest()
       Ajaxrequest.onreadystatechange = function(e){
           if (Ajaxrequest.readyState === 4){
              const revec_data = JSON.parse(Ajaxrequest.responseText)
              if(revec_data.login){
                  alert("Vous devez vous connecté ")
              }else if (revec_data.response){
                 location.reload()
              }
           }
       }
       Ajaxrequest.open("POST",action, true)
       Ajaxrequest.setRequestHeader("X-Requested-With", "XMLHttpRequest")
       formdata = document.querySelector("."+uniqueClass)
       let data = new FormData(formdata)
       Ajaxrequest.send(data)
    }
  
    replayforms = document.querySelectorAll(".replayform")
    function submitForm(e){
      e.preventDefault();
      const load_svg = document.getElementById("svg-2")
      if(e.target.lastElementChild.innerHTML === "envoyer"){
          e.target.lastElementChild.innerHTML += load_svg.innerHTML
      }
    
      const unique = e.target.classList[0]
  
      createComment(unique,e.target.action)
  
    }
    replayforms.forEach(form =>{
      form.addEventListener('submit', submitForm)
    })
  }
    
  
   