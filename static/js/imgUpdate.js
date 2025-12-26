let image = document.querySelector('.update')
let src = image.getAttribute('src');
let allImages = ['hero.avif', 'hero2.jpg', 'hero3.jpg']


    // src = `/static/images/logo/${img}`
    // console.log(src)
let count = 0
setInterval(() =>{
    if (count === allImages.length){
        count = 0
    }
    let img = allImages[count]
    let newSrc = `/static/images/logo/${img}`
    image.setAttribute('src', newSrc)
    
    count += 1
},3000)









// function clock(){
//     let currentTime = new Date()
//     console.log(currentTime.toLocaleTimeString())
// }

// setInterval(clock, 1000)