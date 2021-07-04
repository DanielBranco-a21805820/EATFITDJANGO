
document.addEventListener('DOMContentLoaded', function () {

    document.querySelector('h4').addEventListener("mouseout",function (event) {
        document.querySelector('h4').innerHTML = "Adeus!"
        document.querySelector('h4').onmouseover.style.color = "red"
    })


    document.querySelector('h4').addEventListener("mouseover",function (event) {
        document.querySelector('h4').innerHTML = "Obrigado por ter visitado a nossa página!"
        document.querySelector('h4').style.color = "gold"
        document.querySelector('h4').style.fontWeight = "bold"
    })

})