var valor = updatePrice();
var precio_final =valor[valor.length-1];
function nose(){
   precio_final=valor[valor.length-1];
   return precio_final;
 
}
document.getElementById('quantity').addEventListener('change', nose);

if(precio_final != "undefined"){
    paypal.Buttons({
        createOrder: function(data, actions) {
          // This function sets up the details of the transaction, including the amount and line item details.
          return actions.order.create({
            purchase_units: [
              {
              description: "Paquetes",  
              amount: {
                currency_code: "MXN",
                value: precio_final
              }
            }]
          });
        },
        onApprove: function(data) {
      return fetch('/pago/', {
        method: "POST",
        headers: {
          'content-type': 'application/json',
          'X-CSRFToken': csrftoken,
        },
        body: JSON.stringify({
          orderID: data.orderID
        })
      }).then(function(res) {
        return res.json();
      }).then(function(details) {
          if(details.mensaje == "completed"){
             //window.location.href = "{% url 'login' %}";
             window.location.href ="http://127.0.0.1:8000/home/?status=completed"
            
          }
          if(details.mensaje == "Error"){
             window.location.href ="http://127.0.0.1:8000/home/?status=error" 
          } 
        //alert(details.mensaje);
    
        })
      }
      }).render('#paypal-button-container');
    }