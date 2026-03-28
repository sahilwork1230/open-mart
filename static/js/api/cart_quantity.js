increment = document.getElementById("inc");
decrement = document.getElementById("dec");

function updateCart(itemId, action){
    fetch('/cart/update/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
            'X-CSRFToken': getCSRFToken()
        },
        body: `item_id=${itemId}&action=${action}`
    })
    .then(res => res.json())
    .then(data => {

        if (data.deleted) {
            document.getElementById(`cart-item-${itemId}`).remove();
            document.getElementById('total').innerText = `Total: ₹${data.total}`;
            document.getElementById("total-amount").innerText = data.total;
            return;
        }
        document.getElementById(`qty-${itemId}`).innerText = data.quantity;
        document.getElementById(`${itemId}`).innerText = `₹${data.subtotal}`;
        document.getElementById('total').innerText = `Total: ₹${data.total}`;
        document.getElementById("total-amount").innerText = `₹${data.total}`;
    })
}
function getCSRFToken() {
    return document.cookie
        .split('; ')
        .find(row => row.startsWith('csrftoken'))
        .split('=')[1];
}