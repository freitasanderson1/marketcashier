$('.btn-submit-product').on('click', function(){
        var id = $('#idProduto').val()
        var url = `api/dados_produtos/${id}`

        var data = {
            'id' : id,
            'nome' : $('#nomeProduto').val(),
            'codigo': $('#codigoProduto').val(),
            'unidadePeso': $('#tipoProduto').is(':checked'),
            'estoque' : $('#estoqueProduto').val(),
            'preco' : $('#precoProduto').val(),
        }
        // console.log(url, data)

        APIupdateProduto(url, data)
    })
function APIupdateProduto(url,data) {
    var csrftoken = jQuery("[name=csrfmiddlewaretoken]").val();

    var response = $.ajax({
        url: url,
        type: 'put',
        data: data,
        dataType: "json",
        accept: "application/json",
        beforeSend: function (xhr, settings) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        },
        success: function (dados) {
            // console.log(dados)
            insertMensagem(dados)
        },
        error: function (retorno) {
            console.log(retorno)
        },

    })
}

function insertMensagem(dados, alertType = 'success'){
    $('#listProdutosMensagem').empty()
    
    $('#listProdutosMensagem').prepend(`
        
        <li class="messages">
                
            <div class="alert alert-${alertType} alert-dismissible fade show pt-3">
                <span style="">
                    ${dados.mensagem}
                </span>
                <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
            </div>
            
        </li>
    `);
    $('#modalEditProduct .btn-close').click()
    $('#modalCreateProduct .btn-close').click()

    chamarApiproduto()

}