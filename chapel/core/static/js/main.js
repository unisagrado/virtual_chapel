const CAROUSEL_CONFIG = {
    loop: false,
    navigation: {
        nextEl: '.swiper-button-next',
        prevEl: '.swiper-button-prev'
    },
    scrollbar: {
        el: '.swiper-scrollbar',
        hide: true
    },
    autoplay: {
        delay: 2500,
        disableOnInteraction: false
    },
    grabCursor: true,
    spaceBetween: 30,
    loopFillGroupWithBlank: true,
    breakpoints: {
        1100: {
            slidesPerView: 3,
            slidesPerGroup: 3,
        },
        900: {
            slidesPerView: 2,
            slidesPerGroup: 2,
        },
        700: {
            slidesPerView: 1,
            slidesPerGroup: 1,
        }
    }
}


Vue.use(VueAwesomeSwiper)

new Vue({
    el: '#virtual-candle',
    delimiters: ['[[', ']]'],
    data: {
        litCandle: false,
        swiperOptions: CAROUSEL_CONFIG
    },
    watch: {
        litCandle: function (newVal) {
            if (newVal) {
                return localStorage.setItem('@Unisagrado:VirtualChapel:lit_candle', newVal);
            }
            return localStorage.removeItem('@Unisagrado:VirtualChapel:lit_candle');
        }
    },
    mounted() {
        if (localStorage.getItem('@Unisagrado:VirtualChapel:lit_candle')) {
            this.litCandle = Boolean(localStorage.getItem('@Unisagrado:VirtualChapel:lit_candle'));
        }
    },
    methods: {
        blowOutCandle() {
            this.litCandle = false;
        },
        lightCandle() {
            this.litCandle = true;
        },
    }
});