$('#listarprodutos').on('click', function(){
    chamarApiproduto()
});

$( document ).ready(function() {
    chamarApiproduto()
});

async function chamarApiproduto(){

    let response = await fetch('api/dados_produtos');
    let data = await response.json();

    console.log(`Index: ${Object.getOwnPropertyNames(data)}`);
    console.log(`Dados: ${data[0].nome}`)
    
    insertprodutos(data)
}

function insertprodutos(data){

    // $('#listprodutos').empty()

    // data.forEach(element => {
    //     $('#listprodutos').append(`
    //         <li class="card p-1 mb-1 shadow">
    //             <h6 class="text-success"> 
    //                 ${element.nomeCompleto}
    //             </h6>

    //             <div class="row">
    //                 <div class="col">
    //                     <b>CPF:</b> <span class="text-success">${element.cpf}</span>
    //                 </div>

    //                 <div class="col">
    //                     <b>Celular:</b> <span class="text-success">${element.celular}</span>
    //                 </div>

    //                 <div class="col">
    //                     <b>Endereço:</b> <span class="text-success">${element.endereco}</span>
    //                 </div>

    //             </div>
    //         </li>
    //     `)
    // });
}