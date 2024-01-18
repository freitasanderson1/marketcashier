$('.btn-finalizar-venda').on('click', function(){

    var temClienteSelecionado = $('#client-comprando-id').val()

    // console.log(`Valor: ${temClienteSelecionado}`)

    if (temClienteSelecionado){
        $('.btn-venda-fiado').removeClass('d-none')
    }
})

$('.btn-venda-fiado').on('click',function(){
    // console.log('remover item habilitado')
    var clienteId = $('#client-comprando-id').val()
    var vendaId = $('#IdVenda').val()

    finalizarVendaFiado(clienteId,vendaId)
    
})

$('.btn-venda-avista-finalizada').on('click',function(){
    var clienteId = $('#client-comprando-id').val()
    
    var vendaId = $('#IdVenda').val()

    finalizarVendaAvista(clienteId, vendaId)
    
})

$('.btn-venda-avista').on('click', function(){
    var valorTotal = $('#venda-valor-total-input').val()

    // var valorNumerico = valorTotal.slice(3,valorTotal.length)

    // console.log(valorNumerico)

    $('#valor-total-compra').text(`${parseFloat(valorTotal).toFixed(2)}`)

    $('#div-troco').toggleClass('d-none')
})

$('#valor-pago-compra').on('input',  function(){
    console.log('Inserindo', parseFloat($('#valor-total-compra').text()).toFixed(2))
    
    var troco =  parseFloat($(this).val()).toFixed(2) - parseFloat($('#venda-valor-total-input').val()).toFixed(2)
    
    console.log(troco.toFixed(2))
    if (troco.toFixed(2) >= 0.00){
        $('#troco-compra').empty()
        
        $('#troco-compra').text(troco.toFixed(2))

        $('#restando-compra').empty()
        
        $('#restando-compra').text('0,00')

        $('.btn-venda-avista-finalizada').removeClass('d-none')
    }
    else{
        
        $('#restando-compra').empty()
        
        $('#restando-compra').text(troco.toFixed(2))

        $('#troco-compra').empty()
        
        $('#troco-compra').text('0,00')

        $('.btn-venda-avista-finalizada').addClass('d-none')

    }

})

async function finalizarVendaFiado(cliente,venda){

    var csrftoken = jQuery("[name=csrfmiddlewaretoken]").val();

    var data = {
            "cliente": cliente,
            "finalizado": true,
        }

    var response = $.ajax({
        url: `api/dados_vendas/${venda}`,
        type: 'put',
        data: data,
        dataType: "json",
        accept: "application/json",
        beforeSend: function (xhr, settings) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        },
        success: function (dados) {
            // console.log(dados)
            insertMensagemFinalizar(dados.mensagem)

        },
        error: function (retorno) {
            console.log(retorno)
        },

    })
}

async function finalizarVendaAvista(cliente, venda){

    var csrftoken = jQuery("[name=csrfmiddlewaretoken]").val();

    var data = {
            "cliente": cliente,
            "pago": true,
        }

    var response = $.ajax({
        url: `api/dados_vendas/${venda}`,
        type: 'put',
        data: data,
        dataType: "json",
        accept: "application/json",
        beforeSend: function (xhr, settings) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        },
        success: function (dados) {
            // console.log(dados)
            insertMensagemFinalizar(dados.mensagem)

        },
        error: function (retorno) {
            console.log(retorno)
        },

    })
}

async function insertMensagemFinalizar(mensagem){
    $('.retorno-finalizar-venda').empty()
    $('.retorno-finalizar-venda').append(`

        <div class="alert mb-0 alert-success alert-dismissible fade show">
            <span style="">
                ${mensagem}
            </span>

            <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
        </div>

    `)

    $('.btn-reload-pag').removeClass('d-none')

}
