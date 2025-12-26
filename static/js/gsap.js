gsap.to("#move", {
    x:30,
    duration:1,
})

gsap.to("#move1", {
    x:30,
    duration:1,
})
gsap.from("#move1", {
    x:30,
    y:30,
    duration:1,
})

let tl = gsap.timeline()
tl.from("li",{
    y:-20,
    duration:0.4,
    stagger:0.1
})