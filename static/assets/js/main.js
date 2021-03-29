/******/ (() => { // webpackBootstrap
/******/ 	"use strict";
/******/ 	var __webpack_modules__ = ({

/***/ "./js_modules/components/detailPage.js":
/*!*********************************************!*\
  !*** ./js_modules/components/detailPage.js ***!
  \*********************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "default": () => (/* binding */ Comments)
/* harmony export */ });
class Comments{
    constructor(){
        const updateNumber = function(){
            document.getElementById("numberOfComment").innerHTML = document.querySelectorAll(".comment-wapper").length + document.querySelectorAll(".replay").length
        }
        
        document.getElementById("js-comment").addEventListener('submit', e=>{
            e.preventDefault()
            sendComment()
        })
        
        const sendComment = function(){
            let commentForm = document.getElementById("js-comment")
            fetch(commentForm.action, {
                method:'POST',
                body:new FormData(commentForm),
                headers:{
                    'X-Requested-With':"XMLHttpRequest",
                }
            }).then((response)=>{return response.json()})
            .then((data)=>{
                commentForm.reset()
                document.querySelector('#js-comments').innerHTML = data.data
                toggleReplayText()
                toggleReplayForm()
                updateNumber()
        
        })
        }
        const sendReplay = function(){
            let commentForm = document.getElementById("replay-form")
            fetch(commentForm.action, {
                method:'POST',
                body:new FormData(commentForm),
                headers:{
                    'X-Requested-With':"XMLHttpRequest",
                }
            }).then((response)=>{return response.json()})
            .then((data)=>{
                document.querySelector('#js-comments').innerHTML = data.data
                toggleReplayText()
                toggleReplayForm()
                updateNumber()
        
        })
        }
        
        
        //reucpere id dans l'espce de comment
        
        
        
         function toggleReplayText(){
            document.querySelectorAll(".comment").forEach(e =>{
                e.onmouseenter = function(x){
                   e.querySelector(".replay__btn").style.opacity = 1;
                }
        
        
                e.onmouseleave = function(x){
                    e.querySelector(".replay__btn").style.opacity = 0;
                 }
            })
        }
        
         function toggleReplayForm(){
            ids = null
            let forms = `
            <form action="{% url 'replay' %}" method="post" id="replay-form">{% csrf_token %}
            {{ReplayForm}}
            <input type="hidden" name="hidden" id="hidden value="">
            <button type="submit">Commenter</button>
            </form>`;
            // console.log("ok")
            let replayBtn = document.querySelectorAll(".replay__btn");
            if(replayBtn.length > 0){
                // si les commentaire existent dans notre page
                for(let i=0; i < replayBtn.length; i++){
                    replayBtn[i].addEventListener('click', function(e){
                        let replayForm = document.querySelector("#replay-form");
                        if(replayForm != null){
                           
                            replayForm.remove()
                        }else{
                            let id= replayBtn[i].getAttribute("id")
                            let parent = document.getElementById(id)
                            parent.nextElementSibling.innerHTML = forms;
                            document.currentReplay_id = id;
                            document.querySelector("#replay-form").addEventListener("submit", e=>{
                                e.preventDefault()
                                document.querySelector("#replay-form").hidden.value = document.currentReplay_id
                                sendReplay()
                            })
        
                        }
                       
                    })
                }
            }
        
        }
        
        // #ajouter des animations de click à tout les button de commentaire
        
        updateNumber()
        toggleReplayText()
        toggleReplayForm()
        
    }

    
}

/***/ }),

/***/ "./js_modules/components/history.js":
/*!******************************************!*\
  !*** ./js_modules/components/history.js ***!
  \******************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "default": () => (/* binding */ History)
/* harmony export */ });

class History{
    constructor(element){
        element.onclick = function(e){
            if(confirm('Voulez vous vraiment quitter cette page ?')){
                window.history.back()
            }
        }
        
    }

}

/***/ }),

/***/ "./js_modules/components/navtoggle.js":
/*!********************************************!*\
  !*** ./js_modules/components/navtoggle.js ***!
  \********************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "default": () => (/* binding */ NavigationBar)
/* harmony export */ });
class NavigationBar{
    constructor(toggleBar){
        this.nav = document.querySelector('.header__top')
        //à chaque fois que la fenetre change de largeurs
        window.onresize = function(e){
            if(window.innerWidth > 700 && !document.querySelector('.header__top').classList.contains("show")){
                document.querySelector('.header__top').classList.add("show")
            }
        }

        // let toggle = document.getElementById('toggle-bar');
        this.element = toggleBar
        this.element.onclick = (e)=>{
                this.toggle()
            }
            
            
            
    }

    toggle(){
            if(!this.nav.classList.contains("show")){
                this.nav.classList.add("show")
                    this.nav.classList.remove("hide")
                    this.element.innerHTML = `<svg height="20px" width="20px" style="fill:white">
                            <use xlink:href="../assets/svg/sprite.svg#times">
                        </svg>`
                }else{
                    this.nav.classList.add("hide")
                    this.nav.classList.remove("show")
                    this.element.innerHTML = `<svg height="20px" width="20px" style="fill:white">
                            <use xlink:href="../assets/svg/sprite.svg#bars">
                        </svg>`
                }
            }       
}

/***/ })

/******/ 	});
/************************************************************************/
/******/ 	// The module cache
/******/ 	var __webpack_module_cache__ = {};
/******/ 	
/******/ 	// The require function
/******/ 	function __webpack_require__(moduleId) {
/******/ 		// Check if module is in cache
/******/ 		var cachedModule = __webpack_module_cache__[moduleId];
/******/ 		if (cachedModule !== undefined) {
/******/ 			return cachedModule.exports;
/******/ 		}
/******/ 		// Create a new module (and put it into the cache)
/******/ 		var module = __webpack_module_cache__[moduleId] = {
/******/ 			// no module.id needed
/******/ 			// no module.loaded needed
/******/ 			exports: {}
/******/ 		};
/******/ 	
/******/ 		// Execute the module function
/******/ 		__webpack_modules__[moduleId](module, module.exports, __webpack_require__);
/******/ 	
/******/ 		// Return the exports of the module
/******/ 		return module.exports;
/******/ 	}
/******/ 	
/************************************************************************/
/******/ 	/* webpack/runtime/define property getters */
/******/ 	(() => {
/******/ 		// define getter functions for harmony exports
/******/ 		__webpack_require__.d = (exports, definition) => {
/******/ 			for(var key in definition) {
/******/ 				if(__webpack_require__.o(definition, key) && !__webpack_require__.o(exports, key)) {
/******/ 					Object.defineProperty(exports, key, { enumerable: true, get: definition[key] });
/******/ 				}
/******/ 			}
/******/ 		};
/******/ 	})();
/******/ 	
/******/ 	/* webpack/runtime/hasOwnProperty shorthand */
/******/ 	(() => {
/******/ 		__webpack_require__.o = (obj, prop) => (Object.prototype.hasOwnProperty.call(obj, prop))
/******/ 	})();
/******/ 	
/******/ 	/* webpack/runtime/make namespace object */
/******/ 	(() => {
/******/ 		// define __esModule on exports
/******/ 		__webpack_require__.r = (exports) => {
/******/ 			if(typeof Symbol !== 'undefined' && Symbol.toStringTag) {
/******/ 				Object.defineProperty(exports, Symbol.toStringTag, { value: 'Module' });
/******/ 			}
/******/ 			Object.defineProperty(exports, '__esModule', { value: true });
/******/ 		};
/******/ 	})();
/******/ 	
/************************************************************************/
var __webpack_exports__ = {};
// This entry need to be wrapped in an IIFE because it need to be isolated against other modules in the chunk.
(() => {
/*!******************!*\
  !*** ./index.js ***!
  \******************/
__webpack_require__.r(__webpack_exports__);
/* harmony import */ var _js_modules_components_navtoggle__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! ./js_modules/components/navtoggle */ "./js_modules/components/navtoggle.js");
/* harmony import */ var _js_modules_components_history__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! ./js_modules/components/history */ "./js_modules/components/history.js");
/* harmony import */ var _js_modules_components_detailPage__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! ./js_modules/components/detailPage */ "./js_modules/components/detailPage.js");





// creation de l'array

//losque .hello est trouvé dans la page, la c
const components = [

    {
        class:_js_modules_components_navtoggle__WEBPACK_IMPORTED_MODULE_0__.default,
        selector:"#toggle-bar",
        option:{
            save:false
        }
    },

    {
        class:_js_modules_components_history__WEBPACK_IMPORTED_MODULE_1__.default,
        selector:"#back"
    },
    {
        class:_js_modules_components_detailPage__WEBPACK_IMPORTED_MODULE_2__.default,
        selector:"#numberOfComment"
    }

]


components.forEach(component=>{
    if(document.querySelector(component.selector) !== null){
        document.querySelectorAll(component.selector).forEach(
            element=> new component.class(element, component.options))
    }
})
})();

/******/ })()
;
//# sourceMappingURL=app.js.map