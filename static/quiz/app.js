(function(){
    let interval = setInterval(inter, 1000);
    let openModal = document.getElementById("open")
    let closeModal = document.getElementById("close")
    window.opens = false
    let modal = document.querySelector('.modal-wrapper')
    let modalArea =document.querySelector('.modal-wrapper').children[0]
    openModal.addEventListener("click", open)
    closeModal.addEventListener("click", close)
    modalArea.addEventListener("click", e=>{
        e.stopPropagation()
    })
    
    function open(e){
        window.opens = true
        if(modalArea.classList.contains("reverse")){
            modalArea.classList.remove("reverse");
            clearInterval(interval)
        }
        modal.style.display = "flex";
    
       
    }
    
    function close(e){
        e.stopPropagation()
        modalArea.classList.add("reverse");
        window.opens = false
        location.href = "/"
        clearInterval(interval)
        
        setTimeout(e=>{
            modal.style.display = "none"
        },600)
    
       
    }

    let timeElement = document.querySelector(".time")
    let time =  timeElement.innerHTML * 60
    function inter(){
        timeElement.innerHTML = time
        var m = Math.floor(time/60)
        var s = time % 60
        timeElement.innerHTML = `${m}m ${s}s`
        if(time <= 0){
            if(!window.opens){
                sender.click()
            }
             time=0;
             clearInterval(interval)
        }else{
             time--;
        }
       

    }
    



    
    }())

