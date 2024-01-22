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
                        <button type="button" class="btn btn-success btn-cliente-conta" 
                            data-ms-id="${element.id}" 
                            data-ms-nome="${element.cpf}" 
                            data-bs-toggle="modal" 
                            data-bs-target="#modalContaCliente">
                            <i class="fa-solid fa-circle-dollar-to-slot"></i>
                            Conta
                        </button>
                    </div>
                </div>
            </li>
        `)
    });
}