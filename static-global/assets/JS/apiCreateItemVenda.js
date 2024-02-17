$('#produto-codigo').keypress(function(event){
    var code = event.keyCode || event.which;

    if(code == 13){
        var codigo = $(this).val()
        
        // console.log(codigo)
        
        chamarApiItemVenda(codigo)
    }
})


async function chamarApiItemVenda(codigo){

    let response = await fetch(`api/dados_produtos/${codigo}`);
    let data = await response.json();

    // console.log(`Resposta: ${data[1].quantidade}`)
    insertItemVenda(data[0], data[1] ? data[1].quantidade: $('#produto-quantidade').val())

    $('#produto-nome').empty()
    $('#produto-nome').text(data[0].nome)

    $('#produto-codigo').val('')
    $('#produto-quantidade').val('1')
}

async function insertItemVenda(produto,quantidade){

    var csrftoken = jQuery("[name=csrfmiddlewaretoken]").val();

    var venda = $('#IdVenda').val()

    var valorTotal = produto.preco * quantidade

    var data = {
            "produto": produto.id,
            "quantidade": quantidade,
            "valorTotal": valorTotal,
            "ativo": true,
            "venda": venda
        }

    var response = $.ajax({
        url: 'api/dados_item_venda',
        type: 'post',
        data: data,
        dataType: "json",
        accept: "application/json",
        beforeSend: function (xhr, settings) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        },
        success: function (dados) {
            // console.log(dados)
            insertItemVendaLista(dados)

        },
        error: function (retorno) {
            console.log(retorno)
        },

    })
}

async function removeItemVenda(produto){

    var csrftoken = jQuery("[name=csrfmiddlewaretoken]").val();

    var data = {
            "produto": produto,
            "ativo": false
        }

    var response = $.ajax({
        url: `api/dados_item_venda/${produto}`,
        type: 'put',
        data: data,
        dataType: "json",
        accept: "application/json",
        beforeSend: function (xhr, settings) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        },
        success: function (dados) {
            // console.log(dados)
            insertItemVendaLista(dados)

        },
        error: function (retorno) {
            console.log(retorno)
        },

    })
}

async function insertItemVendaLista(data){

    $('#listItemVenda').empty()

    let response = await fetch(`api/dados_item_venda/${data.venda}`);
    let dados = await response.json();
    
    $('#venda-valor-total').empty();
    $('#venda-valor-total').text(`${dados.valor.toLocaleString('pt-BR', { style: 'currency', currency: 'BRL' })}`);
    $('#venda-valor-total-input').val(`${dados.valor}`);
    

    dados.itens.forEach(element => {
        if(element.produto.unidadePeso){
            var unidadePeso = 'Unidades'
        }
        else{
            var unidadePeso = 'KGs'
        }
        $('#produto-valor-unitario').empty();
        $('#produto-valor-unitario').text(`${element.produto.preco.toLocaleString('pt-BR', { style: 'currency', currency: 'BRL' })}`);

        $('#produto-valor-total-item').empty();
        $('#produto-valor-total-item').text(`${element.valorTotal.toLocaleString('pt-BR', { style: 'currency', currency: 'BRL' })}`)

        if(element.ativo){
            $('#listItemVenda').prepend(`
                <li class="card p-2 mb-1 shadow">
                    <div class="row">
                        <div class="col"> 
                            <b class="text-success">${element.produto.nome}</b>
                        </div>
                        <div class="col">
                            <b>Código:</b> <span class="text-success">${element.produto.codigo}</span>
                        </div>
                        <div class="col">
                            <b>Quantidade:</b> <span class="text-success">${element.quantidade} ${unidadePeso}</span>
                        </div>

                        <div class="col">
                            <b>Preço Unitário:</b> <span class="text-success">${element.produto.preco.toLocaleString('pt-BR', { style: 'currency', currency: 'BRL' })}</span>
                        </div>
                        <div class="col">
                            <b>Preço Total:</b> <span class="text-success">${element.valorTotal.toLocaleString('pt-BR', { style: 'currency', currency: 'BRL' })}</span>
                        </div>
                        <div class="item-venda-option item-venda-remove d-none col-1 d-flex align-items-center justify-content-around" data-item="${element.id}" style="cursor: pointer;">   
                            <i class="fa-solid fa-square-minus text-danger"></i>
                        </div>
                    </div>
                </li>
            `)
        }        
    });
}