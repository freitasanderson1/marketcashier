$('.btn-submit-product').on('click', function(){
        var id = $('#idProduto').val()
        var url = `api/dados_produtos/${id}`

        var data = {
            'id' : id,
            'nome' : $('#nomeProduto').val(),
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

function insertMensagem(dados){
    $('#listProdutos').parent().prepend(`
        
        <ul class="messages pt-3">
                
            <div class="alert alert-success alert-dismissible fade show">
                <span style="">
                    ${dados.mensagem}
                </span>
                <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
            </div>
            
        </ul>
    `);
    $('#modalEditProduct .btn-close').click()
    $('#modalCreateProduct .btn-close').click()

    chamarApiproduto()

}