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

})