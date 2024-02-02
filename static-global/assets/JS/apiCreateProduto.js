$('#tipoNovoProduto').on('change', function(){
    var selected = $(this).is(':checked')
    // console.log(selected)

    if(selected){
        $('#estoqueNovoProduto').attr('step','1')
    }
    else{
        $('#estoqueNovoProduto').attr('step','0.01')
    }
})

$('#codigoNovoProduto').keypress(function(event){
    var code = event.keyCode || event.which;

    if(code == 13){
        var codigo = $(this).val()
        
        // console.log(codigo)
        
        chamarApiNomeProduto(codigo)
    }
})

async function chamarApiNomeProduto(codigo){
    $('#nomeNovoProduto').empty()

    let response = await fetch(`product/${codigo}`);
    let data = await response.json();

    insertNomeProduto(data)
}

function insertNomeProduto(data){
    $('#nomeNovoProduto').val(data.name)
}

$('.btn-submit-new-product').on('click', function(){
    var url = `api/dados_produtos`

    var data = {
        'nome' : $('#nomeNovoProduto').val(),
        'codigo' : $('#codigoNovoProduto').val(),
        'unidadePeso': $('#tipoNovoProduto').is(':checked'),
        'estoque' : $('#estoqueNovoProduto').val(),
        'preco' : $('#precoNovoProduto').val(),
        'ativo': true,
    }
    // console.log(url, data)

    APIcreateProduto(url, data)
})

function APIcreateProduto(url,data) {
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

            $('#nomeNovoProduto').val(''),
            $('#codigoNovoProduto').val(''),
            $('#estoqueNovoProduto').val(''),
            $('#precoNovoProduto').val(''),

            insertMensagem(dados)
        },
        error: function (retorno) {
            // console.log(retorno.responseJSON)
            insertMensagem(retorno.responseJSON, 'danger')

        },

    })
}