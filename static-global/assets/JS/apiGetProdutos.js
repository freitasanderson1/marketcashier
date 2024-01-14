$('#listarProdutos').on('click', function(){
    chamarApiproduto()
});

$( document ).ready(function() {
    chamarApiproduto()
});

async function chamarApiproduto(){

    let response = await fetch('api/dados_produtos');
    let data = await response.json();

    // console.log(`Index: ${Object.getOwnPropertyNames(data)}`);
    // console.log(`Dados: ${data}`)
    
    insertprodutos(data)
}

function insertprodutos(data){

    $('#listProdutos').empty()

    data.forEach(element => {
        if(element.unidadePeso){
            var unidadePeso = 'Unidades'
        }
        else{
            var unidadePeso = 'KGs'
        }

        $('#listProdutos').append(`
            <li class="card p-2 mb-1 shadow">
                <div class="row">
                    <div class="col"> 
                        <b class="text-success">${element.nome}</b>
                    </div>
                    <div class="col">
                        <b>Código:</b> <span class="text-success">${element.codigo}</span>
                    </div>
                    <div class="col">
                        <b>Estoque:</b> <span class="text-success">${element.estoque} ${unidadePeso}</span>
                    </div>

                    <div class="col">
                        <b>Preço:</b> <span class="text-success">${element.preco.toLocaleString('pt-BR', { style: 'currency', currency: 'BRL' })}</span>
                    </div>
                    <div class="col d-flex justify-content-center">
                        <button type="button" class="btn btn-success btn-update-product" 
                            data-ms-id="${element.id}" 
                            data-ms-nome="${element.nome}" 
                            data-ms-codigo="${element.codigo}" 
                            data-ms-estoque="${element.estoque}"
                            data-ms-preco="${element.preco}"
                            data-ms-unidadepeso="${element.unidadePeso}"
                            data-bs-toggle="modal" data-bs-target="#modalEditProduct">
                            Editar
                        </button>
                    </div>
                </div>
            </li>
        `)

        $('.btn-update-product').on('click', function(){
            var id = $(this).data('ms-id')
            var nome = $(this).data('ms-nome')
            var codigo = $(this).data('ms-codigo')
            var estoque = $(this).data('ms-estoque')
            var preco = $(this).data('ms-preco')
            var unidadepeso = $(this).data('ms-unidadepeso')

            // console.log(unidadepeso)
            // console.log($(this).data('ms-unidadepeso'))

            $('#modalEditProductLabel').text(`Editando - ${nome}`)

            $('#idProduto').val(`${id}`)
            $('#nomeProduto').val(`${nome}`)
            $('#codigoProduto').val(`${codigo}`)
            $('#estoqueProduto').val(`${estoque}`)
            $('#precoProduto').val(`${preco}`)
            
            if(unidadepeso){
                $('#estoqueProduto').attr('step','1')
            }
            else{
                $('#estoqueProduto').attr('step','0.01')
            }

        })
        
    });
}