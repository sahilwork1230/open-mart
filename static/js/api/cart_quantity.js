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
    .then(response => response.json())
    .then(data => {
        document.getElementById(`qty-${itemId}`).innerText = data.quantity;
    })
}
function getCSRFToken() {
    return document.cookie
        .split('; ')
        .find(row => row.startsWith('csrftoken'))
        .split('=')[1];
}