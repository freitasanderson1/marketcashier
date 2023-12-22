$('#listarClientes').on('click', function(){
    chamarApiCliente()
});

$( document ).ready(function() {
    chamarApiCliente()
});

async function chamarApiCliente(){

    let response = await fetch('api/dados_clientes');
    let data = await response.json();

    // console.log(`Index: ${Object.getOwnPropertyNames(data)}`);
    // console.log(`Dados: ${data[0].nomeCompleto}`)
    
    insertClientes(data)
}

function insertClientes(data){

    $('#listClientes').empty()

    data.forEach(element => {
        $('#listClientes').append(`
            <li class="card p-1 mb-1 shadow">
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

                </div>
            </li>
        `)
    });
}