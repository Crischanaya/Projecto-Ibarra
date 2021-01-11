
function cleanCardInfo() {
    document.getElementById('cardNumber').style.backgroundImage = '';
    document.getElementById('issuerInput').classList.add("hidden");
    document.getElementById('issuer').options.length = 0;
    document.getElementById('installments').options.length = 0;
}

//Handle transitions
document.getElementById('checkout-btn').addEventListener('click', function(){ 
    $('.shopping-cart').fadeOut(500);
    setTimeout(() => { $('.container_payment').show(500).fadeIn(); }, 500);
});
document.getElementById('go-back').addEventListener('click', function(){ 
    $('.container_payment').fadeOut(500);
    setTimeout(() => { $('.shopping-cart').show(500).fadeIn(); }, 500);
});

var total=[];
//Handle price update
function updatePrice(){
    let quantity = document.getElementById('quantity').value;
    let unitPrice = document.getElementById('unit-price').innerHTML;
    quantity = parseFloat(quantity);
    console.log(quantity);
    let amount;
    if(quantity >= 0){
        if(quantity > 1){
        amount = parseInt(unitPrice) * (quantity * .20);
        amount = amount + parseInt(unitPrice);
        }
        else{  
            amount = parseInt(unitPrice) * parseInt(quantity);
        }
    }
     amount = amount.toFixed(2);
    document.getElementById('cart-total').innerHTML = '$ ' + amount;
    document.getElementById('summary-price').innerHTML = '$ ' + unitPrice;
    document.getElementById('summary-quantity').innerHTML = quantity;
    document.getElementById('summary-total').innerHTML = '$ ' + amount;
    document.getElementById('amount').value = amount;
    
   
    total.push(String(amount));
   // total = total.unshift(amount);
    
   return total;

};
document.getElementById('quantity').addEventListener('change', updatePrice);
updatePrice();

//Retrieve product description
document.getElementById('description').value = document.getElementById('product-description').innerHTML;

  
/*
paypal.Buttons({
    createOrder: function(data, actions) {
      // This function sets up the details of the transaction, including the amount and line item details.
      return actions.order.create({
        purchase_units: [
          {
          description: "Paquetes",  
          amount: {
            currency_code: "MXN",
            value: amount
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
    alert(details.mensaje);

    })
  }
  }).render('#paypal-button-container');*/