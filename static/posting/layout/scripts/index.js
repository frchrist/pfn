function addsvg(){
  const svg = document.querySelector(".hide")
  const load_area = document.querySelectorAll(".loader")
  load_area.forEach(loader =>{
  loader.innerHTML = svg.innerHTML;
})}
addsvg()


let infinite = new Waypoint.Infinite({
    element:$(".infinite")[0],
    offset : "bottom-in-view",

    onBeforePageLoad: function(){


      var parent = document.querySelector(".infinite-more-link")
      parent.innerHTML = "chargement..."
    },
    onAfterPageLoad: function(){
      load()
      addsvg()

    }

  })
  const ratio = .5
  const option = {
    root:null,
    rootmargin:"0px",
    threshold:ratio
  }
  function load(){
    const callback = function(entries, observe){
    entries.forEach(entry=>{
      // var img = entry.target
      
      if(entry.intersectionRatio > ratio){
       var img = entry.target
       img.style.display = "none"
        img.setAttribute("src", img.getAttribute('data-src'))
        img.addEventListener('load', (e)=>{
          img.previousElementSibling.style.display = "none";
          img.style.display = "inline-block";
        })

        observe.unobserve(entry.target)
      }

    })
  }
  const intersection = new IntersectionObserver(callback, option)
  document.querySelectorAll('.lazy').forEach(e =>{
    intersection.observe(e)
  })
  }
  load()