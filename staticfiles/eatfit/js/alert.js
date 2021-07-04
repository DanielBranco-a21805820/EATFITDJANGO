document.addEventListener('DOMContentLoaded', function () {
            document.querySelector('form').onsubmit = function() {
                let name = document.querySelector('#fname').value;
                alert(`Obrigado por te juntares ${name}!`);
            }
        });