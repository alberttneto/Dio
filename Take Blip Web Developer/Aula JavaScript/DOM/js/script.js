
function modificaEstilo(){

    if(h2.textContent.includes('Light')){
        body.style.backgroundColor = 'black';
        footer.classList.add('dark-mode');
        footer.classList.remove('light-mode');
        footer.classList.add('dark-mode');
        footer.classList.remove('light-mode');
        h2.textContent = 'Dark Mode ON';
        h2.style.color = 'white';
        botao.innerHTML = "Dark-Mode"
    }else{
        body.style.backgroundColor = 'rgb(199, 194, 194)';
        botao.classList.add('light-mode');
        botao.classList.remove('dark-mode');
        footer.classList.add('light-mode');
        footer.classList.remove('dark-mode');
        h2.textContent = 'Light Mode ON';
        h2.style.color = 'black';
        botao.innerHTML = "Light-Mode"
    }
}

const botao = document.getElementsByTagName('button')[0];
const h2 = document.getElementsByTagName('h2')[0];
const body = document.getElementsByTagName('body')[0];
const footer = document.getElementsByTagName('footer')[0];

botao.addEventListener('click', modificaEstilo);