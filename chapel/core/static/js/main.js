
Vue.use(VueAwesomeSwiper)

new Vue({
    el: '#virtual-candle',
    delimiters: ['[[', ']]'],
    data: {
        litCandle: false,
        success: false,
        helloVue: 'Hello from Vue',
        swiperOptions: {
            navigation: {
                nextEl: '.swiper-button-next',
                prevEl: '.swiper-button-prev'
            },
            scrollbar: {
                el: '.swiper-scrollbar',
                hide: true
            },
            spaceBetween: 30,
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
    },
    methods: {
        hello() {
            location.reload();
        },
        submitPrayerForm(event) {
            event.preventDefault();
            form = event.target;
            form.submit();
            this.success = true;
            this.litCandle = false;
        },
        lightCandle() {
            this.litCandle = true;
        },
    }
});