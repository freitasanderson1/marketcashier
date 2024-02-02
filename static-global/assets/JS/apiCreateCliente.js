$('.btn-submit-new-cliente').on('click', function(){
    var url = `api/dados_clientes`

    var data = {
        'nomeCompleto' : $('#nomeNovoCliente').val(),
        'cpf' : $('#cpfNovoCliente').val(),
        'celular' : $('#telefone_id').val(),
        'endereco' : $('#enderecoNovoCliente').val(),
        'dataNascimento' : $('#data_id').val(),
        'ativo': true,
    }
    // console.log(url, data)

    APIcreateCliente(url, data)
})

function APIcreateCliente(url,data) {
    var csrftoken = jQuery("[name=csrfmiddlewaretoken]").val();

    var response = $.ajax({
        url: url,
        type: 'post',
        data: data,
        dataType: "json",
        accept: "application/json",
        beforeSend: function (xhr, settings) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        },
        success: function (dados) {
            // console.log(dados)

            $('#nomeNovoCliente').val(''),
            $('#cpfNovoCliente').val(''),
            $('#enderecoNovoCliente').val(''),
            $('#data_id').val(''),
            $('#telefone_id').val('')

            insertMensagemCliente(dados)
        },
        error: function (retorno) {
            insertMensagemCliente(retorno.responseJSON, 'warning',retorno.responseJSON.mensagem)
        },

    })
}

function insertMensagemCliente(dados, alertType='success', mensagem='Cliente Cadastrado!'){
    $('#listClientes').parent().prepend(`
        
        <ul class="messages pt-3">
                
            <div class="alert alert-${alertType} alert-dismissible fade show">
                <span style="">
                    ${mensagem}
                </span>
                <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
            </div>
            
        </ul>
    `);
    $('#modalCreateCliente .btn-close').click()

    chamarApiCliente()

}