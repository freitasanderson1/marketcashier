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
    var valorOriginal = $('#venda-valor-original').val()

    finalizarVendaFiado(clienteId,vendaId,valorOriginal)
    
})

$('.btn-venda-avista-finalizada').on('click',function(){
    var clienteId = $('#client-comprando-id').val()
    
    var vendaId = $('#IdVenda').val()

    finalizarVendaAvista(clienteId, vendaId)
    
})

$('.btn-venda-avista-finalizada-parcialmente').on('click',function(){
    var clienteId = $('#client-comprando-id').val()
    
    var vendaId = $('#IdVenda').val()
    var valor = $('#valor-pago-compra').val()

    finalizarVendaParcialmente(clienteId, vendaId,valor)
    
})

$('.btn-venda-avista').on('click', function(){

    var valorTotal = $('#venda-valor-total-input').val()
    var valorDesconto = $('#venda-valor-desconto-input').val()

    // var valorNumerico = valorTotal.slice(3,valorTotal.length)

    // console.log(valorNumerico)

    $('#valor-total-compra').text(`${parseFloat(valorTotal).toFixed(2)}`)
    $('#valor-desconto-compra').text(`${parseFloat(valorDesconto).toFixed(2)}`)

})

$("input:radio[name='tipoPagamento']").on('click',function(){
    var tipo = $('input[name=tipoPagamento]:checked').val()

    // console.log(tipo)
    
    var valorTotal = $('#venda-valor-total-input').val()
    var desconto = $('#venda-valor-desconto-input').val()

    $('#valor-total-compra').empty().text(`${parseFloat(valorTotal-desconto).toFixed(2)}`)
    $('#valor-desconto-compra').empty().text(`${parseFloat(desconto).toFixed(2)}`)

    // switch (tipo){
    //     case '1':
    //         $('#valor-total-compra').empty().text(`${parseFloat(valorTotal-desconto).toFixed(2)}`)
    //         $('#valor-desconto-compra').empty().text(`${parseFloat(desconto).toFixed(2)}`)
    //         break;
    //     case '2':
    //         $('#valor-total-compra').empty().text(`${parseFloat(valorTotal-desconto).toFixed(2)}`)
    //         $('#valor-desconto-compra').empty().text(`${parseFloat(desconto).toFixed(2)}`)
    //         break;
    //     case '3':
    //         $('#valor-total-compra').empty().text(`${parseFloat(valorTotal).toFixed(2)}`)
    //         $('#valor-desconto-compra').empty().text(`0.00`)
    //         break;
    //     case '4':
    //         $('#valor-total-compra').empty().text(`${parseFloat(valorTotal).toFixed(2)}`)
    //         $('#valor-desconto-compra').empty().text(`0.00`)
    //         break;
    // }

    // console.log(valorTotal,desconto)

    $('#tipoPagamentoSelecionado').val($('input[name=tipoPagamento]:checked').val())

    if($("input:radio[name='tipoPagamento']").is(":checked")) {
        $('.func-pagar').removeClass('d-none')
    }
})

$('#valor-pago-compra').on('input',  function(){
    // console.log('Inserindo', parseFloat($('#valor-total-compra').text()).toFixed(2))
    var tipo = $('input[name=tipoPagamento]:checked').val()

    var valorTotal = $('#venda-valor-total-input').val()
    var desconto = $('#venda-valor-desconto-input').val()

    switch (tipo){
        case '1':
            var troco =  parseFloat($(this).val()).toFixed(2) - parseFloat(valorTotal-desconto).toFixed(2)
            break;
        case '2':
            var troco =  parseFloat($(this).val()).toFixed(2) - parseFloat(valorTotal-desconto).toFixed(2)
            break;
        case '3':
            var troco =  parseFloat($(this).val()).toFixed(2) - parseFloat(valorTotal-desconto).toFixed(2)
            break;
        case '4':
            var troco =  parseFloat($(this).val()).toFixed(2) - parseFloat(valorTotal-desconto).toFixed(2)
            break;
    }
    
    
    // console.log(troco.toFixed(2))
    var valorOriginal = $('#venda-valor-original').val()
    var descontoOriginal = $('#produto-descontos-original').val()
    var valorPago = $('#valor-pago-compra').val()

    if (troco.toFixed(2) >= 0.00 && valorPago >= (valorOriginal - descontoOriginal)){

        $('#troco-compra').empty()
        
        $('#troco-compra').text(troco.toFixed(2))

        $('#restando-compra').empty()
        
        $('#restando-compra').text('0,00')

        $('.btn-venda-avista-finalizada').removeClass('d-none')
        // $('.btn-venda-avista-finalizada-parcialmente').addClass('d-none')

        
    }
    else{
        
        $('#restando-compra').empty()
        
        $('#restando-compra').text(Math.abs(troco).toFixed(2))

        $('#troco-compra').empty()
        
        $('#troco-compra').text('0,00')

        $('.btn-venda-avista-finalizada').addClass('d-none')

        var temClienteSelecionado = $('#client-comprando-id').val()

        // console.log(`Valor: ${temClienteSelecionado}`)

        // if (temClienteSelecionado){
            $('.btn-venda-avista-finalizada-parcialmente').removeClass('d-none')
        // }

    }

})

async function finalizarVendaFiado(cliente,venda,valor){

    var csrftoken = jQuery("[name=csrfmiddlewaretoken]").val();

    var data = {
            "valorCompra": valor,
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
async function finalizarVendaParcialmente(cliente, venda, valor){
    var pagamentoSelecionado = $('#tipoPagamentoSelecionado').val()
    var valorOriginal = $('#venda-valor-original').val()

    var csrftoken = jQuery("[name=csrfmiddlewaretoken]").val();

    var data = {
            "cliente": cliente,
            "pago": false,
            "valor": valor,
            "valorCompra": valorOriginal,
            "tipo": pagamentoSelecionado,
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
            // console.log(dados.desconto, dados.pago)
            $('#venda-valor-total-input').val(dados.pago.toFixed(2))
            $('#venda-valor-desconto-input').val(dados.desconto.toFixed(2))
            insertMensagemFinalizar(dados.mensagem)

        },
        error: function (retorno) {
            console.log(retorno)
        },

    })
}

async function finalizarVendaAvista(cliente, venda){
    var pagamentoSelecionado = $('#tipoPagamentoSelecionado').val()

    var csrftoken = jQuery("[name=csrfmiddlewaretoken]").val();

    var data = {
            "cliente": cliente,
            "pago": true,
            "tipo": pagamentoSelecionado,
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
