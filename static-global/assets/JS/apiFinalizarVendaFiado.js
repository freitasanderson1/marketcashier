$('.btn-venda-fiado').on('click',function(){
    // console.log('remover item habilitado')
    var clienteId = $('#client-comprando-id').val()
    var vendaId = $('#IdVenda').val()

    finalizarVendaFiado(clienteId,vendaId)
    
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
            console.log(dados)
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
