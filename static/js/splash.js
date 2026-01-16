gsap.to(".ball", {
  x: 350,
  duration: 3,
  repeat: -1,
  ease: "linear"
});

gsap.to(".ball",{
    y:-25,
    duration: .2,
    repeat: -1,
    yoyo: true,
    ease: "power1.out"
});

setTimeout(()=>{
    window.location.href = "/welcome";
},2000);