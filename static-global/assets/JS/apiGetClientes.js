$('#listarClientes').on('click', function(){
    $('#termoListCliente').val('')
    chamarApiCliente('')
});

$( document ).ready(function() {
    chamarApiCliente('')
});
$('#termoListCliente').on('input', function(){
    var termo = $(this).val()
  
    // console.log(termo.length,termo)
  
    if (termo.length > 3){
      chamarApiCliente(termo)
    }
})

$("input:radio[name='tipoPagamentoConta']").on('click',function(){

    // console.log($('input[name=tipoPagamentoConta]:checked').val())

    $('#tipoPagamentoContaSelecionado').val($('input[name=tipoPagamentoConta]:checked').val())

    if($("input:radio[name='tipoPagamentoConta']").is(":checked")) {
        $('.abater-conta-cliente-div').removeClass('d-none')
    }

})

async function chamarApiCliente(termo){
    if (termo){
        var response = await fetch(`api/dados_clientes/${termo}`);
    }
    else{
        var response = await fetch(`api/dados_clientes`);   
    }
    let data = await response.json();

    // console.log(`Index: ${Object.getOwnPropertyNames(data)}`);
    // console.log(`Dados: ${data.clientes}`)
    
    termo ? insertClientes(data.clientes) : insertClientes(data)
}

function insertClientes(data){

    $('#listClientes').empty()

    data.forEach(element => {

        $('#listClientes').append(`
            <li class="card p-1 mb-1 shadow">
                <div>
                    
                    <h6 class="text-success"> 
                        ${element.nomeCompleto}
                    </h6>

                    <div class="row">
                        <div class="col">
                            <b>CPF:</b> <span class="text-success">${element.cpf}</span>
                        </div>

                        <div class="col">
                            <b>Celular:</b> <span class="text-success">${element.celular}</span>
                        </div>

                        <div class="col">
                            <b>Endereço:</b> <span class="text-success">${element.endereco}</span>
                        </div>
                        <div class="col-2 d-flex justify-content-end">
                            <button type="button" class="btn btn-success btn-cliente-conta p-2" 
                                data-ms-id="${element.id}" 
                                data-ms-cpf="${element.cpf}" 
                                data-bs-toggle="modal" 
                                data-bs-target="#modalContaCliente">
                                <i class="fa-solid fa-circle-dollar-to-slot"></i>
                                Conta
                            </button>
                        </div>
                    </div>
                </div>
            </li>
        `)

    });

    $('.btn-cliente-conta').on('click', function(){
                
        var cpf = $(this).data('ms-cpf')

        // console.log(`CPF do cliente: ${cpf}`)

        chamarApiClienteConta(cpf)
    })
}

async function chamarApiClienteConta(cpf){
    
    var response = await fetch(`cliente/${cpf}`);

    let data = await response.json();

    var valor = data.debito.toFixed(2)

    $('#contaClienteNome').empty().text(data.nome)
    $('#contaClienteCpf').val(data.cpf)

    $('#contaClienteDebito').val(`R$ ${valor}`)
    // $('#contaClienteDebitoAvista').val(`R$ ${valorAvista}`)

    // console.log(`Index: ${Object.getOwnPropertyNames(data.vendas)}`);
    // console.log(`Dados: ${data.vendas}`)

    $('#contaClienteCompras ').empty()

    data.vendas.forEach(venda => {
        $('#contaClienteCompras ').append(`
            <li class="card p-1 mb-1 shadow text-success">
                ${venda.info}
            </li>
        `)
        
    });

    $('.btn-mostra-abater-valor').on('click', function(){
        $('.contaClienteAbaterValor').toggleClass('d-none')
    })

    $('.btn-abater-valor').on('click', function(){
        var valor = $('#valorAbaterConta').val()

        var pagamentoSelecionado = $('#tipoPagamentoContaSelecionado').val()

        if (valor){

            console.log(valor)

            var data = {
                'valor': valor,
                'tipo': pagamentoSelecionado
            }
            var csrftoken = jQuery("[name=csrfmiddlewaretoken]").val();
            
            var response = $.ajax({
                url: `cliente/${cpf}`,
                type: 'post',
                data: data,
                dataType: "json",
                accept: "application/json",
                beforeSend: function (xhr, settings) {
                    xhr.setRequestHeader("X-CSRFToken", csrftoken);
                },
                success: function (dados) {
                    controlPagarConta(dados)
                    console.log(dados)

                },
                error: function (retorno) {
                    console.log(retorno)
                },
                
            })
        }
    })

   
}


function controlPagarConta(dados){
    $('.btn-mostra-abater-valor').addClass('d-none')
    $('.contaClienteAbaterValor').empty()

    $('.retorno-pagar-conta').empty()
    $('.retorno-pagar-conta').append(`

        <div class="alert mb-0 alert-success alert-dismissible fade show">
            <span style="">
                Foi abatido da conta um total de R$ ${dados.pago.toFixed(2)}. Resta um total de R$ ${dados.resta.toFixed(2)}.'     
            </span>

            <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
        </div>

    `)
    $('.contaClienteDebito').val(`R$ ${dados.resta.toFixed(2)}`)
    $('#finish-pay-conta').removeClass('d-none')

}