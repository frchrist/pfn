function register(sentto, login){
  document.querySelector("#form").addEventListener("submit", (e)=>{
      e.preventDefault()
      if(!document.querySelector("#error").classList.contains("d-none")){
        document.querySelector("#error").classList.add("d-none");
      }
      if(!document.querySelector("#msg").classList.contains("d-none")){
        document.querySelector("#msg").classList.add("d-none");
      }
      document.querySelector(".btn").textContent = "Creation encoure ..."
      $.ajax({
              type: "POST",
              url: sentto,
              data: $("#form").serialize(),
              datatype: "json",
              success: function(data) {
                  if (data.success === "success") {
                     document.querySelector("#msg").classList.remove("d-none");
                     document.querySelector(".btn").textContent = "Terminer"
                     location.href= login
                  }else{
                    if(data.username){
                      document.querySelector("#ierror").innerHTML = data.username
                    }else if(data.email){
                      document.querySelector("#ierror").innerHTML = data.email
                    }else{
                      document.querySelector("#ierror").innerHTML = data.password2
                    }
        
                    document.querySelector("#error").classList.remove("d-none");
                    document.querySelector(".btn").textContent = "Erreur"
                  }
              }
          })
    })

}