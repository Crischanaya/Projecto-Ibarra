function enviarFormulario(){
    event.preventDefault();

if(document.querySelector('.msj-verificacion').textContent == "Tu contraseña al menos debe contener 8 digitos" || 
    document.querySelector('.msj-verificacion').textContent == "Ingresa tambien letras mayusculas y minusculas" || 
    document.querySelector('.msj-verificacion').textContent == "La contraseña es pobre ingresa numeros y simbolos para complementarla")
    {
    Swal.fire({
    icon: 'error',
    title: 'La contraseña es insegura',
    text: document.querySelector('.msj-verificacion').textContent
    })
}
else{ 
    document.form_registro.submit();  
}

return false;

}



var password = document.getElementById('contrasenna');
var mensaje = document.querySelector('.msj-verificacion');
var cambiarError = document.querySelector('.formulario__input-error');
password.addEventListener('keyup', (e) =>{
     var valorinput = e.target.value;
    

    if(validar_clave(valorinput) != "ocho_digitos"){

        if(validar_clave(valorinput) == true){
            mensaje.classList.add('msj-verificacion');
            mensaje.innerHTML="Tu contraseña es segura";
            mensaje.classList.add('msj-verificacion-activo');
            
        }else{
           if(validar_clave(valorinput) == "mayuscula" || validar_clave(valorinput) == "minuscula"){
               mensaje.classList.remove('msj-verificacion');
              cambiarError.innerHTML="Ingresa tambien letras mayusculas y minusculas";	
              cambiarError.classList.add('formulario__input-error-activo');
           }/*
           if(validar_clave(valorinput) == "minuscula"){
              mensaje.innerHTML="Ingresa tambien Minusculas";
              $('.msj-verificacion').css("color","darkorange");
           }*/
           if(validar_clave(valorinput) == "numero" || validar_clave(valorinput) == "caracter_raro"){
                mensaje.classList.remove('msj-verificacion');
              cambiarError.innerHTML="La contraseña es pobre ingresa numeros y simbolos para complementarla";
             // $('.msj-verificacion').css("color","darkorange");
             cambiarError.classList.add('formulario__input-error-activo');
           }
          /* if(validar_clave(valorinput) == "caracter_raro"){
              mensaje.innerHTML="Ingresa tambien simbolos";
           }*/
        }
    
    }
    else
    {
         mensaje.classList.remove('msj-verificacion');
           mensaje.innerHTML="Tu contraseña al menos debe contener 8 digitos";  
         cambiarError.classList.add('formulario__input-error-activo');
    }

});

function validar_clave(contrasenna)
{
    if(contrasenna.length >= 8)
    {		
        var mayuscula = false;
        var minuscula = false;
        var numero = false;
        var caracter_raro = false;
        
        for(var i = 0;i<contrasenna.length;i++)
        {
            if(contrasenna.charCodeAt(i) >= 65 && contrasenna.charCodeAt(i) <= 90)
            {
                mayuscula = true;
            }
            else if(contrasenna.charCodeAt(i) >= 97 && contrasenna.charCodeAt(i) <= 122)
            {
                minuscula = true;
            }
            else if(contrasenna.charCodeAt(i) >= 48 && contrasenna.charCodeAt(i) <= 57)
            {
                numero = true;
            }
            else
            {
                caracter_raro = true;
            }
        }
          if(mayuscula == true && minuscula == true && caracter_raro == true && numero == true)
        {
            return true;
        }
        if(mayuscula == false){
            
            return "mayuscula";
        }
        if(minuscula == false){
            return "minuscula";
        }
        if(caracter_raro == false){
            return "caracter_raro";
        }
        if(numero == false){
            return "numero";
        }
    }
    return "ocho_digitos";
}