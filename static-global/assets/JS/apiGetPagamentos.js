$('#listarPagamentosHoje').on('click', function(){ 
    chamarApiPagamentos(dataDeHoje)
});

$('#listaTodosPagamentos').on('click', function(){ 
    chamarApiPagamentos()
});

$( document ).ready(function() {
    chamarApiPagamentos(dataDeHoje)
});

async function chamarApiPagamentos(dataPagamento){
    if (dataPagamento){
        var response = await fetch(`api/dados_pagamentos/${dataPagamento}`);
    }
    else{
        var response = await fetch(`api/dados_pagamentos`);   
    }
    let data = await response.json();

    console.log(`Index: ${Object.getOwnPropertyNames(data.pagamentos)}`);
    console.log(`Dados: ${data.pagamentos}`)

    insertPagamentos(data)
}

const TIPO_PAGAMENTO = {
    '1': 'Dinheiro',
    '2': 'Pix',
    '3': 'Débito',
    '4': 'Crédito',
}

function insertPagamentos(data){
    // Somar Dinheiro

    var somaDinheiro = 0;

    for (var i = 0; i < data.pagamentos.dinheiro.length; i++) {
        somaDinheiro += data.pagamentos.dinheiro[i];
    }

    $('#total-dinheiro-recebido-hoje').empty()
    $('#total-dinheiro-recebido-hoje').text(`R$ ${somaDinheiro.toFixed(2)}`)
    //////////////////

    // Somar Pix
    var somaPix = 0;

    for (var i = 0; i < data.pagamentos.pix.length; i++) {
        somaPix += data.pagamentos.pix[i];
    }
    
    $('#total-pix-recebido-hoje').empty()
    $('#total-pix-recebido-hoje').text(`R$ ${somaPix.toFixed(2)}`)
    //////////////////

    // Somar Débito
    var somaDebito = 0;

    for (var i = 0; i < data.pagamentos.debito.length; i++) {
        somaDebito += data.pagamentos.debito[i];
    }
    
    $('#total-debito-recebido-hoje').empty()
    $('#total-debito-recebido-hoje').text(`R$ ${somaDebito.toFixed(2)}`)
    //////////////////

    // Somar Crédito
    var somaCredito = 0;

    for (var i = 0; i < data.pagamentos.credito.length; i++) {
        somaCredito += data.pagamentos.credito[i];
    }
    
    $('#total-credito-recebido-hoje').empty()
    $('#total-credito-recebido-hoje').text(`R$ ${somaCredito.toFixed(2)}`)
    //////////////////

    var totalRecebido = somaDinheiro + somaPix + somaDebito + somaCredito

    $('#total-recebido-hoje').empty()
    $('#total-recebido-hoje').text(`R$ ${totalRecebido.toFixed(2)}`)

    // Listagem de Pagamentos
    $('#listPagamentos').empty()

    data.lista.forEach(element => {

        // console.log(`Index: ${Object.getOwnPropertyNames(element)}`);
        // console.log(`Dados: ${element}`)

        $('#listPagamentos').append(`
            <li class="card p-1 mb-1 shadow">
                <div>
                    <h6 class="text-success"> 
                        ID: ${element.id} - Valor: R$ ${element.valor.toFixed(2)} Tipo: <b>${TIPO_PAGAMENTO[element.tipo]}</b> - Data do Pagamento: ${new Date(Date.parse(element.dataCadastro)).toLocaleDateString('pt-BR')}
                    </h6>
                </div>
            </li>
        `)

    });
}