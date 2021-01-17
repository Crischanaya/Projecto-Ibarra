
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
    let count = quantity;
    let amount;
    if(quantity >= 0){
        if(quantity >= 2){
        quantity--; 
        amount = parseFloat(unitPrice) * (quantity * .2);
        amount = parseFloat(amount) + parseFloat(unitPrice);
      
        }
        else{  
            amount = parseFloat(unitPrice) * parseInt(quantity);
        }
    }
     amount = amount.toFixed(2);
    document.getElementById('cart-total').innerHTML = '$ ' + amount;
    document.getElementById('summary-price').innerHTML = '$ ' + unitPrice;
    console.log(count);
    if(count == 1){
       console.log(quantity);
        document.getElementById('summary-quantity').innerHTML = quantity;
    }
   else if(count == 2){ 
        console.log(count);
        document.getElementById('summary-quantity').innerHTML = count;
    }
    else{
        document.getElementById('summary-quantity').innerHTML = quantity + 1;
    }
   
    document.getElementById('summary-total').innerHTML = '$ ' + amount;
    document.getElementById('amount').value = amount;
    
   
    total.push(String(amount));

   return total;

};
document.getElementById('quantity').addEventListener('change', updatePrice);
updatePrice();

//Retrieve product description
document.getElementById('description').value = document.getElementById('product-description').innerHTML;
