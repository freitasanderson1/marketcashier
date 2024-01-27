const date = new Date();

let day = date.getDate();
let month = date.getMonth() + 1;
let year = date.getFullYear();

let dataDeHoje = `${day}-${month}-${year}`

$('#listarVendasHoje').on('click', function(){ 
    chamarApiVenda(dataDeHoje)
});

$('#listaTodasVendas').on('click', function(){ 
    chamarApiVenda()
});

$( document ).ready(function() {
    chamarApiVenda(dataDeHoje)
});

async function chamarApiVenda(dataHoje){
    if (dataHoje){
        var response = await fetch(`api/dados_vendas/${dataHoje}`);
    }
    else{
        var response = await fetch(`api/dados_vendas`);   
    }
    let data = await response.json();

    // console.log(`Index: ${Object.getOwnPropertyNames(data[0])}`);
    // console.log(`Dados: ${data[0]}`)
    

    insertVendas(data)
}

function insertVendas(data){

    $('#listVendas').empty()

    data.forEach(element => {
        var cliente

        element.cliente == null ?  cliente = 'Cliente não cadastrado' : cliente = element.cliente.nomeCompleto 

        if(element.finalizado){
            $('#listVendas').append(`
                <li class="card p-1 mb-1 shadow">
                    <div>
                        
                        <h6 class="text-success"> 
                            ID: ${element.id} - Valor: R$ ${element.valor.toFixed(2)} - Cliente: ${cliente} - Data da Compra: ${new Date(Date.parse(element.dataCadastro)).toLocaleDateString('pt-BR')}
                        </h6>
                    </div>
                </li>
            `)
        }
        

    });
}