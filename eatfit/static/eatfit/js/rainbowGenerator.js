document.addEventListener('DOMContentLoaded',  () =>{
        const elements = document.getElementsByClassName('title')

            function changeWord() {
                for (let i = 0; i < elements.length; i++) {
                    changeColor(elements[i]);
                }
            }

        setInterval(changeWord,500)
    })

    function random(){
        return Math.floor((Math.random() * 100) + 1);
    }

    function changeColor(element) {
        const text = element.innerText;
        element.innerHTML = "";
        for (let i = 0; i < text.length; i++) {
            let charElem = document.createElement("span");
            charElem.style.color = "hsl(" + (360 * random() / text.length) + ",80%,50%)";
            charElem.innerHTML = text[i];
            element.appendChild(charElem);
        }



    }