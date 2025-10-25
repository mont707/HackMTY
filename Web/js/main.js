// Detecta scroll y activa clase shrink
window.addEventListener('scroll', function() {
    const header = document.querySelector('.principal_header');
    if(window.scrollY > 50){
        header.classList.add('shrink');
    } else {
        header.classList.remove('shrink');
    }
});
