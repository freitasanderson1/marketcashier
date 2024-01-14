$('.nav-link').on('click', function(){

    var target = $(this).attr('href')
    
    $('.nav-link, .active').removeClass('active')

    $('.active, .inside-tab, .show').removeClass('active show')

    $(this).addClass('active')

    $(`${target}`).addClass('active show')
    if (target != '#pdv'){
        $(`${target}`).parent().parent().parent().addClass('active show')
    }
    
    // console.log(target)

    if (target == '#pdv'){
        CriarNovaVenda()
    }
})

$('.btn-remover-item-venda').on('click',function(){
    // console.log('remover item habilitado')
    $('.item-venda-option').toggleClass('d-none')
})

function CriarNovaVenda(){
    var csrftoken = jQuery("[name=csrfmiddlewaretoken]").val();

    var vendedor = $('#vendedorId').val()

    var data = {
        "valor": '0.00',
        "finalizado": false,
        "pago": false,
        "ativo": true,
        "cliente": null,
        "vendedor": vendedor
    }

    var response = $.ajax({
        url: 'api/dados_vendas',
        type: 'post',
        data: data,
        dataType: "json",
        accept: "application/json",
        beforeSend: function (xhr, settings) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        },
        success: function (dados) {
            // console.log(dados)

            $('#IdVenda').val(dados.id)
        },
        error: function (retorno) {
            console.log(retorno)
        },

    })

}