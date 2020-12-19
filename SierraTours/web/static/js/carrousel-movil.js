var imagenes = ['img/creel1.jpg','img/creelbaner.jpg','img/huapocabaner.jpg'];
var direcciones = ['barrancas.html','creel.html','huapoca.html'];
cont = 0;
conturl = 0;
function carrousel(contenedor){
    contenedor.addEventListener('click', e => {
         let atras = contenedor.querySelector('.atras'),
           adelante = contenedor.querySelector('.adelante'),
           img= contenedor.querySelector('.change'),
           url= contenedor.querySelector('.redireccion'),
           tgt = e.target;

           if(tgt == atras){
                if(cont > 0){
                    img.src = imagenes[cont - 1];
                    url.href = direcciones[conturl -1];
                    cont--;
                    conturl--;
                }else{
                    img.src = imagenes[imagenes.length - 1];
                    url.href = direcciones[direcciones.length -1];
                    conturl = direcciones.length-1;
                    cont = imagenes.length-1;
                }   
           }else if(tgt == adelante){
                if(cont < imagenes.length -1){
                    url.href = direcciones[conturl + 1];
                    img.src = imagenes[cont + 1];
                    cont++;
                    conturl++;
                }else{
                    url.href = direcciones[0];
                    img.src = imagenes[0];
                    conturl = 0;
                    cont = 0;
                }
           }

    });
}

document.addEventListener("DOMContentLoaded", () =>{
    
    let contenedor = document.querySelector(".paquetes-movil");
    carrousel(contenedor);

});