const sliderImgs = ["img11.jpg", "img22.jpg", "img33.jpg", "img44.jpg", "img55.jpg", "img66.jpg"];
let sliderImage = document.querySelector('.background-image');
let sliderGrids = [...document.querySelectorAll('.grid-item')];

let currentImage = 0;

setInterval(() => {
    changeSliderImage();
}, 5000);

const changeSliderImage = () => {
    sliderGrids.map((gridItem, index) => {
        setTimeout(() => {
            gridItem.classList.remove('hide');

            setTimeout(() => {

                if(index == sliderGrids.length - 1){
                    if(currentImage >= sliderImgs.length - 1){
                        currentImage = 0;
                    } else{
                        currentImage++;
                    }

                    sliderImage.src = `img/${sliderImgs[currentImage]}`;

                    sliderGrids.map((item, i) => {
                        setTimeout(() => {
                            item.classList.add('hide')
                        }, i * 100);
                    })

                }

            }, 100);

        }, index * 100);
    })
}

const navbar = document.querySelector('.navbar');

window.addEventListener('scroll', () => {
    if(scrollY >= 188){
        navbar.classList.add('bg');
    } else{
        navbar.classList.remove('bg')
    }
})