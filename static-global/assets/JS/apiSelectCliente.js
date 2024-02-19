$('#termoCliente').on('input', function(){
  var termo = $(this).val()

  // console.log(termo.length,termo)

  if (termo.length > 3){
    chamarApiSelecionarCliete(termo)
  }
})

async function chamarApiSelecionarCliete(termo){

  let response = await fetch(`api/dados_clientes/${termo}`);
  let data = await response.json();

  
  $('#listSelecionarCliente').empty()

  data.clientes.forEach(element => {
    // console.log(`Resposta: ${element.nomeCompleto}`)
    // console.log(`Index: ${Object.getOwnPropertyNames(element)}`);
    
   $('#listSelecionarCliente').append(`
      <li class="card p-2 mb-1 shadow">
        <div class="row">
            <div class="col"> 
                <b class="text-success">${element.nomeCompleto}</b>
            </div>
            <div class="col">
                <b>CPF:</b> <span class="text-success">${element.cpf}</span>
            </div>
            <div class="col">
              <button 
                type="button" 
                class="btn btn-success btn-select-cliente" 
                data-ms-id="${element.id}" 
                data-ms-nome="${element.nomeCompleto}" 
                data-ms-cpf="${element.cpf}"
                data-bs-dismiss="modal"> 
                Selecionar
              </button>
            </div>
        </div>
      </li>
   `)    
  });

  $('.btn-select-cliente').on('click', function(){
    $('#cliente-nome').text($(this).data('ms-nome'))
    $('#client-comprando-id').val($(this).data('ms-id'))
    $('#client-comprando-nome').val($(this).data('ms-nome'))
    $('#client-comprando-cpf').val($(this).data('ms-cpf'))
  })
  
}