/*
1 - após envio do form:
    - esconde form
    - mostra vela
    - mostra sucesso
    - mostra botão acende vela

2 - após acende vela
    - mostra imagem fogo
    - mostra mensagem vela 7 dias

3 - Clique faça sua prece (recarrega página)
    - esconde mensagem de sucesso
    - esconde vela
    - escode imagem fogo
    - esconde mensagem vela 7 dias
    - mostra form
*/

const virtualCandle = new Vue({
    el: '#virtual-candle',
    data: {
        litCandle: false,
        success: false,
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